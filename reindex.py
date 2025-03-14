import os

target_dir = "dataset/bicycle"

index = 1

for filename in os.listdir(target_dir):
    os.rename(os.path.join(target_dir, filename), os.path.join(target_dir, f"temp_{index}.jpg"))
    index += 1

index = 1

for filename in os.listdir(target_dir):
    os.rename(os.path.join(target_dir, filename), os.path.join(target_dir, f"{index}.jpg"))
    index += 1