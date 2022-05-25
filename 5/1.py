from selenium import webdriver


driver =webdriver.Firefox(executable_path="geckodriver.exe")
url = "https://www.amazon.com/"
driver.get(url)
driver.maximize_window()
url1 =''' //*[@id="twotabsearchtextbox"] '''

search = driver.find_element_by_xpath(url1)
search.send_keys("rtx")
search.submit()
