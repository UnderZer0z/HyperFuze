from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import time
import os



# ==[loading the dotenv flie values]
load_dotenv(dotenv_path='discord_bot/.env')
upass = os.getenv('PASS')
uname = os.getenv('NAME')



# ==[stting up the chorme driver for selenium] 
PATH = 'discord_bot\chromedriver.exe'
driver = webdriver.Chrome(PATH)


def login_in(uname, upass):
    driver.get('http://www.gametracker.com/servers')
    # adding the username
    username = driver.find_element_by_name('username')
    username.send_keys(uname)
    # adding the user password
    password = driver.find_element_by_name('password')
    password.send_keys(upass)

    loginbtn = driver.find_element_by_name('submit')
    loginbtn.submit()

    print('waiting for loading')
    time.sleep(5)


# game,ip,port
def addserver():
    game = 'Minecraft' # test value's
    ip = '127.0.0.1'
    port = '25565
    '
    # select game type
    option = driver.find_element_by_xpath('//select[@name="GMID"]/option[text()="'+ game +'"]')
    option.click()
    
    # adds the ip_address
    ip_input = driver.find_element_by_id("ip_address")
    ip_input.send_keys(ip)


    time.sleep(5)



def logout():
    logoutbtn = driver.find_element_by_xpath('//input[@alt="Log Out"]')
    logoutbtn.click()
    time.sleep(5)



def main(uname, upass):
    login_in(uname, upass)
    addserver()
    logout()
    driver.quit()


main(uname, upass)