import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def login(driver):
    '''
    log bot into twitch 
    '''
    driver.get('http://www.twitch.tv/login');
    time.sleep(5) 
    elem_user = driver.find_element_by_id("login-username") # username entry field
    elem_user.click()
    elem_user.send_keys('testetsttest', Keys.TAB) # switch to the password entry field
    elem_pw = driver.switch_to.active_element
    time.sleep(3)
    elem_pw.send_keys('password', Keys.ENTER)

def get_current_location(driver): 
    print(driver.current_url)

def elb_gogogo():
    '''
    navigate to electricallongboard
    '''
    print("going to ELB...")


if __name__ == "__main__":    
    print("<...logging in...>")
    driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
    login(driver)
    get_current_location(driver)
    print("<DONE>")


