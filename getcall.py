#python3
import requests
import sys
from urllib3.exceptions import InsecureRequestWarning

requests.urllib3.disable_warnings()


url = sys.argv[1]
headers={'User-agent':'Mozilla//5.0',}
r = requests.get(url=url, verify=False,headers=headers)
getcontent = r.content
print(getcontent)
