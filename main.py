import requests
from itertools import cycle

#download fresh proxies
requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all")
px = open("proxies.txt", "w")
px.write(str(x.text)) 
px.close()

#proxies
proxies = []
rotating = cycle(proxies)

#load proxies
try:
    f = open("proxies.txt", "r+")
    for line in f:
        if line.strip():
            proxies.append(line.strip())
except Exception as e:
    print(f"    [!] ERROR: {e}")
    time.sleep(5)
    exit()