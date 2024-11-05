import utils
import time
import undetected_chromedriver as uc
import pickle

mainPage = "https://www.ozon.ru/"
targetPage = "https://www.ozon.ru/product/svitshot-adidas-originals-1689043556/"
targetTime = "00:02:10.850000"

driver = uc.Chrome(use_subprocess=True)
driver.get(mainPage)
cookies = pickle.load(open("cookies.pkl", "rb"))
utils.loadCookies(driver, cookies)
driver.get(targetPage)

utils.wait(targetTime)
driver.refresh()

time.sleep(1.75)
driver.addToCart(driver)

time.sleep(1)
utils.buy(driver)