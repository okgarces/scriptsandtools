from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
email = raw_input('Correo:\n')
password = raw_input('Password Viejo:\n')
new_password = raw_input('Password Nuevo:\n')

for i in range(2):
	driver.get("")
	elem = driver.find_element_by_name("userfrm")
	elem.send_keys(email)
	elem = driver.find_element_by_name("password")
	elem.send_keys(password)
	elem = driver.find_element_by_name("password1")
	elem.send_keys(new_password)
	elem = driver.find_element_by_name("password2")
	elem.send_keys(new_password)
	elem.send_keys(Keys.RETURN)

	password_temp = password
	password = new_password
	new_password = password_temp

driver.close()
driver.quit()
