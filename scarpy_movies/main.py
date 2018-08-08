import requests
import os

def getHTMLMovies(url):
    try:
        headers = {"user-agent":"Mozilla/5.0"}
        r = requests.get(url,headers=headers, timeout=10)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.content                        # 获得二进制文件
    except:
        print("获取movies失败！！！！")


if __name__ == '__main__':
    url_hls = "https://hls1-l3.xvideos-cdn.com/74cb01038b6256ca927fbc05b2a6c46c3658d9de-1533753881/videos/hls/a4/58/88/a45888baef3923827781b9efc2a2dada/hls.m3u8"
    url_high ="https://vid-egc.xvideos-cdn.com/videos/mp4/a/4/5/xvideos.com_a45888baef3923827781b9efc2a2dada.mp4?ztdeOPPmk7bpggGB_gR4Dpi3WDd9fbf5azt1NhkPkNj1uVTTJd1QPJptQD37JlJ2lJVzmWmZRaPPTXlZhXXjmrUl3IP3rl71WP97GNmxbgEPbUy3v1jYLiCK5C22vSTt6gBGTNs91tISxRiQpHtibSyAJaYR9WtJt1e4XLpPBeLcP5vz9lTrJ3wcQTVjDtzBB_edk71SdRQ"
    new_url = "https://vid-egc.xvideos-cdn.com/videos/mp4/a/4/5/xvideos.com_a45888baef3923827781b9l&ipn=d&word=今日新鲜事&step_word=&ie=utf-8&in=&cl=2&lm=-1&st=undefined&cs=2749386478,3983218336&os=3681435141,2206867024&simid=0,0&pn=0&rn=1&di=145894226390&ln=1183&fr=&fmq=1533744471580_R&fm=&ic=undefined&s=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&is=0,0&istype=0&ist=&jit=&bdtype=0&spn=0&pi=0&gsm=0&objurl=http%3A%2F%2Fx.itunes123.com%2Fuploadfiles%2Fb2ab55461e6dc7a82895c7425fc89017.jpg&rpstart=0&rpnum=0&adpicid=0"
    photo_url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1533754621012&di=311881975f13c3a6206cead1725b181f&imgtype=0&src=http%3A%2F%2Fx.itunes123.com%2Fuploadfiles%2Fb2ab55461e6dc7a82895c7425fc89017.jpg"
    # 设置相关路径
    base_dir = os.getcwd()
    movie_file = os.path.join(base_dir, "taogu123.jpg")
    content = getHTMLMovies(photo_url)
    print("获取视频成功！！！！")
    if os.path.exists(movie_file):
        print("文件已存在！！！！")
    else:
        with open(movie_file, "wb") as f:
            f.write(content)
            print("文件保存成功！！！！")