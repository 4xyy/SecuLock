from honeypot_manager import deploy_honeypots
from breach_detector import monitor_honeypots
from incident_responder import handle_breach

if __name__ == "__main__":
    print("Deploying honeypot credentials across platforms...")
    deploy_honeypots()

    print("Monitoring honeypot credentials for usage...")
    breach_detected, ip, geo_info = monitor_honeypots()
    if breach_detected:
        print(f"Breach detected from IP: {ip} | Location: {geo_info}")
        print("Initiating incident response...")
        handle_breach()
