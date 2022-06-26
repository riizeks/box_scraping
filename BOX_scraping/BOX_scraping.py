from selenium import webdriver
import time
import io
from urllib import request
from PIL import Image
from selenium.webdriver.chrome.options import Options
 
options = Options()
options.add_argument('--headless')

driver = webdriver.Chrome('path',chrome_options=options) #chromedriverのパスを指定
URL = "url" #boxのurl
driver.get(URL)
time.sleep(1) #以降のsleepは各自の回線状況に合わせて変更
search_bar = driver.find_element_by_name('password')
search_bar.send_keys("パスワード") #パスワード
time.sleep(1)
search_bar.submit() #ここでパスワードを確定
time.sleep(1) 
driver.get(URL) #名前順に並び替え
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[1]/div[5]/span/div/main/div/div/div[2]/div/div[1]/div[1]/div/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div/span/a").click()
time.sleep(3) #画像読み込みは時間かかるため
img = driver.find_element_by_xpath("/html/body/div[1]/div[5]/span/div/span/div/main/div/div/div/div/div/div[2]/div/div[1]/img")
imgurl = img.get_attribute('src')
f = io.BytesIO(request.urlopen(imgurl).read())
img = Image.open(f)
picname = "1"
pic = "path" + picname +".png" #"path"には保存ディレクトリを記入。ex)C:\\Hozon
img.save(pic) 
next = driver.find_element_by_xpath("/html/body/div[1]/div[5]/span/div/span/div/main/div/div/div/button")
next.click()
time.sleep(3)
num = 2
while num < 70:
    img = driver.find_element_by_xpath("/html/body/div[1]/div[5]/span/div/span/div/main/div/div/div/div/div/div[2]/div/div[1]/img")
    imgurl = img.get_attribute('src')
    f = io.BytesIO(request.urlopen(imgurl).read())
    img = Image.open(f)
    
    picname = str(num)
    pic = "path" + picname +".png" #"path"には保存ディレクトリを記入。ex)C:\\Hozon
    img.save(pic) 
    next = driver.find_element_by_xpath("/html/body/div[1]/div[5]/span/div/span/div/main/div/div/div/button[2]")
    next.click()
    time.sleep(3)
    num = num + 1
    
#sleepで処理を待機しないと要素が読み込まれないため注意    
 