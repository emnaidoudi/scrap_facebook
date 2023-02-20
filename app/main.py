from fastapi import FastAPI
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
import re

app = FastAPI()

chrome_options = Options()
chrome_options.add_argument('--lang=en-US')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('----disable-dev-shm-usage')
driver_service = Service(executable_path = 'chromedriver')
driver = webdriver.Chrome(service=driver_service, options=chrome_options)
driver.get('https://www.facebook.com/pythonprogramming.net')
sleep(5) 


def class_name_format(class_name):
    return re.sub(' +', ' ', class_name).replace(" ", ".") 
def scrap_info(class_name, index = 0):
    try:
        class_name_formatted = class_name_format(class_name)
        class_name_element = driver.find_elements(By.CLASS_NAME, class_name_formatted)[index]
        info = class_name_element.text
    except:
        return "A PROBLEM OCCURED"
    return info  

@app.get("/facebook")
async def scrap_fb_python_page(page_name = "pythonprogramming.net/about_profile_transparency"):    
    data = dict()   
    try:
        data["page_name"] = scrap_info('x78zum5 xdt5ytf x1wsgfga x9otpla')
        text_likes = scrap_info('x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xi81zsa x1s688f')
        data["nb_likes"] = text_likes.split(" ")[0]
        text_follower = scrap_info('x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xi81zsa x1s688f', 1)
        data["nb_follower"] = text_follower.split(" ")[0]
        text_page_type = scrap_info('x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x6prxxf xvq8zen xo1l8bm xzsf02u', 2)
        try:
            data["page_type"] = text_page_type.split("·")[1].strip()
        except:
            data["page_type"] = "Interest"    
        data["contact"]= scrap_info('x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xzsf02u x1yc453h', 1)
        data["website"]= scrap_info('x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm x1qq9wsj x1yc453h')
        data["description"]= scrap_info('x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x6prxxf xvq8zen xo1l8bm xzsf02u',1)
        driver.get(f"https://www.facebook.com/{page_name}")
        sleep(3)
        i = 0
        while i<3:
            try:
                data["creation_date"] = scrap_info('x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xzsf02u',i)
                date_format = '%B %d, %Y'
                data["creation_date"] = datetime.strptime(data["creation_date"], date_format)
            except:
                i+=1
            else:
                break
        driver.get('https://www.facebook.com/pythonprogramming.net') 
    except Exception as e:
        print(e)
        return data  
    return data
