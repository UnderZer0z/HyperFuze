import requests
from bs4 import BeautifulSoup


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



def print_page(soup):
    with open('page.html','w') as f:
        f.write(str(soup))
        f.close()



if __name__ == '__main__':
    get_serv_stat(ip1)