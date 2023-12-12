import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#Allgemeine Einstellungen
url="https://www.soscisurvey.de/Datenkompetenz/" #Zielurl wird für Selenium verwendet

#Selenium Einstellungen
driver = webdriver.Firefox() #webdriver kann upgedated werden mit - "brew install geckodriver" - muss instaliert sein - Brew geht nur bei installiertem homebrew
driver.get(url) #Selenium driver bekommt zielurl zum aufruf

#Funktionen
#1. Seite - Anmeldung
def anmeldung():

    try:
        WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#A001_01"))).click()
        print("Accepted Terms")
    except:
        print("Could not accept Terms")
    pass
    try:
        WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#submit0"))).click()
        print("Finished Page 1")
    except:
        print("Could not finish page 1")
    pass


#2. Seite
    try:
        WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#B001_01a"))).click()
        print("Choosed wisley")
    except:
        print("Choose didn't worked")
    pass
    try:
        WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#submit0"))).click()
        print("Finished Page 2")
    except:
        print("Could not finish page 2")
    pass
#3. Seite
    #1.
    try:
        WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#B002_015"))).click()
        print("First Choice")
    except:
        print("Choose didn't worked")
    pass
    #2
    try:
        WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#B002_021"))).click()
        print("Second Choice")
    except:
        print("Choose didn't worked")
    pass
    # 3.
    try:
        WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#B002_041"))).click()
        print("Third Choice")
    except:
        print("Choose didn't worked")
    pass
    # 4.
    try:
        WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#B002_031"))).click()
        print("Fourth Choice")
    except:
        print("Choose didn't worked")
    pass
    # 5.
    try:
        WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#B002_055"))).click()
        print("Fifth Choice")
    except:
        print("Choose didn't worked")
    pass
    # 6.
    try:
        WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#B002_061"))).click()
        print("Sixth Choice")
    except:
        print("Choose didn't worked")
    pass
    # 7.
    try:
        WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#B002_075"))).click()
        print("Seventh Choice")
    except:
        print("Choose didn't worked")
    pass
    # 8.
    try:
        WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#B002_085"))).click()
        print("Eighth Choice")
    except:
        print("Choose didn't worked")
    pass
    # 9.
    try:
        WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#B002_091"))).click()
        print("Ninth Choice")
    except:
        print("Choose didn't worked")
    pass
#Finish Page 3
    try:
        WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#submit0"))).click()
        print("Finished Page 2")
    except:
        print("Could not finish page 3")
    pass

# Ausführung der Funktionen evtl. Loop
anmeldung()
print("Done")



#Old mydealz scraper
"""
#erste Seite
def Cookie_klick():
    try:
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-t='continueWithoutAcceptingBtn']"))).click()
    except:
        print("Could not click Cookies")
        pass
    time.sleep(5)

#2. Einloggen
def login():
    try:
        # driver.find_elements_by_xpath('.//span[@class = "gbts"]')
        # driver.find_element_by_id("loginModalForm-identity").send_keys('akw.ingress@gmail.com')

        # WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[@class='space--ml-2' and @type='button']"))).click()
        # driver.find_element_by_css_selector('button--toW5-square.space--ml-2.button.button--shape-circle.button--type-primary.button--mode-white').click()
        WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'button--toW5-square space--ml-2 button button--shape-circle button--type-primary button--mode-white')]"))).click()
    except:
        print("Could not find Form")
        pass
    time.sleep(5)
    # Email
    try:
        driver.find_element(By.NAME, "identity").send_keys("akw.ingress@gmail.com")
        # username = driver.find_element_by_id("loginModalForm-identity")
        #
        # username.send_keys("akw.ingress@gmail.com")
        # drivers.find_elements_by_xpath("//button[@class='button--toW5-square.space--ml-2.button.button--shape-circle.button--type-primary.button--mode-white' and @type='button']")
        # driver.find_element_by_css_selector('button--toW5-square.space--ml-2.button.button--shape-circle.button--type-primary.button--mode-white').click()
        # WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div[1]/header/div/div/div[3]/button[2]"))).click()
    except:
        print("Could not Enter Email")
        pass
    time.sleep(5)
    # Passwort
    try:
        driver.find_element(By.NAME, "password").send_keys("4589*Hokusoto")
    except:
        print("Could not Enter Password")
        pass
    time.sleep(5)
    # Login Button
    try:
        driver.find_element(By.NAME, "form_submit").click()
    except:
        print("Could not Login")
        pass


#3. KWK Seite BS4
def open_kwk():
    page = requests.get(url, headers=header, timeout=20)
    if page.status_code == 200:
        try:
            soup = BeautifulSoup(page.content, 'html.parser')

            posts = soup.find_all("article", class_='thread--deal', limit=5)  # 5 article, written together
            n = 0
            for post in posts:  # read the articles as several products and print it (open array)
                # print(product, end='\n\n\n' * 2)
                title = functions.get_title(product)  # get's the Title of the Product description
                mydealz_url = functions.get_url(product)
                #commentbox = soup.find('section', attrs={'id':'thread-comments'})
                print(post.prettify())
                scraped_data.append({
                    'title': title,
                    # 'price': price,
                    'mydealz_url': mydealz_url
                })
        except:
            print("BS4 Scrapping Fehler")
        pass

def start_scrape(url):
    ## Send Request
    page = requests.get(url, headers=header, timeout=20)

    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser') #the hole page
        products = soup.find_all("article", class_='thread--deal', limit=5) #5 article, written together
        n=0
        print(soup.prettify())
        for product in products: #read the articles as several products and print it (open array)
            #print(product, end='\n\n\n' * 2)
            title = functions.get_title(product) # get's the Title of the Product description
            mydealz_url = functions.get_url(product) # wenn du das hast kannst du letzt endlich neu Scrappem
            scraped_data.append({
                'title': title,
                #'price': price,
                'mydealz_url': mydealz_url
            })




def chat_with_profile(profile: str):

    url_profile = f'https://www.mydealz.de/profile/{profile}'


assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source"""





