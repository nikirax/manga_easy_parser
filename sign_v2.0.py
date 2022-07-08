from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import username, password 
import random
import time

def mangalib(username , pas):
    try:
        browser = webdriver.Chrome("C:\\Users\\User\\Desktop\\project_instagrammbot\\chromedriver\\chromedriver.exe")

        browser.get('https://mangalib.me/')
        time.sleep(random.randrange(3))
        #login
        browser.find_element('id', "show-login-button").click()

        user_input = browser.find_element("name",'email')
        user_input.clear()
        user_input.send_keys(username)

        password_input = browser.find_element("name", "password")
        password_input.clear()
        password_input.send_keys(pas)

        password_input.send_keys(Keys.ENTER)
        time.sleep(random.randrange(10))

        try: 
            browser.get(f"https://mangalib.me/manga-list")
            d = {}
            for num in range(1, 7):
                item = browser.find_element('xpath', f"/html/body/div[3]/div/div/div[2]/div[1]/div[1]/div/div[7]/div[2]/label[{num}]/span[2]").text
                d[item] = num
            #sorry about this crutch. I'll think about how to remove it
            flag = False
            while(True):
                print(d , "Сhoose the you like, and to stop, type stop")
                input_type = input()
                if input_type == 'stop' or input_type == 'Stop':
                    break
                else:
                    type_num = d.get(input_type, 0)

                    browser.find_element('xpath', f'/html/body/div[3]/div/div/div[2]/div[1]/div[1]/div/div[7]/div[2]/label[{type_num}]/span[2]').click()
                    time.sleep(random.randrange(3))
                    flag = True
            Top_10_print(browser, flag)
        except Exception as ex:
            print(ex)
            close_browser(browser)
        close_browser(browser)
    except Exception as ex: 
        print(ex)
        close_browser(browser)
def close_browser(browser):
    browser.close()
    browser.quit()
def Top_10_print(browser, flag):
    browser.find_element('xpath', f'/html/body/div[3]/div/div/div[2]/div[1]/div[2]/button[2]').click()
    time.sleep(random.randrange(3))
    if flag == True:
        print('Top 10 in choose category:')
        for num in range(10, 0, -1):
            href = browser.find_element('xpath', f'/html/body/div[3]/div/div/div[1]/div[2]/div/div/div[{num}]/a')
            print(f"{num} point - {browser.find_element('xpath', f'/html/body/div[3]/div/div/div[1]/div[2]/div/div/div[{num}]/a/div/h3').text} href-{href.get_attribute('href')}")
        print('I hope I was helpful host. Bye!!')

if __name__ == '__main__':
    mangalib(username, password)