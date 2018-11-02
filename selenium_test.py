from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def test_home():
    options = Options()
    options.add_argument("--no-sandbox")# Bypass OS security model
    options.add_argument("--headless")# Runs Chrome in headless mode.
    driver = webdriver.Chrome(chrome_options=options, executable_path='C:\git\web-app-ci-cd-with-travis-ci-pshn111\chromedriver.exe')
    driver.get("http://162.246.157.125:8000/")

    assert driver.find_element_by_id("name") != None
    assert driver.find_element_by_id("about") != None
    assert driver.find_element_by_id("education") != None
    assert driver.find_element_by_id("skills") != None
    assert driver.find_element_by_id("work") != None
    assert driver.find_element_by_id("contact") != None     

test_home()



