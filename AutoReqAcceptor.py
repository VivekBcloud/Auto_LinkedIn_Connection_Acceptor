import os
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


links = [
    "https://www.linkedin.com/feed/update/urn:li:activity:6785441555596492800/",
    "https://www.linkedin.com/feed/update/urn:li:activity:6794077580908744704/"
]


options = webdriver.ChromeOptions()
options.add_argument("user-data-dir={}\driver_data".format(os.getcwd()))

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver.get("https://linkedin.com")
# sleep(5)
# delete this after every month

try:
    # auto login in case the user is not logged in
    userid = '' # fill the userid
    password = '' # fill the password 
    checklink = driver.find_element_by_class_name("sign-in-form__form-input-container")
    driver.find_element_by_xpath('//*[@id="session_key"]').send_keys(userid)
    driver.find_element_by_xpath('//*[@id="session_password"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="main-content"]/section[1]/div[2]/form/button').click()
    sleep(2)
    
except:
    print("CAN'T SIGNIN")



# for link in links:
#     try:
#         print("accessing link ", link)
#         driver.get(link)
#         sleep(2)
#         el = driver.find_element_by_class_name("react-button__trigger")
#         if "false" == el.get_attribute("aria-pressed"):
#             print("liking")
#             el.click()
#             print("liked")
#             sleep(1)
#         else:
#             print("already processed link ", link)
#     except Exception as e:
#         print("error processing link\nlink: ", link, "\nerror",  e)


# for accepting the connection requests
try:
    driver.get("https://www.linkedin.com/mynetwork/")
    sleep(2)
    invite = driver.find_element_by_class_name("mn-invitation-list")
    while invite:
        invite.find_element_by_class_name("artdeco-button--secondary").click()
        sleep(2)
        invite = driver.find_element_by_class_name("mn-invitation-list")
        
except Exception as e:
    print("Error-",e)


driver.close()


