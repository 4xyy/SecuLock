import requests
import random

def get_geolocation(ip):
    response = requests.get(f'https://ipinfo.io/{ip}/json')
    return response.json() if response.status_code == 200 else {}

def check_breach_attempts():
    ip_address = "127.0.0.1"  
    print(f"Simulated breach attempt from IP: {ip_address}")

    geo_info = get_geolocation(ip_address)
    print(f"Geolocation Info: {geo_info}")

    return True, ip_address, geo_info

def monitor_honeypots():
    breach_detected, ip, geo_info = check_breach_attempts()
    if breach_detected:
        return True, ip, geo_info
    return False, None, None
