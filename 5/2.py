import time

from selenium import webdriver

driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&prevRID=GCXG99K18WW6NH4MT5XT&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")


time.sleep(3)
login = driver.find_element_by_id("ap_customer_name")
password = driver.find_element_by_id("ap_password")
email = driver.find_element_by_id("ap_email")
button = driver.find_element_by_id("continue")

login.send_keys("BoB")
time.sleep(1)
password.send_keys("Пароль")
time.sleep(1)
email.send_keys("passwf@gmail.com")

