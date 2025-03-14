import os
import shutil
import random

def split_dataset_ratio(source_dir, output_base_dir, split_ratios):
    # 分割不同比例的dataset
    categories = ['Bicycle', 'Motorcycle']
    
    for ratio in split_ratios:
        output_dir = os.path.join(output_base_dir, f"dataset_{ratio}")
        os.makedirs(output_dir, exist_ok=True)
        
        for category in categories:
            source_category_dir = os.path.join(source_dir, category)
            output_category_dir = os.path.join(output_dir, category)
            os.makedirs(output_category_dir, exist_ok=True)
            
            files = os.listdir(source_category_dir)
            random.shuffle(files)
            num_files = int(len(files) * (ratio / 100))
            selected_files = files[:num_files]
            
            for file in selected_files:
                src_path = os.path.join(source_category_dir, file)
                dst_path = os.path.join(output_category_dir, file)
                shutil.copy(src_path, dst_path)
            
        print(f"folder {output_dir} created with data of num files {len(selected_files)}")

def split_dataset_num(source_dir, output_base_dir, split_num):
    # 分割不同數量的dataset，且總數為 100
    categories = ['Bicycle', 'Motorcycle']
    
    for bicycle_num in split_num:
        motorcycle_num = 100 - bicycle_num
        output_dir = os.path.join(output_base_dir, f"dataset_{bicycle_num}_{motorcycle_num}")
        os.makedirs(output_dir, exist_ok=True)

        for category in categories:
            source_category_dir = os.path.join(source_dir, category)
            output_category_dir = os.path.join(output_dir, category)
            os.makedirs(output_category_dir, exist_ok=True)

            files = os.listdir(source_category_dir)
            random.shuffle(files)
            selected_files = files[:bicycle_num] if category == 'Bicycle' else files[:motorcycle_num]

            for file in selected_files:
                src_path = os.path.join(source_category_dir, file)
                dst_path = os.path.join(output_category_dir, file)
                shutil.copy(src_path, dst_path)

        # print(f"folder {output_dir} created with data of num files {len(selected_files)}")

if __name__ == "__main__":
    source_dataset_dir = "dataset"  # 原始資料夾名稱
    output_directory = "unbalanced_datasets"  # 存放輸出的資料夾
    # split_percentages = [20, 40, 60, 80]  # 設定不同的比例
    split_num = [20, 50, 80] # 不同 dataset 中，bicycle的數量，且總數為 100
    
    # split_dataset_ratio(source_dataset_dir, output_directory, split_percentages)
    split_dataset_num(source_dataset_dir, output_directory, split_num)
    print("Dataset splitting completed!")