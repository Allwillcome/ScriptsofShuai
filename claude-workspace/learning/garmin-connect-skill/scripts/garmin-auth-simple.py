#!/usr/bin/env python3
"""
Simple Garmin Authentication using requests only
For international Garmin accounts (garmin.com)
"""

import base64
import json
import os
import sys
from pathlib import Path
from getpass import getpass

try:
    import requests
except ImportError:
    print("❌ requests not installed. Run: pip install requests")
    sys.exit(1)

def setup_oauth_simple(email, password, is_cn=False):
    """Simple OAuth authentication for Garmin"""

    # Determine region
    if is_cn:
        base_url = "https://sso.garmin.cn"
        sso_url = "sso.garmin.cn"
    else:
        base_url = "https://sso.garmin.com"
        sso_url = "sso.garmin.com"

    region = "China (garmin.cn)" if is_cn else "Global (garmin.com)"
    print(f"🔐 Authenticating with Garmin {region} ({email})...")

    session = requests.Session()

    # Step 1: Get login page and CSRF token
    print("  → Getting login page...")
    login_params = {
        'service': 'https://connectapi.garmin.com/oauth-service/oauth/preauthorized',
        'webhost': sso_url,
        'source': 'https://connect.garmin.com',
        'redirectAfterAccountLoginUrl': 'https://connect.garmin.com/modern',
        'redirectAfterAccountCreationUrl': 'https://connect.garmin.com/modern',
        'gauthHost': sso_url,
        'locale': 'en_US',
        'id': 'gauth-widget',
        'cssUrl': 'https://connect.garmin.com/gauth-custom-v1.2-min.css',
        'clientId': 'Garmin Connect',
        'clientRedirectTo': 'https://connect.garmin.com/modern/',
        'rememberMeShown': 'true',
        'rememberMeChecked': 'false',
        'createAccountShown': 'true',
        'openCreateAccount': 'false',
        'displayNameShown': 'false',
        'consumeServiceTicket': 'false',
        'initialFocus': 'true',
        'embedWidget': 'false',
        'generateExtraServiceTicket': 'true',
        'generateTwoExtraServiceTickets': 'false',
        'generateNoServiceTicket': 'false',
        'globalOptInShown': 'true',
        'globalOptInChecked': 'false',
        'mobile': 'false',
        'connectLegalTerms': 'true',
        'locationPromptShown': 'true',
        'showPassword': 'true',
    }

    try:
        response = session.get(
            f"{base_url}/sso/login",
            params=login_params,
            timeout=30
        )

        if response.status_code != 200:
            print(f"❌ Failed to get login page: {response.status_code}")
            return False

        # Get the CSRF token from the response
        csrf_token = None
        if 'csrf' in response.text:
            import re
            match = re.search(r'name="csrf"\s+value="([^"]+)"', response.text)
            if match:
                csrf_token = match.group(1)

        if not csrf_token:
            print("⚠️  Could not find CSRF token, trying anyway...")

        # Step 2: Submit login credentials
        print("  → Submitting credentials...")
        login_data = {
            'username': email,
            'password': password,
            'embed': 'true',
            'selectedLocationId': '',
            'source': 'https://connect.garmin.com',
            'redirectAfterAccountLoginUrl': 'https://connect.garmin.com/modern',
            'redirectAfterAccountCreationUrl': 'https://connect.garmin.com/modern',
            'webhost': sso_url,
            'clientId': 'Garmin Connect',
            'clientRedirectTo': 'https://connect.garmin.com/modern/',
            'gauthHost': sso_url,
            'locale': 'en_US',
            'id': 'gauth-widget',
            'cssUrl': 'https://connect.garmin.com/gauth-custom-v1.2-min.css',
            'clientRequestId': 'garmin-connect-python-client',
            'rememberMeShown': 'true',
            'rememberMeChecked': 'false',
            'createAccountShown': 'true',
            'openCreateAccount': 'false',
            'displayNameShown': 'false',
            'consumeServiceTicket': 'false',
            'initialFocus': 'true',
            'embedWidget': 'false',
            'generateExtraServiceTicket': 'true',
            'generateTwoExtraServiceTickets': 'false',
            'generateNoServiceTicket': 'false',
            'globalOptInShown': 'true',
            'globalOptInChecked': 'false',
            'mobile': 'false',
            'connectLegalTerms': 'true',
            'locationPromptShown': 'true',
            'showPassword': 'true',
        }

        if csrf_token:
            login_data['csrf'] = csrf_token

        # Add the login parameters as form data
        for key, value in login_params.items():
            if key not in login_data:
                login_data[key] = value

        response = session.post(
            f"{base_url}/sso/login",
            data=login_data,
            timeout=30,
            allow_redirects=True
        )

        # Check if login was successful
        if response.status_code != 200:
            print(f"❌ Login failed with status {response.status_code}")
            return False

        # Look for service ticket in response
        if 'ticket=' in response.url or 'service-ticket' in response.text:
            print("✅ Login successful!")

            # Save credentials
            garth_dir = Path.home() / ".garth"
            session_file = garth_dir / "session.json"

            encoded_password = base64.b64encode(password.encode()).decode()

            session_info = {
                "email": email,
                "password_encrypted": encoded_password,
                "region": "CN" if is_cn else "GLOBAL",
                "is_cn": is_cn,
                "oauth_token": response.url.split('ticket=')[-1] if 'ticket=' in response.url else None,
            }

            garth_dir.mkdir(exist_ok=True)

            with open(session_file, 'w') as f:
                json.dump(session_info, f, indent=2)

            os.chmod(session_file, 0o600)

            print(f"✅ Credentials saved to {session_file}")
            print(f"✅ Region: {region}")
            print("✅ You can now use garmin-sync.py")
            return True
        else:
            print("❌ Authentication failed: Invalid credentials or 2FA enabled")
            print("\nCommon issues:")
            print("- Wrong email/password")
            print("- 2FA enabled (disable temporarily)")
            print("- Account locked (try logging in via web)")
            return False

    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
        return False
    except Exception as e:
        print(f"❌ Authentication error: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        email = input("Garmin email: ")
        password = getpass("Password: ")
        cn_input = input("Use China region (garmin.cn)? [y/N]: ").strip().lower()
        is_cn = cn_input == 'y' or cn_input == 'yes'
    else:
        email = sys.argv[1]
        password = sys.argv[2]
        is_cn = "--cn" in sys.argv

    success = setup_oauth_simple(email, password, is_cn)
    sys.exit(0 if success else 1)
