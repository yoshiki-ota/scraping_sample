import time
# noinspection PyUnresolvedReferences
import chromedriver_binary  # コード中には使用しないけど表示＝グレー表示だけど自分で抑止した場合は色がつく
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def main():
    food = "ピーマン"
    # 　ドライバーの立ち上げ
    driver = webdriver.Chrome()
    #  Googleにアクセス
    driver.get('https://google.com/')

    driver.find_element(By.NAME, "q").send_keys(food)  # (ID要素,"input")
    driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)

    time.sleep(1)  # １秒待つ
    driver.close()


if __name__ == '__main__':
    main()
