# 建立以requests库为基础的爬虫，爬去京东商品评论
import requests
# 使用user-agent模拟浏览器访问服务器
def getHTMLText(url):
    try:
        kv = {"user-agent": "Mozilla/5.0"}                  # 设置爬取时的相关参数
        r = requests.get(url, headers=kv, timeout=30)       # 获得url内容
        r.raise_for_status()                   # 如果获取失败，产生异常，跳转到except
        r.encoding = r. apparent_encoding      # 解析页面内容
        requests_headers = r.request.headers   # 爬虫发给浏览器的头部文件
        return r.text
    except:
        print("获取HTML失败！！！！")

if __name__ == '__main__':
    url = "https://item.jd.com/5475612.html"
    print(getHTMLText(url))



