from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from traceback import print_exc
from time import sleep

def driver_init(url, userId=None, password=None):
    try:
        ChromeDriverManager().install()
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        sleep(1)

        driver.find_element(By.XPATH, '//*[@id="cMain"]/div/div/div/a[2]').click()
        sleep(1)

        if userId is None:
            userId = input('아이디: ')
        if password is None:
            password = input('비밀번호: ')
        
        id = driver.find_element(By.XPATH, '//*[@id="loginId--1"]')
        id.send_keys(userId)
        # EC.element_to_be_clickable((By.XPATH, '//*[@id="loginId--1"]'))
        pw = driver.find_element(By.XPATH, '//*[@id="password--2"]')
        pw.send_keys(password)
        # EC.element_to_be_clickable((By.XPATH, '//*[@id="password--2"]'))
        pw.send_keys(Keys.RETURN)
        # EC.element_to_be_clickable((By.XPATH, '//*[@id="mainContent"]/div/div/form/div[4]/button[1]'))

        sleep(10)
        
        
    except:
        print_exc()
        return None



if __name__ == '__main__':
    baekjoon = None
    userId = None
    password = None

    try:
        driver = driver_init('https://www.tistory.com/auth/login')
    finally:
        if driver is not None:
            driver.quit()
            print('드라이버가 정상적으로 종료되었습니다.')