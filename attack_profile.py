attack_log = []

def log_attack(ip_address, device):
    attack_details = {
        'ip_address': ip_address,
        'device': device
    }
    attack_log.append(attack_details)
    print(f"Logging attack from IP: {ip_address}, Device: {device}")

def get_attack_log():
    return attack_log
