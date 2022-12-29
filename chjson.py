# 1、导入包
import json
import os
from tqdm import tqdm
paths = "/home/xhh/Desktop/data_partA/data_annotated"


for json_name in tqdm(os.listdir(paths)):
    # 读打开文件
    path =  paths + '/' + json_name
    with open(path, encoding='utf-8') as f:
        # 读取文件
        result = json.load(f)
        result["imageData"] = None
        result["imagePath"] = "../img_data/" + json_name.split(".")[0] + ".png"
        print(json_name)

    with open(path, "w") as f:
        json.dump(result, f, ensure_ascii=False)
    print()


