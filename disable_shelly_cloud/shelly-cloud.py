import requests as r
from concurrent.futures import ThreadPoolExecutor
from browser import *
import subprocess


ip_bases = ["192.168.1.", "192.168.2."]
results = {}

def check_ip(ip):
    command = ["ping", "-c", "1", "-W", "2", ip]

    result = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if result.returncode == 0:
        return True
    else:
        return False


def call(url: str):
    try:
        # Added a general exception catch to prevent crashes on 'Refused' or 'No route'
        response = r.get(f"http://{url}", timeout=5)
        if response.status_code == 200:
            return response.json()
    except Exception:
        pass
    return False


def is_cloud_enabled(json_text):
    cloud = json_text['cloud']['connected']
    return cloud


def main(ip: str):
    if not check_ip(ip):
        print(f"{ip}\tNo Host")
        return
    

    new_shelly = True
    # old shelly
    state = call(ip + '/status')
    if state:
        new_shelly = False
    # new shelly
    else:
        state = call(ip + '/rpc/Shelly.GetStatus')
        if not state:
            # not a shelly
            print(f"{ip}\tNo Shelly")
            return
    
    # is a shelly
    cloud = is_cloud_enabled(state)
    print(f"{ip}\t{'Enabled' if cloud else 'Disabled'}")
    if cloud:
        if new_shelly:
            results[ip] = 'new'
        else:
            results[ip] = 'old'


# Generate list of IPs
all_ips = [f"{base}{i}" for base in ip_bases for i in range(256)]

def collection():
    with ThreadPoolExecutor(max_workers=500) as executor:
        executor.map(main, all_ips)

if __name__ == '__main__':
    collection()

    print("Cloud enabled:")
    for k, v in results.items():
        print(f"{k}\t{v}")
    
    print("Starting disabling")
    for ip, version in results.items():
        if version == 'new':
            res = disable_cloud_new(ip)
        elif version == 'old':
            res = disable_cloud_old(ip)
        else:
            raise RuntimeError("Something is messed up")
        
        if res:
            print(f"{ip}: Cloud disabled succesfully")
        else:
            raise RuntimeError(f"Could not disable the Cloud for {ip}")
    
    print("\n Done!")