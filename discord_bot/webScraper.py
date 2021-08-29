from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from asyncio.tasks import wait
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
import json
import time
import os



# ==[loading the dotenv flie values]
load_dotenv(dotenv_path='discord_bot/.env')
upass = os.getenv('PASS')
uname = os.getenv('NAME')
gt_serv = 'http://www.gametracker.com/server_info/'

# ==[stting up the chorme driver for selenium] 
PATH = 'discord_bot\chromedriver.exe'
driver = webdriver.Chrome(PATH)

# =========================================

    # loging into gametraker
def login_in():
    driver.get('http://www.gametracker.com/servers')
        # adding the username
    username = driver.find_element_by_name('username')
    username.send_keys(uname)
        # adding the user password
    password = driver.find_element_by_name('password')
    password.send_keys(upass)
        # find and press the login butten
    loginbtn = driver.find_element_by_name('submit')
    loginbtn.submit()
    print('waiting for loading')
    time.sleep(5)

# =========================================

    # game,ip,port
def addserver(game , ip, port):
        # select game type
    option = driver.find_element_by_xpath('//select[@name="GMID"]/option[text()="'+ game +'"]')
    option.click()
        # adds the ip_address
    ip_input = driver.find_element_by_id("ip_address")
    ip_input.send_keys(ip)
        # add Port 
    ip_input = driver.find_element_by_id("join_port")
    ip_input.send_keys(port)
        # push submit to GT 
    sub_btn = driver.find_element_by_xpath('//input[@value="Add Server"]')
    sub_btn.click()

    time.sleep(5) #a wait timer.. just to be safe.

# =========================================

    # loging out of gametraker
def logout():
    logoutbtn = driver.find_element_by_xpath('//input[@alt="Log Out"]')
    logoutbtn.click()
    time.sleep(5)




# ==========================================================
# ==========================================================
# ==========================================================


# gets the server status 
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
    

# =========================================


def load_json():
    with open('./servers.json', 'r') as f:
        server_list = json.load(f)
        f.close()
        return server_list

# =========================================


def save_json(data):
    ts = time.time()
    server_list = load_json()
    scan_new = get_serv_stat(data.ip)
    server_scan = {
        "Name":data.name,
        "IP":data.ip,
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


# =========================================

    # the add main loop 
def track_game(game,ip,port): 
    login_in()
    addserver(game,ip,port)
    logout()
    driver.quit()


# =========================================
# testarea