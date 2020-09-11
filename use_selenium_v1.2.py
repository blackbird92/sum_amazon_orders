import time
import pdb
from selenium import webdriver

sum_orderprice = 0
start_index = 1

driver = webdriver.Chrome(executable_path='****.exe')
driver.get('https://www.amazon.co.jp/gp/css/order-history?ref_=nav_orders_first&orderFilter=year-2020&startIndex=' + str(start_index))

account_field = driver.find_element_by_id("ap_email")
account_field.send_keys("******@mail.com")
go_next = driver.find_element_by_id("continue")
go_next.click()

time.sleep(1)

password_field = driver.find_element_by_id("ap_password")
password_field.send_keys(input(">>"))
exe_login = driver.find_element_by_id("signInSubmit")
exe_login.click()

page_count = int(driver.find_element_by_class_name("num-orders").text.replace("件",""))
page_count = int(page_count / 10 + 1)

for cnt in range(page_count):
	for o in driver.find_elements_by_class_name("order"):
		sum_orderprice += int((o.find_elements_by_class_name("value")[1].text).strip("￥").replace(",",""))
	
	start_index += 10
	driver.get('https://www.amazon.co.jp/gp/css/order-history?ref_=nav_orders_first&orderFilter=year-2020&startIndex=' + str(start_index))
print(sum_orderprice)
driver.quit()