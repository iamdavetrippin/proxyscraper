import requests
import time
import random
import sys
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

sources = [
    "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    "https://www.proxy-list.download/api/v1/get?type=http",
    "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
]

ascii_banner = r"""
  ____                      _____                                  
 |  _ \ _ __ ___  ___ _ __ | ____|_ __   ___ __ _ _ __   ___ _ __  
 | |_) | '__/ _ \/ _ \ '_ \|  _| | '_ \ / __/ _` | '_ \ / _ \ '__| 
 |  __/| | |  __/  __/ | | | |___| | | | (_| (_| | |_) |  __/ |    
 |_|   |_|  \___|\___|_| |_|_____|_| |_|\___\__,_| .__/ \___|_|    
                                                 |_|              
       by iamdavetrippin |
"""

spinner_chars = ['|', '/', '-', '\\']
def spinner(duration=2):
    print(Fore.YELLOW + "[*] Initializing scraper ", end="")
    for _ in range(duration * 4):
        for c in spinner_chars:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write('\b')

def scrape_proxies():
    proxies = set()
    print(Fore.CYAN + "\n[+] Starting proxy scraping from sources...\n")
    for url in sources:
        try:
            print(Fore.YELLOW + f"[>] Fetching from: {url}")
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                new_proxies = response.text.strip().split('\n')
                proxies.update(new_proxies)
                print(Fore.GREEN + f"[+] Retrieved {len(new_proxies)} proxies.")
            else:
                print(Fore.RED + f"[!] Failed to fetch from {url}")
        except Exception as e:
            print(Fore.RED + f"[!] Error: {str(e)}")
        time.sleep(1)
    return proxies

def save_to_file(proxies):
    with open("proxies.txt", "w") as f:
        for proxy in proxies:
            f.write(proxy.strip() + "\n")
    print(Fore.MAGENTA + f"\n[✔] Saved {len(proxies)} proxies to proxies.txt\n")

def main():
    print(Fore.LIGHTBLUE_EX + ascii_banner)
    spinner()
    proxies = scrape_proxies()
    save_to_file(proxies)
    print(Fore.GREEN + "[*] Done. You can now use your proxies. Happy scraping!\n")

if __name__ == "__main__":
    main()
