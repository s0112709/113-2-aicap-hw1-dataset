# import libraries
import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # 不開啟瀏覽器視窗
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(options=options)
    return driver

def fetch_image_urls(query, max_images=50):
    driver = setup_driver()
    search_url = f"https://www.google.com/search?tbm=isch&q={query}"
    driver.get(search_url)
    
    image_urls = set()
    for _ in range(5):  # 捲動頁面以加載更多圖片
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(2)
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    img_tags = soup.find_all("img")
    
    for img_tag in img_tags:
        img_url = img_tag.get("src") or img_tag.get("data-src")
        if img_url and img_url.startswith("http"):
            image_urls.add(img_url)
        if len(image_urls) >= max_images:
            break
    
    driver.quit()
    return list(image_urls)

def download_images(image_urls, folder):
    os.makedirs(folder, exist_ok=True)
    for i, url in enumerate(image_urls):
        try:
            img_data = requests.get(url, timeout=10).content
            with open(os.path.join(folder, f"{i+1}.jpg"), "wb") as f:
                f.write(img_data)
            print(f"Downloaded: {url}")
        except Exception as e:
            print(f"Failed to download {url}: {e}")

if __name__ == "__main__":
    # categories = {"motorcycle": "機車", "bicycle": "腳踏車"}
    categories = {"motorcycle": "motorcycle", "bicycle": "bicycle"}
    max_images = 200  # 每類別下載的圖片數量
    
    for category, keyword in categories.items():
        print(f"Fetching images for {keyword}...")
        urls = fetch_image_urls(keyword, max_images)
        download_images(urls, f"dataset/{category}")
    
    print("Image collection complete!")