import requests
import argparse
import base64
import sys
import json

def banner():
    print("""
\033[1;36m    __               __                               \033[0m
\033[1;36m   [  ]             [  ]                              \033[0m
\033[1;36m   |  |             |  |     \     _ .--.  ------     \033[0m
\033[1;36m   |  |.--..------  |  |.--.----- [ `.-. | /     \    \033[0m
\033[1;36m   |      \/      \ |      \    / | |  | | |           \033[0m 
\033[1;36m   |      ||        |      |   /  | |  | |  \__ _ _| fofa \033[0m
\033[1;36m   |.__ _/  \__ _ _||.__ _/   /__[___| [__]        |   \033[0m
\033[1;36m                   |                               |    \033[0m
\033[1;36m                   |                         \__ _ /      \033[0m    
\033[1;36m             \__ _ /           """)
    print("\n")
    print('\033[1;36m   fofa采集工具使用方法\033[0m')
    print("\n")
    print('\033[1;36m           python3 bgbingfofa.py -e/--email email -k/--key key -s/--size size\033[0m')
    print("\n")
    print('\033[1;36m           python3 bgbingfofa.py -h/--help\033[0m')
    print("\n")
if len(sys.argv)==1:
    banner()
    sys.exit()
parser = argparse.ArgumentParser(description='bgbingfofaapi help')
parser.add_argument('-e','--email', help='Please Input a email!',default='')
parser.add_argument('-k','--key', help='Please Input a key!',default='')
parser.add_argument('-s','--size', help='Please Input size!',default='')
args=parser.parse_args()
email=args.email
key=args.key
size=args.size
url="https://fofa.so/api/v1/info/my?email="+email+"&key="+key
header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    "Content-Type":"application/x-www-form-urlencoded"
        }
response=requests.get(url,headers=header)
if 'errmsg' not in response.text:
    print("\033[1;32memail和key均正确\033[0m")
    while 1:
        sentence=input("\033[1;36mfofa语句 >>>\033[0m")
        sentence=base64.b64encode(sentence.encode('utf-8')).decode("utf-8")
        url="https://fofa.so/api/v1/search/all?email="+email+"&key="+key+"&qbase64="+sentence+"&size="+size
        response=requests.get(url,headers=header)
        if 'errmsg' not in response.text:
            print("\033[1;36m已保存到\033[0m\033[1;32mresult.txt\033[0m")
            r1 = json.loads(response.text)
            for i in r1['results']:
                s=i[0]
                f = open('result.txt','a')
                f.write(s+"\n")
        else:
            print("\033[1;31mfofa语句不正确\033[0m")
else:
    print("\033[1;31memail或key不正确\033[0m")
