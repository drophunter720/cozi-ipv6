#!/usr/bin/env python3
import hmac
import hashlib
import sys

def generate_api_token(user_agent, shared_secret):
    """Generate API token for i6.shark proxy"""
    key = user_agent.encode()
    h = hmac.new(key, shared_secret.encode(), hashlib.sha256)
    return h.hexdigest()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 generate_token.py 'Your-User-Agent-String'")
        print("Example: python3 generate_token.py 'MyApp/1.0'")
        sys.exit(1)
    
    user_agent = sys.argv[1]
    shared_secret = "aeza-vps-2a0b4140df47-secure-key-2024"
    
    token = generate_api_token(user_agent, shared_secret)
    
    print(f"User-Agent: {user_agent}")
    print(f"API-Token: {token}")
    print(f"\nTest command:")
    print(f"curl 'http://YOUR_VPS_IP/?url=https://httpbin.org/ip' \\")
    print(f"  -H 'API-Token: {token}' \\")
    print(f"  -H 'User-Agent: {user_agent}'")
