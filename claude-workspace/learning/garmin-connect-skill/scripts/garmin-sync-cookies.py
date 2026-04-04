#!/usr/bin/env python3
"""
Garmin Connect Data Sync using saved cookies
Avoids re-login and rate limiting issues
"""

import json
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

try:
    import requests
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry
except ImportError:
    print("❌ requests not installed. Run: pip install requests")
    sys.exit(1)

def create_session_with_cookies(cookies_dict):
    """Create a requests session with Garmin cookies"""
    session = requests.Session()

    # Retry strategy
    retry = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    # Browser-like headers - include NK and HT keys for Garmin API
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Origin': 'https://connect.garmin.com',
        'Referer': 'https://connect.garmin.com/modern/',
        'DI-Backend': 'connectapi.garmin.com',
    })

    # Set cookies for both garmin.com and sso.garmin.com
    for name, value in cookies_dict.items():
        session.cookies.set(name, value, domain='.garmin.com')
        # Also set for SSO domain
        session.cookies.set(name, value, domain='.sso.garmin.com')

    return session

def load_cookies():
    """Load saved Garmin cookies"""
    session_file = Path.home() / ".garth" / "session.json"

    if not session_file.exists():
        print(f"❌ No session file found at {session_file}")
        return None

    try:
        with open(session_file, 'r') as f:
            data = json.load(f)

        if 'cookies' not in data:
            print("❌ No cookies found in session file")
            return None

        return data['cookies']
    except Exception as e:
        print(f"❌ Failed to load cookies: {e}")
        return None

def test_session(session):
    """Test if the session is valid by fetching user profile"""
    try:
        url = "https://connect.garmin.com/userprofile-service/socialProfile"
        response = session.get(url, timeout=30)

        if response.status_code == 200:
            data = response.json()
            if 'username' in data or 'displayName' in data:
                return True, data
        return False, None
    except Exception as e:
        return False, None

def get_daily_summary(session, date_str):
    """Get daily summary using cookies"""
    data = {
        'steps': 0,
        'heart_rate_resting': 0,
        'heart_rate_min': 0,
        'heart_rate_max': 0,
        'calories': 0,
        'calories_active': 0,
        'calories_bmr': 0,
        'active_minutes': 0,
        'distance_km': 0,
        'floors_ascended': 0,
        'floors_descended': 0,
        'intensity_minutes': 0,
        'moderate_intensity_minutes': 0,
        'vigorous_intensity_minutes': 0,
    }

    try:
        # Get user summary
        url = f"https://connect.garmin.com/usersummary-service/usersummary/daily/{date_str}"
        response = session.get(url, timeout=30)

        if response.status_code == 200:
            summary = response.json()
            if 'dailySummary' in summary:
                s = summary['dailySummary']
                data['steps'] = s.get('totalSteps', 0)
                data['heart_rate_resting'] = s.get('restingHeartRate', 0)
                data['calories'] = s.get('totalKilocalories', 0)
                data['active_minutes'] = s.get('intensityMinutes', 0)
                data['distance_km'] = round(s.get('totalDistanceMeters', 0) / 1000, 2)

        # Get stats
        url = f"https://connect.garmin.com/wellness-service/wellness/dailySummaryData/{date_str}"
        response = session.get(url, timeout=30)

        if response.status_code == 200:
            stats = response.json()
            if 'dailySummary' in stats:
                s = stats['dailySummary']
                data['heart_rate_min'] = s.get('minHeartRate', 0)
                data['heart_rate_max'] = s.get('maxHeartRate', 0)
                data['calories_active'] = s.get('activeKilocalories', 0)
                data['calories_bmr'] = s.get('bmrKilocalories', 0)
                data['floors_ascended'] = s.get('floorsAscended', 0)
                data['floors_descended'] = s.get('floorsDescended', 0)

    except Exception as e:
        print(f"⚠️  Daily summary error: {e}", file=sys.stderr)

    return data

def get_sleep_data(session, date_str):
    """Get sleep data using cookies"""
    data = {
        'duration_hours': 0,
        'duration_minutes': 0,
        'quality_percent': 0,
        'deep_sleep_hours': 0,
        'rem_sleep_hours': 0,
        'light_sleep_hours': 0,
        'awake_minutes': 0,
        'nap_count': 0,
        'nap_total_minutes': 0,
        'nap_details': [],
        'sleep_source': 'none',
    }

    try:
        url = f"https://connect.garmin.com/wellness-service/wellness/dailySleepData/{date_str}"
        response = session.get(url, timeout=30)

        if response.status_code == 200:
            sleep_data = response.json()

            if 'dailySleepDTO' in sleep_data:
                s = sleep_data['dailySleepDTO']

                def safe_div(value, divisor, default=0):
                    if value is None:
                        return default
                    try:
                        return round(value / divisor, 1)
                    except (TypeError, ZeroDivisionError):
                        return default

                duration_sec = s.get('sleepTimeSeconds') or 0

                # Check for nap promotion
                nap_to_promote = None
                if duration_sec == 0 and 'dailyNapDTOS' in s and s['dailyNapDTOS']:
                    for nap in s['dailyNapDTOS']:
                        nap_sec = nap.get('napTimeSec', 0)
                        nap_min = round(nap_sec / 60, 0)

                        if nap_min < 180:
                            continue

                        start_gmt = nap.get('napStartTimestampGMT', '')
                        if start_gmt:
                            start_dt = datetime.fromisoformat(start_gmt.replace('Z', '+00:00'))
                            start_local = start_dt + timedelta(hours=8)
                            start_hour = start_local.hour

                            if start_hour >= 22 or start_hour < 10:
                                nap_to_promote = nap
                                break

                if nap_to_promote:
                    nap_sec = nap_to_promote.get('napTimeSec', 0)
                    data['duration_hours'] = safe_div(nap_sec, 3600)
                    data['duration_minutes'] = safe_div(nap_sec, 60)
                    data['quality_percent'] = 70
                    data['sleep_source'] = 'promoted_nap'
                    print(f"💤 Nap promoted to main sleep: {data['duration_hours']}h", file=sys.stderr)
                else:
                    data['duration_hours'] = safe_div(duration_sec, 3600)
                    data['duration_minutes'] = safe_div(duration_sec, 60)
                    data['quality_percent'] = s.get('sleepQualityPercentage') or 0
                    data['deep_sleep_hours'] = safe_div(s.get('deepSleepSeconds'), 3600)
                    data['rem_sleep_hours'] = safe_div(s.get('remSleepSeconds'), 3600)
                    data['light_sleep_hours'] = safe_div(s.get('lightSleepSeconds'), 3600)
                    data['awake_minutes'] = safe_div(s.get('awakeTimeSeconds'), 60)

                    if duration_sec > 0:
                        data['sleep_source'] = 'main'

                # Nap data
                if 'dailyNapDTOS' in s and s['dailyNapDTOS']:
                    data['nap_count'] = len(s['dailyNapDTOS'])
                    for nap in s['dailyNapDTOS']:
                        nap_sec = nap.get('napTimeSec', 0)
                        nap_min = round(nap_sec / 60, 0)
                        data['nap_total_minutes'] += nap_min

                        start_gmt = nap.get('napStartTimestampGMT', '')
                        end_gmt = nap.get('napEndTimestampGMT', '')

                        if start_gmt and end_gmt:
                            start_dt = datetime.fromisoformat(start_gmt.replace('Z', '+00:00'))
                            end_dt = datetime.fromisoformat(end_gmt.replace('Z', '+00:00'))
                            start_local = start_dt + timedelta(hours=8)
                            end_local = end_dt + timedelta(hours=8)

                            data['nap_details'].append({
                                'duration_minutes': nap_min,
                                'start_time': start_local.strftime('%H:%M'),
                                'end_time': end_local.strftime('%H:%M'),
                            })

    except Exception as e:
        print(f"⚠️  Sleep data error: {e}", file=sys.stderr)

    return data

def get_workouts(session):
    """Get recent workouts using cookies"""
    workouts = []

    try:
        # Get activities from Garmin
        url = "https://connect.garmin.com/activitylist-service/activities/search/activities?start=0&limit=20"
        response = session.get(url, timeout=30)

        if response.status_code == 200:
            activities_data = response.json()

            if 'activityList' in activities_data:
                for activity in activities_data['activityList'][:10]:
                    act = activity.get('activity', {})

                    start_time_gmt = act.get('startTimeGMT', None)
                    timestamp = 0
                    date_str = ''

                    if start_time_gmt:
                        try:
                            dt = datetime.fromisoformat(start_time_gmt.replace('Z', '+00:00'))
                            timestamp = int(dt.timestamp())
                            date_str = dt.strftime('%Y-%m-%d')
                        except Exception as e:
                            print(f"⚠️  Failed to parse startTimeGMT: {e}", file=sys.stderr)

                    workout = {
                        'type': act.get('activityType', 'Unknown'),
                        'name': act.get('activityName', 'Unnamed'),
                        'distance_km': round(act.get('distanceMeters', 0) / 1000, 2),
                        'duration_minutes': round(act.get('durationSeconds', 0) / 60, 0),
                        'calories': act.get('calories', 0),
                        'heart_rate_avg': act.get('averageHR', 0),
                        'heart_rate_max': act.get('maxHR', 0),
                        'timestamp': timestamp,
                        'date': date_str,
                    }
                    workouts.append(workout)

    except Exception as e:
        print(f"⚠️  Workouts error: {e}", file=sys.stderr)

    return workouts

def sync_all(output_file=None):
    """Sync all Garmin data using cookies"""

    cookies = load_cookies()
    if not cookies:
        return None

    session = create_session_with_cookies(cookies)

    # Test session
    print("🔍 Testing session...", file=sys.stderr)
    is_valid, profile = test_session(session)

    if not is_valid:
        print("❌ Session is invalid or expired. Please re-authenticate.", file=sys.stderr)
        print("Run: python3 garmin-auth.py <email> <password>", file=sys.stderr)
        return None

    print(f"✅ Session valid for user: {profile.get('displayName', 'Unknown')}", file=sys.stderr)

    # Get date (Beijing time)
    beijing_tz = timezone(timedelta(hours=8))
    now_beijing = datetime.now(beijing_tz)
    hour = now_beijing.hour

    if hour < 5:
        target_date = (now_beijing - timedelta(days=1)).strftime("%Y-%m-%d")
    else:
        target_date = now_beijing.strftime("%Y-%m-%d")

    # Get workouts first to determine actual date
    workouts = get_workouts(session)

    actual_date = target_date
    if workouts and len(workouts) > 0:
        for workout in workouts:
            if 'date' in workout and workout['date']:
                workout_date = workout['date']
                workout_dt = datetime.strptime(workout_date, '%Y-%m-%d')
                target_dt = datetime.strptime(target_date, '%Y-%m-%d')
                diff = abs((workout_dt - target_dt).days)

                if diff <= 1:
                    actual_date = workout_date
                    break

    # Collect all data
    all_data = {
        'timestamp': datetime.now().isoformat(),
        'date': actual_date,
        'summary': get_daily_summary(session, actual_date),
        'sleep': get_sleep_data(session, actual_date),
        'workouts': workouts,
        'vo2_max': {'vo2_max': 0, 'vo2_max_precise': 0},
        'body_battery': {'charged': 0, 'drained': 0, 'highest': 0, 'lowest': 0, 'current': 0, 'most_recent': 0},
        'stress': {'average': 0, 'max': 0},
        'hrv': {'hrv_last_night': 0},
        'fitness_age': {'fitness_age': 0},
        'respiration': {'avg_respiration': 0},
        'lactate_threshold': {'ftp_watts': 0},
    }

    # Save to file if specified
    if output_file:
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, 'w') as f:
            json.dump(all_data, f, indent=2)

    # Print JSON to stdout
    print(json.dumps(all_data, indent=2))

    return all_data

if __name__ == "__main__":
    # Default cache file
    cache_file = os.path.expanduser('~/.clawdbot/.garmin-cache.json')

    # Use custom path if provided
    if len(sys.argv) > 1:
        cache_file = sys.argv[1]

    sync_all(cache_file)
