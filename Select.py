from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(r"D:\_Selenium\chromedriver_win32\chromedriver.exe")
driver.get(r"C:\Users\ADMIN\Desktop\Demo-html\demo.html")
driver.maximize_window()
sleep(2)
list_box = driver.find_element_by_xpath("//select[@id='standard_cars']")
select = Select(list_box)

select.select_by_visible_text("Audi")
sleep(2)
select.select_by_index(4)
sleep(2)
select.select_by_value('nin')
sleep(2)

driver.quit()
