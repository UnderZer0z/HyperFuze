import requests
from bs4 import BeautifulSoup

ip = '149.202.88.8:25565'
gt_serv = 'https://www.gametracker.com/server_info/'

def serv_stat(ip):
    r = requests.get(gt_serv + ip)
    soup = BeautifulSoup(r.content,'lxml')
    players_num = soup.find( id="HTML_num_players" ).text
    players_max = soup.find( id="HTML_num_players" ).text

    print("number of players: " + players_num)
    print("max number of players: " + players_max)


serv_stat(ip)


# with open('page.html','w') as f:
#     f.write(str(soup))
#     f.close()