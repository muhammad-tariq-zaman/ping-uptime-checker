import subprocess, sys, platform
def ping(host, count=1, timeout=2):
    flag = "-n" if platform.system() == "Windows" else "-c"
    try:
        r = subprocess.run(["ping", flag, str(count), host], capture_output=True, text=True, timeout=timeout + 2)
        return r.returncode == 0
    except Exception:
        return False
if __name__ == "__main__":
    hosts = sys.argv[1:] or ["127.0.0.1"]
    for h in hosts:
        print(f"{h}: {'UP' if ping(h) else 'DOWN'}")
