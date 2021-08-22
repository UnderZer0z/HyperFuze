from asyncio.tasks import wait
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
import json
import time
import os


# gatting vals
load_dotenv(dotenv_path='discord_bot/.env')
ip = '51.178.91.185:41413'
ip1 = '54.38.154.47:2302'
gt_serv = 'http://www.gametracker.com/server_info/'
gt_login = 'http://www.gametracker.com/servers'

upass = os.getenv('PASS')
uname = os.getenv('NAME')

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
}



def get_serv_stat(ip):
    r = requests.get(gt_serv + ip)
    soup = BeautifulSoup(r.content,'lxml')
    try:
        is_server_dead = soup.find(class_='item_color_success').text.strip()
    except:
        is_server_dead = 'Dead'
    players_num = soup.find( id="HTML_num_players" ).text
    players_max = soup.find( id="HTML_max_players" ).text
    print("server status: " + is_server_dead)
    print("number of players: " + players_num)
    print("max number of players: " + players_max)
    # print_page(soup)
    

def add_sevrer():
    with requests.session() as s:
        s.get(gt_login , headers=header)
        form = {"username": uname ,'password': upass , 'submit': 'LOGIN'}
        print(form)
        s1 = s.post(gt_login, data=form , headers=header)
        print(s1.headers)


    # with open('debug.html', 'a', encoding="utf-8") as f:
    #     f.write(r.text)
    #     f.close()

    # logout = requests.post(gt_login, { 'logout': 1 } )
    # # print(logout.cookies)


def load_json():
    with open('./servers.json', 'r') as f:
        server_list = json.load(f)
        f.close()
        return server_list


def save_json(data):
    ts = time.time()
    server_list = load_json()
    scan_new = get_serv_stat(data.ip)

    server_scan = {
        "Name":data.name,
        "IP":data.ip,
        "description": data.description,
        "gameMode": data.gamemode,
        "maxPlayer": scan_new.players_max,
        "playerNum":scan_new.players_num,
        "lastScanTimestamp": ts ,
        "addedBy":data.user,
        "addedTime": ts
    }

    server_list.append(server_scan)


    with open('./servers.json', 'w') as f:
        f.write()
        f.close()




#  ============= test area =============

add_sevrer()

# newdata = load_json()
# print(newdata['Minecarft'][0]['Name'])



# if __name__ == '__main__':
    # get_serv_stat(ip1)
