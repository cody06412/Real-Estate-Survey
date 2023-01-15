from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas

website = 'https://www.fotocasa.es/es/comprar/todas-las-casas/barcelona-provincia/maresme/l'
path = 'C:\\Users\\user\\Downloads\\chromedriver.exe'

driver = webdriver.Chrome(path)
driver.get(website)
cookies = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/footer/div/button[2]')
cookies.click()
driver.maximize_window()
time.sleep(5)

preus = []
habs = []
immo = []

for i in range (2, 9):
	height = driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );")
	for e in range(0, height, 700):
		driver.execute_script('window.scrollTo(0, {});'.format(e))
		time.sleep(0.6)

	time.sleep(3)
	llista_preu = driver.find_elements(By.CLASS_NAME, 're-CardPrice')
	llista_hab = driver.find_elements(By.CLASS_NAME, 're-CardFeaturesWithIcons-wrapper')
	llista_immo = driver.find_elements(By.CLASS_NAME, 're-CardPromotionBanner-title-name')

	for p in llista_preu:
		preus.append(p.text)
	for h in llista_hab:
		habs.append(h.text)
	for immob in llista_immo:
		immo.append(immob.text)

	page = "https://www.fotocasa.es/es/comprar/todas-las-casas/barcelona-provincia/maresme/l/"+str(i)
	driver.get(page)
	time.sleep(6)


print(preus)

data_habs = pandas.DataFrame({'habs': habs})
data_habs.to_csv('habs.csv', index=False)

data_preus = pandas.DataFrame({'preus': preus})
data_preus.to_csv('preus.csv', index=False)

data_immo = pandas.DataFrame({'immo': immo})
data_immo.to_csv('immo.csv', index=False)
