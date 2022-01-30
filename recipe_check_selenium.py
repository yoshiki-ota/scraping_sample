import time
# noinspection PyUnresolvedReferences
import chromedriver_binary  # コード中には使用しないけど表示＝グレー表示だけど自分で抑止した場合は色がつく
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://cookpad.com/"


def chromedriver_options():
    # オプション設定  確認できたらブラウザを表示しないでやれる
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # ヘッドレスモード
    # options.add_argument("--blink-settings=imagesEnabled=false")  # 画像無効
    # options.add_argument("--enable-javascript")  # JS無効
    return options


def search_by_food(driver, food):
    driver.get(f"{URL}")
    driver.implicitly_wait(10)

    driver.find_element(By.ID, "keyword").send_keys(food)  # 検索にfoodの内容を入力
    driver.find_element(By.ID, "submit_button").click()  # 検索ボタンを押す
    # time.sleep(1)


def get_recipes(driver):
    recipe_previews = driver.find_elements(By.CLASS_NAME, "recipe-preview")

    recipes = []
    for recipe_preview in recipe_previews:
        recipe_title = recipe_preview.find_element(By.CLASS_NAME, "recipe-title").text
        recipe_url = recipe_preview.find_element(By.CLASS_NAME, "recipe-title").get_attribute('href')
        recipes.append({
            "title": recipe_title,
            "url": recipe_url})
    return recipes


def main():
    food = "ピーマン"
    # 前の方法
    # driver = webdriver.Chrome()
    # driver.get("")
    # driver.implicitly_wait(10)
    # driver.close()

    # withの方法(close忘れ防止）
    with webdriver.Chrome(options=chromedriver_options()) as driver:
        search_by_food(driver, food)
        recipes = get_recipes(driver)

        for recipe in recipes:
            print(f"レシピ名 {recipe['title']}, URL:{recipe['url']}")


if __name__ == '__main__':
    main()
