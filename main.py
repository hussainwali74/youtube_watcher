from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

video_url="https://www.youtube.com/watch?v=N-xnaX8lX3Q"
video_duration='1:04'

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(executable_path="C:/Program Files (x86)/chromedriver.exe", options=options)
# driver = webdriver.Chrome(executable_path="C:/Program Files (x86)/chromedriver.exe")

try:
    while True:
            
        driver.get(  video_url)
        driver.maximize_window()
        
        video_title=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="title"]/h1/yt-formatted-string'))
        )
        print('video title: ', video_title.text)
        try:
            play_button = WebDriverWait(driver,10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,'[aria-label="Play"]'))
            )
            
            play_button.click()
            print('played')
        except Exception as ee:
            print('error in playing : ',ee)
            pass
        try:
            driver.execute_script('document.querySelector("[data-title-no-tooltip=\'Mute\']").click();')

            # mute_button=WebDriverWait(driver,10).until(
            #     EC.element_to_be_clickable((By.CSS_SELECTOR,'[data-title-no-tooltip="Mute"]'))
            # )
            # mute_button.click()
            print('muted')
        except Exception as ee:
            print('error in  muting: ',ee)
            pass
        try:
            auto_play=WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,'[data-tooltip-target-id="ytp-autonav-toggle-button"]'))
            )
            auto_play.click()
            print('autoplay')
        except Exception as ee:
            print('error autoplay: ',ee)
            pass
        #convert video duration to seconds
        minutes, seconds = map(int, video_duration.split(':'))
        total_seconds = minutes*60+seconds
        total_seconds+=random.randint(1,5)
        print('total_seconds: ',total_seconds)
        time.sleep(total_seconds)
except Exception as e:
    print('e',e)