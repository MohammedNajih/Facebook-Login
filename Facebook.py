from seledroid import webdriver
from seledroid.webdriver.common.by import By
from seledroid.webdriver.common.keys import Keys
username = input('USERNAME : ')
password = input('PASSWORD : ')
driver = webdriver.Chrome()
driver.clear_cookies
driver.wait(3)
driver.get("https://m.facebook.com/login/?ref=dbl&fl&login_from_aymh=1&refid=9")
driver.wait(2)
user = driver.find_element(By.ID,"m_login_email").send_text(username)
pas = driver.find_element(By.ID,"m_login_password").send_text(password)
driver.find_element(By.XPATH, '//button[@name="login"]').click()
driver.wait(3)
driver.get("https://mobile.facebook.com/?paipv=0&eav=Afa_4y2fbINYotbph0M3PcfTy68dYbJMeUhS1c_8uyqt4EWRdN5yW3-GBBP23me7OJA&_rdc=1&_rdr&tbua=1")
driver.wait(1)
cookie =driver.get_cookies()
print(cookie)
driver.clear_cookies



