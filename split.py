import os
import random



def main():
    # 保证随机可复现
    random.seed(0)

    # 将数据集中10%的数据划分到验证集中
    split_rate = 0.2


    cla_path = "imgs"
    images = os.listdir(cla_path)
    num = len(images)
    # 随机采样验证集的索引
    eval_index = random.sample(images, k=int(num*split_rate))
    train_name = []
    val_name = []
    for index, image in enumerate(images):
        if image in eval_index:
            val_name.append(image.split(".")[0])
        else:
            # 将分配至训练集中的文件复制到相应目录
            train_name.append(image.split(".")[0])

    with open("train.txt", "w") as f:
        f.write("\n".join(train_name))
    with open("val.txt", "w") as f:
        f.write("\n".join(val_name))


if __name__ == '__main__':
    main()