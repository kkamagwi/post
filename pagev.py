# установите бибилиотеку selenium в терминале командой
# pip install selenium
from selenium import webdriver
import time

# в скобочках место в которое установлен chromedriver
driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")

driver.get('https://www.instagram.com/endgmpython/')
refrshrate = 10

while True:
    time.sleep(refrshrate)
    driver.refresh()

@endgmPythON