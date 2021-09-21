def txt(text):  # 定义函数名
    file = open('result.txt', 'w')
    file.write(text)  # 写入内容信息
    file.close()
    print('ok')


def hack_add(path):
    with open(path, 'r') as f:
        data = f.read()
        for j in range(1, 26):
            news = ' '
            for i in data:
                # print(i)
                if i == " ":
                    news = news + i
                elif ord(i) + j > 90:
                    news = news + chr(ord(i) + j - 26)
                else:
                    news = news + chr(ord(i) + j)
            print(news)
            print("分割\n")


def hack_multi(path):
    with open(path, 'r') as f:
        data = f.read()
        for j in range(3, 26, 2):
            news = ' '
            print(j)
            for i in data:

                if i == " ":
                    news = news + i
                else:
                    news = news + chr(((ord(i) - 64) * j) % 26 + 65)
            print(news)
            print("分割\n")


def hack_fun(path):
    with open(path, 'r') as f:
        data = f.read()
        for j in range(3, 26, 2):
            for k in range(1, 26):
                news = ' '
                for i in data:
                    if i == " ":
                        news=news+i
                    else:
                        news = news + chr(((ord(i) - 64) * j + k) % 26 + 65)
                print(news)
"""   
        j=11
        k=1
        news = ' '
        for i in data:
            if i == " ":
                news = news + i
            elif i =='\n':
                news = news + i
            else:
                news = news + chr(((ord(i) - 64) * j + k) % 26 + 65)
        txt(news)
        j = 23
        k = 1
        news = ' '
        for i in data:
            if i == " ":
                news = news + i
            elif i == '\n':
                news = news + i
            else:
                news = news + chr(((ord(i) - 64) * j + k) % 26 + 65)
        txt(news)
       
"""