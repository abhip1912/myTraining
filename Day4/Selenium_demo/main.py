from selenium import webdriver
import  time
ERL_NO = '170303108093'
PASSWORD = '30003'

ERL_NO_ID = 'txtEnrollmentNo'
PASSWORD_ID = 'txtPassword'
LOGIN_BTN_ID = 'btnLogin'

with webdriver.Chrome() as driver:
    driver.get("https://ums.paruluniversity.ac.in/StudentPanel/")
    ernNo = driver.find_element_by_id(ERL_NO_ID)
    ernNo.send_keys(ERL_NO)
    passwd = driver.find_element_by_id(PASSWORD_ID)
    passwd.send_keys(PASSWORD)
    loginButton = driver.find_element_by_id(LOGIN_BTN_ID)
    loginButton.click()
    time.sleep(10)