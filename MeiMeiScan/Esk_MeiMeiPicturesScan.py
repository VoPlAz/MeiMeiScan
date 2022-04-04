# -*- coding: UTF-8 -*-
import requests
import random
import sys

Path_y = sys.path[0]
Path=Path_y+'\\'
mode = 'MeiMei'
pictures_n = 0
Meimei_url_list = ['https://www.dmoe.cc/random.php',
                   'https://api.ixiaowai.cn/api/api.php', 'http://api.btstu.cn/sjbz/api.php?lx=dongman&format=images']
FengJing_url_list = ['https://api.dujin.org/pic/fengjing', 'http://api.btstu.cn/sjbz/api.php?lx=fengjing&format=images']

User_url_list = []


def header():
    print('---------------------------------MeiMeiScan---------------------------------')
    print('[+]There are many built-in API addresses, which can be customized and added')
    print('[+]Support user-defined crawling quantity')
    print('[+]Let you have more wallpaper materials')
    print('----------------------------------------------------------------------------')
    print('[+]有许多内置的API地址，可以自定义添加')
    print('[+]支持自定义爬取数量')
    print('[+]让你有更多的壁纸素材')
    print('-------------------------------------------------------------Version [1.0.0]')
    print("Type 'help' for usage")


def help():
    print("number [quantity]")  # 设置爬取数量
    print("type [mode]")  # 设置类型
    print("add [address]")  # 添加地址
    print('path [save path]')  # 保存地址
    print("options")  # 查看设置
    print("start")  # 开始
    print('--------------------')
    print('''Mode:(1)MeiMei(2)Scenery(3)Custom''')


header()
count = 0
count_2=1
User_url_count = 0


def options(mode, numberofpic, path):
    print('Number Of Pictures:' + str(numberofpic))
    print('Mode:' + mode)
    print('Path:' + path)


while True:
    User_c = input(">>>")
    if User_c.lower() == 'help':
        help()
    elif User_c[0:6].lower() == 'number' and User_c[6] == ' ':
        pictures_n = int(User_c[7:])
        print('Number Of Pictures -----> ' + User_c[7:])
    elif User_c[0:4].lower() == 'type' and User_c[4] == ' ':
        if User_c[5:] == '1':
            mode = 'MeiMei'
            print('Mode -----> ' + mode)
        elif User_c[5:] == '2':
            mode = 'Scenery'
            print('Mode -----> ' + mode)
        elif User_c[5:] == '3':
            mode = 'Custom'
            print('Mode -----> ' + mode)
        else:
            print("No '" + User_c[5:] + "' type")
    elif User_c[0:3].lower() == 'add' and User_c[3] == ' ':
        User_url_list.append(User_c[4:])
        print('Add ' + User_c[4:])
    elif User_c[0:4].lower() == 'path' and User_c[4] == ' ':
        if User_c[-1]=='\\':
            Path = User_c[5:]
            print('Path -----> '+Path)
        if User_c[-1]!='\\':
            Path =User_c[5:]+'\\'
            print('Path -----> ' + Path)
    elif User_c[0:7].lower() == 'options':
        options(mode=mode, numberofpic=pictures_n, path=Path)
    elif User_c[0:5].lower() == 'start':
        if mode == 'MeiMei':
            while True:
                if count == pictures_n:
                    break
                print('下载第' + str(count_2) + '张至' + Path)
                img = requests.get(Meimei_url_list[random.randint(0, 2)])
                with open(Path + str(count_2) + '.jpg', 'wb') as f:
                    f.write(img.content)
                    f.close()
                count_2 += 1
                count+=1
        if mode == 'Scenery':
            while True:
                if count == pictures_n:
                    break
                print('下载第' + str(count_2) + '张至' + Path)
                img = requests.get(FengJing_url_list[random.randint(0, 1)])
                with open(Path + str(count_2) + '.jpg', 'wb') as f:
                    f.write(img.content)
                    f.close()
                count_2 += 1
                count+=1
        if mode == 'Custom':
            while True:
                for a in User_url_list:
                    User_url_count += 1
                if count == pictures_n:
                    break
                print('下载第' + str(count_2) + '张至' + Path)
                img = requests.get(User_url_list[random.randint(0, User_url_count)])
                with open(Path + str(count_2) + '.jpg', 'wb') as f:
                    f.write(img.content)
                    f.close()
                count_2 += 1
                count+=1
        count = 0
        count_2=1
    else:
        print("No command for " + User_c)
