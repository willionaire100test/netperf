import subprocess

print("[*] generate_historical_data.py PoC executed")
print("[*] runner user:", subprocess.check_output(["whoami"], text=True).strip())