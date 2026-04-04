#!/usr/bin/env python3
"""
Garmin Authentication using current garth library API
"""

import base64
import json
import os
import sys
from pathlib import Path

def setup_garth_auth(email, password, is_cn=False):
    """Authenticate using garth library"""
    try:
        import garth

        region = "China (garmin.cn)" if is_cn else "Global (garmin.com)"
        print(f"🔐 Authenticating with Garmin {region} ({email})...")

        # Set domain if needed
        if is_cn:
            garth.client.Client.configure(domain="garmin.cn")

        # Login
        try:
            garth.login(email, password)
            print("✅ Login successful!")

            # Save session
            garth.save()

            # Also save simplified credentials for garmin-sync.py
            garth_dir = Path.home() / ".garth"
            session_file = garth_dir / "session.json"

            encoded_password = base64.b64encode(password.encode()).decode()

            session_info = {
                "email": email,
                "password_encrypted": encoded_password,
                "region": "CN" if is_cn else "GLOBAL",
                "is_cn": is_cn,
            }

            with open(session_file, 'w') as f:
                json.dump(session_info, f, indent=2)

            os.chmod(session_file, 0o600)
            print(f"✅ Session saved to {session_file}")
            print("✅ You can now use garmin-sync.py")
            return True

        except Exception as e:
            print(f"❌ Login failed: {e}")
            print("\n可能的原因:")
            print("- 账号密码错误")
            print("- 账号被锁定")
            print("- 网络问题")
            return False

    except ImportError:
        print("❌ garth library not installed. Run: pip install garth")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 garmin-auth-final.py <email> <password> [--cn]")
        print("\nExamples:")
        print("  Global: python3 garmin-auth-final.py user@example.com password123")
        print("  China:  python3 garmin-auth-final.py user@qq.com password123 --cn")
        sys.exit(1)

    email = sys.argv[1]
    password = sys.argv[2]
    is_cn = "--cn" in sys.argv

    success = setup_garth_auth(email, password, is_cn)
    sys.exit(0 if success else 1)
