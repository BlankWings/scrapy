# 储存文件路径和参数，还有基本的使用函数
import os

BASE_DIR = os.getcwd()      # 基础路径为../jd_comment
# data/文件夹下的文件
NEGATIVE_FILE = os.path.join(BASE_DIR, "data", "negative.txt")
NEUTRAL_FILE = os.path.join(BASE_DIR, "data", "neutral.txt")
POSITIVE_FILE = os.path.join(BASE_DIR, "data", "positive.txt")
ALL_FILE = os.path.join(BASE_DIR, "data", "all.txt")




# 生成好评，中评和差评的url链接
def gen_url(score, page):
    # print("score参数：1为差评，2为中评，3为好评 \npage参数为要爬取的评论第几页")
    url = "https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv109366&productId=5089273&score={}&sortType=6&page={}&pageSize=10&isShadowSku=0&fold=1".format(score,page)
    url = "https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv109407&productId=5089273&score={}&sortType=5&page={}&pageSize=10&isShadowSku=0&fold=1".format(score,page)
    url = "https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv109409&productId=5089273&score={}&sortType=5&page={}&pageSize=10&isShadowSku=0&fold=1".format(score,page)
    url = "https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv125790&productId=3133857&score={}&sortType=5&page={}&pageSize=10&isShadowSku=0&fold=1".format(score,page)
    return url