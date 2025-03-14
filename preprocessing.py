from PIL import Image
import os
import cv2
import matplotlib.pyplot as plt

dataset_dir = "dataset"

def remove_corrupted_images(folder):
    # 檢查並刪除損壞的圖片
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        try:
            with Image.open(filepath) as img:
                img.verify()  # 檢查圖片是否損壞
        except (IOError, SyntaxError):
            print(f"Removing corrupted image: {filepath}")
            os.remove(filepath)

def convert_to_jpg(folder):
    # 將所有圖片轉換為 JPEG 格式
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        try:
            with Image.open(filepath) as img:
                rgb_img = img.convert("RGB")  # 確保圖片為 RGB 模式
                new_filepath = os.path.splitext(filepath)[0] + ".jpg"
                rgb_img.save(new_filepath, "JPEG")
                if filepath != new_filepath:
                    os.remove(filepath)  # 刪除舊格式文件
        except Exception as e:
            print(f"Error converting {filepath}: {e}")

def resize_images(folder, size=(224, 224)):
    # 調整圖片大小
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        img = cv2.imread(filepath)
        if img is None:
            continue
        img_resized = cv2.resize(img, size)
        cv2.imwrite(filepath, img_resized)

# remove_corrupted_images
for category in os.listdir(dataset_dir):
    category_dir = os.path.join(dataset_dir, category)
    if os.path.isdir(category_dir):
        remove_corrupted_images(category_dir)

# convert_to_jpg
for category in os.listdir(dataset_dir):
    category_dir = os.path.join(dataset_dir, category)
    if os.path.isdir(category_dir):
        convert_to_jpg(category_dir)

# resize_images
for category in os.listdir(dataset_dir):
    category_dir = os.path.join(dataset_dir, category)
    if os.path.isdir(category_dir):
        resize_images(category_dir)
