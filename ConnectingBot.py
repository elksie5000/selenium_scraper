#imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
"""Download ChromeDriver
Now we need to download latest stable release of ChromeDriver from:
"""

#https://chromedriver.chromium.org/
## Log In to Your Instagram Account
#specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Chrome()

#open the webpage
driver.get("http://www.instagram.com")

#target username
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

#enter username and password
username.clear()
username.send_keys("my_username")
password.clear()
password.send_keys(username.send_keys("davidelks3"))
password.send_keys("6CdwtCquQVr6TzHUHeZc")

#target the login button and click it
button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

#We are logged in!
#Handle Alerts
#ou might only get a single alert, or you might get 2 of them


#please adjust the cell below accordingly
time.sleep(5)
alert = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
#alert2 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
#Search for a certain hashtag
#target the search input field
searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchbox.clear()

#search for the hashtag cat
keyword = "#cat"
searchbox.send_keys(keyword)
 
#FIXING THE DOUBLE ENTER
time.sleep(5) # Wait for 5 seconds
my_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/" + keyword[1:] + "/')]")))
my_link.click()
"""
"Scroll Down
"Increase n_scrolls to select more photos (depending on screen resolution)
"Example:
"2 scrolls cover approx. 35 photos
"3 scrolls cover approx. 45 photos
#scroll down 2 times
"""
#increase the range to sroll more
n_scrolls = 2
for j in range(0, n_scrolls):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
#target all the link elements on the page
anchors = driver.find_elements_by_tag_name('a')
anchors = [a.get_attribute('href') for a in anchors]
#narrow down all links to image links only
anchors = [a for a in anchors if str(a).startswith("https://www.instagram.com/p/")]

print('Found ' + str(len(anchors)) + ' links to images')
anchors[:5]
#Found 45 links to images
"""['https://www.instagram.com/p/CLS2iQYMMQl/',
 'https://www.instagram.com/p/CLTZ6wssjRb/',
 'https://www.instagram.com/p/CLTF0NID96i/',
 'https://www.instagram.com/p/CLTGXXipfmn/',
 'https://www.instagram.com/p/CLTR-boJOYx/']"""
images = []

#follow each image link and extract only image at index=1
for a in anchors:
    driver.get(a)
    time.sleep(5)
    img = driver.find_elements_by_tag_name('img')
    img = [i.get_attribute('src') for i in img]
    images.append(img[1])
    
#Save images to computer
#First we'll create a new folder for our images somewhere on our computer.


#Then, we'll save all the images there.
import os

path = os.getcwd()
path = os.path.join(path, keyword[1:] + "s")

#create the directory
os.mkdir(path)

#path
'C:\\Users\\goaim\\cats'
#download images
counter = 0
for image in images:
    save_as = os.path.join(path, keyword[1:] + str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1
