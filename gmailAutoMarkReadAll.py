#---------------------------
#      15/11/2017
# created by Wojciech Kuczer 
#---------------------------


from selenium import webdriver
import time


driver = webdriver.Chrome('YOUR PATH TO/chromedriver')
driver.get("https://mail.google.com/mail/?tab=wm&amp;authuser=0")
#finds username field
username = driver.find_element_by_name('identifier')
username.send_keys("USERNAME")
#finds password field
driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
time.sleep(4)
password = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
password.send_keys('PASSWORD')
driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
time.sleep(4)
#grabs text label of inbox messages for finishing while loop
content = driver.find_element_by_xpath('//*[@id=":hl"]/div/div[2]/span/a').text
while content != "CONTENT OF INBOX LABEL":
    #finds and clicks MORE button
    driver.find_element_by_xpath('//*[@id=":33"]').click()
    time.sleep(2)
    #finds and clicks MARK ALL AS READ
    driver.find_element_by_xpath('//*[@id=":jc"]/div').click()
    time.sleep(2)
    #finds and clicks next page button
    driver.find_element_by_xpath('//*[@id=":ha"]').click()
    #updates label text for breaking out of loop
    content = driver.find_element_by_xpath('//*[@id=":hl"]/div/div[2]/span/a').text
print('MISSION COMPLITE')


# PLEASE BE AWARE THAT XPATH FOR YOUR GMAIL ACCOUNT WILL DIFFER.
# JUST INSPECT ELEMENT IN CHROME BROWSER AND CHANGE IT IN SCRIPT