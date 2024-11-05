import time
import pickle
from datetime import datetime
from selenium.common import exceptions


def saveCookies(driver):
	while True:
		inp = input()
		if inp == 'go':
			pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
			print('cookies have been saved')
			break


def loadCookies(driver, cookies):
	for cookie in cookies:
		try:
			driver.add_cookie(cookie)
		except exceptions.InvalidCookieDomainException:
			print()
	print("cookies have been loaded")


def wait(target):
	while True:
		if datetime.now().strftime("%f")[:-5] == "0":
			break

	while True:
		current = datetime.now().strftime("%H:%M:%S.%f")
		print(current)
		if current >= target:
			break
		time.sleep(1)
	print("YAY!! ITS " + target)


def addToCart(driver):
	classesAddToCart = "'b2117-a0 b2117-b6 b2117-b2 b2117-a4'"
	driver.execute_script(f"document.getElementsByClassName({classesAddToCart})[0].click()")


def buy(driver):
	classesBuy = "'b2117-a0 b2117-b5 b2117-b2 b2117-a4'"
	driver.execute_script(f"document.getElementsByClassName({classesBuy})[0].click()")