# 建立以requests库为基础的爬虫，爬去京东商品评论
from helpers import *
import requests
import re
import time
from bs4 import BeautifulSoup

def getHTMLText(url):                                       # 从url中提取字符串形式的内容并返回
    try:
        kv = {"user-agent": "Mozilla/5.0"}                  # 设置爬取时的相关参数, 使用user-agent模拟浏览器访问服务器
        r = requests.get(url, headers=kv, timeout=30)       # 获得url内容
        r.raise_for_status()                                # 如果获取失败，产生异常，跳转到except
        r.encoding = r. apparent_encoding                   # 解析页面内容
        return r.text
    except:
        print("获取HTML失败！！！！")

def processText(text):                                              # 处理从url中提取的文本，返回评论以及评分
    new_text = re.findall(r"\"comments\":.*}]", text)[0]            # 选取comment部分数据
    new_text = re.sub(r"\"hAfterUserComment\":{.*?}", "", new_text) # 去掉"hAfterUserComment"部分，防止获取的评论数超过评分数
    comment = re.findall(r"\"content\":\".*?\"", new_text)          # 获取评论列表，如['"content":"机器暂时没啥问题，物流很快。"',....]
    score = re.findall(r"\"score\":.*?\d",new_text)                 # 获取评分列表，如['"score":1', '"score":1', '"score":0', '"score":1', '"score":0', '"score":1', '"score":0',...]
    # 对comment和score进行处理，获得能直接写入文本的数据列表。
    new_comment = [i.replace("\"content\":","").replace("\"","").strip() for i in comment]     # 如['机器暂时没啥问题，物流很快',....]
    new_score = [i.replace("\"score\":","").replace("\"","").strip() for i in score]           # 如['1', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0']
    if len(score) == len(comment):                                  # 检测获取的得分和评论长度是否相等
        return new_score, new_comment
    else:
        print("获取的评分与评论的数量不相等！！！！")

if __name__ == '__main__':
    # 设置基本参数
    FILE = ALL_FILE              # 设置写入的文件
    SCORE = 3                         # 设置访问的url参数
    PAGE_NUM = 1000                    # 设置访问的url的页面总数
    # 打开要写入的文件
    iphone8_file = open(FILE, "w", encoding="utf-8")
    cnt = 0; sum_comments = 0         # cnt用来计数休眠，sum_comments记录采集到的评论总数
    for page_num in range(PAGE_NUM):
        url = gen_url(score=SCORE, page=page_num)           # 获取url
        text = getHTMLText(url); time.sleep(0.5)            # 获取html页面
        print(text)
        try:
            score, comment = processText(text)              # 获取得分和评论列表
            for i,j in zip(score, comment):                 # 将数据写入文本
                if i != "0" and j != "此用户未填写评价内容":    # 排除未编写的用户评论和重复评论
                    iphone8_file.writelines(i + " " + j + "\n")
            cnt += 1; sum_comments += len(comment)
            if cnt % 10 == 0:
                print("已获得{}条数据。".format(sum_comments))
                time.sleep(5)                                # 每获取10页信息，休眠10秒
        except:
            print("已获取到的评论页面数为：{}".format(page_num+1))
            continue
    iphone8_file.close()





