from asyncio.tasks import wait
from bs4 import BeautifulSoup
import requests
import json
import time



# gatting gametracker

ip = '51.178.91.185:41413'
ip1 = '54.38.154.47:2302'
gt_serv = 'https://www.gametracker.com/server_info/'

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


    with open('./servers.json', 'w') as f:
        f.write()
        f.close()





newdata = load_json()
print(newdata['Minecarft'][0]['Name'])




# if __name__ == '__main__':
    # get_serv_stat(ip1)
