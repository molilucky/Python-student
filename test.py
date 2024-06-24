import os

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from tkinter import *

root = Tk()
Label(root, text="请在下方输入网站地址").grid(row=0)

v1 = StringVar()
v2 = StringVar()
e1 = Entry(root, textvariable=v1, width=50)
e1.grid(row=1, padx=5, pady=5)
e2 = Entry(root, textvariable=v2, width=10)
e2.grid(row=2, padx=5, pady=5, sticky=E)


def photo(e1=e1, v2=v2):
    # 目标网站URL
    url = e1.get()

    # 发送HTTP请求
    response = requests.get(url)
    response.raise_for_status()  # 检查请求是否成功

    # 使用BeautifulSoup解析HTML内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 创建photo文件夹，如果已存在，则尝试创建photo1, photo2, ...
    folder_name = 'photo'
    counter = 0
    while os.path.exists(folder_name):
        counter += 1
        folder_name = f'photo{counter}'

    os.makedirs(folder_name)

    # 找到所有图片标签
    img_tags = soup.find_all('img')

    # 下载并保存图片
    for img in img_tags:
        # 获取图片的URL
        img_url = img.get('src')
        if not img_url:
            continue
        # 将相对URL转换为绝对URL
        full_img_url = urljoin(url, img_url)
        # 获取图片内容
        try:
            img_response = requests.get(full_img_url)
            img_response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"无法下载图片：{full_img_url}，原因：{e}")
            v2.set("无法下载...")
            continue

        # 获取图片名字
        filename = os.path.join(folder_name, img_url.split('/')[-1])
        # 保存图片
        with open(filename, 'wb') as f:
            f.write(img_response.content)

    print(f"下载完成，图片保存在{folder_name}文件夹中！")
    v2.set("下载完成！")


Button(root, text="下载图片", command=photo).grid(row=2)

mainloop()
