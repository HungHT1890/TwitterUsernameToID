from requests import session
from colorama import Fore
import os,threading,codecs,re
xanh , do = Fore.GREEN,Fore.RED
ss = session()
def convertID(username):
    global error,hits,checked
    api = f'https://findidfb.com/find-twitter-id/'
    header = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '16',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://findidfb.com',
        'referer': 'https://findidfb.com/find-twitter-id/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    data = {
        'user_name_twitter': username
    }
    convert = ss.post(api,headers=header,data=data)
    checked +=1
    if convert.status_code ==200:
        if 'Numeric ID' in convert.text:
            id = re.findall(r'<div>Numeric ID: <b>(\d+)</',convert.text)[0]
            save = (f'{xanh}{username}|{id}')
            print(save)
            with open('Hits\Success.txt','a',encoding='utf-8') as saveSuccess:
                saveSuccess.write(username+'|'+id+'\n')
                hits +=1
        else:
            error +=1
            print(f'{do}username error: {username}')
            with open(r'Hits\Error.txt','a',encoding='utf-8') as saveError:
                saveError.write(username+'\n')
    else:
        error +=1
        print(f'{do}username error: {username}')
        with open(r'Hits\Error.txt','a',encoding='utf-8') as saveError:
            saveError.write(username+'\n')
    os.system('title Twitter ID and username converter by hungsaki2003@gmail.com Success: {} Error: {}'.format(hits,error))
    if checked == len(usernameData):
        input(f'{do}Convert Done !')
        exit()
error = 0
hits = 0
checked = 0
os.system('title Twitter ID and username converter by hungsaki2003@gmail.com Success: {} Error: {}'.format(hits,error))
try:
    with codecs.open('username.txt','r',encoding='unicode_escape') as readFile:
        usernameData = readFile.readlines()
except Exception as usernameFileerror:
    input(f'{do}{usernameFileerror}')
try:
    os.makedirs('Hits')
except:
    pass
def runTools(thread_step):
    for x in range(thread_step,len(usernameData),100):
        username = usernameData[x].strip()
        convertID(username)
input(f'{xanh}Enter to run !')
for x in range(100):
    newThread = threading.Thread(target=runTools,args=(x,))
    newThread.start()