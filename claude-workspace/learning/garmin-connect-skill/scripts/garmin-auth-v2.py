#!/usr/bin/env python3
"""
Garmin Authentication with better browser simulation
"""

import base64
import json
import os
import sys
from pathlib import Path

try:
    import requests
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry
except ImportError:
    print("❌ requests not installed. Run: pip install requests")
    sys.exit(1)

def create_session():
    """Create a requests session with retry and browser-like headers"""
    session = requests.Session()

    # Retry strategy
    retry = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    # Browser-like headers
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Cache-Control': 'max-age=0',
    })

    return session

def save_credentials(email, password, is_cn=False):
    """Save credentials to file"""
    garth_dir = Path.home() / ".garth"
    session_file = garth_dir / "session.json"

    encoded_password = base64.b64encode(password.encode()).decode()

    session_info = {
        "email": email,
        "password_encrypted": encoded_password,
        "region": "CN" if is_cn else "GLOBAL",
        "is_cn": is_cn,
    }

    garth_dir.mkdir(exist_ok=True)

    with open(session_file, 'w') as f:
        json.dump(session_info, f, indent=2)

    os.chmod(session_file, 0o600)
    print(f"✅ Credentials saved to {session_file}")
    return True

def authenticate_garth(email, password, is_cn=False):
    """Try using garth library directly"""
    try:
        from garth import GarminClient

        region = "China (garmin.cn)" if is_cn else "Global (garmin.com)"
        print(f"🔐 Using garth library for {region}...")

        # Create client
        client = GarminClient(email=email, password=password, is_cn=is_cn)

        # Try to login
        client.login()

        print("✅ Login successful with garth!")
        save_credentials(email, password, is_cn)
        return True

    except ImportError:
        print("⚠️  garth library not available")
        return False
    except Exception as e:
        print(f"⚠️  garth login failed: {e}")
        return False

def authenticate_manual(email, password, is_cn=False):
    """Manual OAuth flow - user logs in via browser"""
    print("\n🌐 尝试浏览器登录方式...")
    print("请按以下步骤操作：")
    print("1. 在浏览器中访问: https://connect.garmin.com/")
    print("2. 登录你的账号")
    print("3. 登录成功后，打开浏览器开发者工具 (F12)")
    print("4. 切换到 Application/存储 标签")
    print("5. 找到 Cookies → https://connect.garmin.com")
    print("6. 复制以下 Cookie 的值：")
    print("   - GARMIN-SSO-GUID")
    print("   - SESSIONID")
    print("\n输入 GARMIN-SSO-GUID 的值 (或按 Enter 跳过):")

    sso_guid = input().strip()

    if not sso_guid:
        return False

    print("输入 SESSIONID 的值:")
    session_id = input().strip()

    if session_id:
        # Save cookies
        save_credentials(email, password, is_cn)

        # Update session file with cookies
        garth_dir = Path.home() / ".garth"
        session_file = garth_dir / "session.json"

        with open(session_file, 'r') as f:
            data = json.load(f)

        data['cookies'] = {
            'GARMIN-SSO-GUID': sso_guid,
            'SESSIONID': session_id,
        }

        with open(session_file, 'w') as f:
            json.dump(data, f, indent=2)

        os.chmod(session_file, 0o600)
        print("✅ Cookies saved!")
        return True

    return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        email = input("Garmin email: ")
        password = input("Password: ")
        cn_input = input("Use China region (garmin.cn)? [y/N]: ").strip().lower()
        is_cn = cn_input == 'y' or cn_input == 'yes'
    else:
        email = sys.argv[1]
        password = sys.argv[2]
        is_cn = "--cn" in sys.argv

    # Try garth library first
    if authenticate_garth(email, password, is_cn):
        print("\n✅ 认证成功！你可以使用 garmin-sync.py 同步数据了。")
        sys.exit(0)

    # Fall back to manual cookie method
    if authenticate_manual(email, password, is_cn):
        print("\n✅ Cookies 已保存！你可以使用 garmin-sync.py 同步数据了。")
        sys.exit(0)

    print("\n❌ 认证失败")
    sys.exit(1)
