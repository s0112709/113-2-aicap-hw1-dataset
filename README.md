# 113-2 人工智慧總整與實作 HW1

|        |                  |
| :----: | :--------------: |
|  **Name**  |     陳宥翔      |
|  **ID**   |      110611014       |
| **GitHub** | [s0112709](https://github.com/s0112709) |
| **Email**  |     s20232161@gmail.com     |

---

##  Dataset 介紹

- `dataset/`：包含所有經過挑選與處理後的資料。
- `imbalanced_datasets/`：內部為不平衡的 dataset，命名方式為 `dataset_{num_of_bicycle}_{num_of_motorcycle}`。
- `split_datasets/`：內部為隨機挑選後的 dataset，包含較少數據，命名方式為 `dataset_{原始dataset的百分比}`。

---

##  Code 介紹

- **`crawler.py`**
  - 透過關鍵字爬取並下載圖片。

- **`preprocessing.py`**
  - 在人工篩選與處理後，再次檢查並移除損壞的圖片。
  - 轉換格式為 JPEG，並重新調整圖片大小。

- **`reindex.py`**
  - 在指定資料夾內，將所有圖片重新命名。

- **`split_dataset.py`**
  - 依照指定條件分割 dataset，產生 `imbalanced_datasets/` 與 `split_datasets/`。

---

##  Dataset 準備過程

1. 使用 `crawler.py` 下載 `bicycle` 與 `motorcycle` 各 200 張圖片。
2. 手動篩選不符合條件的圖片（例如品牌 Logo 等）。
3. 若圖片內包含多台 `bicycle` 或 `motorcycle`，則進行分割。
4. 裁切圖片，使畫面內僅保留 `bicycle` 或 `motorcycle`，減少不必要的背景資訊。
5. 使用 `preprocessing.py` 進行圖片格式轉換與修正。
6. 利用 `reindex.py` 重新命名所有圖片。
7. 最終整理後獲得 129 張 `Bicycle` 與 143 張 `Motorcycle` 的 `dataset/`。
8. 根據實驗需求，使用 `split_dataset.py` 產生不同條件的 `imbalanced_datasets/` 與 `split_datasets/`。