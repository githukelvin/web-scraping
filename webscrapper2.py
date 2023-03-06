from selenium import webdriver
from selenium.webdriver.common.by  import By
from selenium.webdriver.chrome.service import Service as ChromeService
url = "https://jiji.co.ke/computers-and-laptops"

driver = webdriver.Chrome(service=ChromeService(chromeDriverManager().insall()))
driver = webdriver.Chrome(url)
driver.find_element('By.Xpath=//*[@id="js-advert-listing-wrapper"]/div/div')
