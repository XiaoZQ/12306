import urllib
import urllib.request, urllib.parse
import http.cookiejar
import re
import json
import ssl
from bs4 import BeautifulSoup
from info import user, password
from distinguish import postition
# from showjpg import showjpg

ssl._create_default_https_context = ssl._create_unverified_context
cookiejar = http.cookiejar.CookieJar()
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
          'Referer': 'https: // kyfw.12306.cn / otn / regist / init'}
# url = "https://www.douban.com/group/tianhezufang/discussion?start=0"
handler = urllib.request.HTTPCookieProcessor(cookiejar=cookiejar)
opener = urllib.request.build_opener(handler, urllib.request.HTTPHandler(debuglevel=1))


def login():
    # 验证码图片获取
    img_req = urllib.request.Request('https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.4535962540217122')
    img_req = opener.open(img_req)
    jpgname = 'touclick_image.jpg'
    with open(jpgname, 'wb') as f:
        f.write(img_req.read())
    # x = showjpg(jpgname)
    # print('x=', x)
    # 提交验证码信息
    req = urllib.request.Request('https://kyfw.12306.cn/passport/captcha/captcha-check',headers=header)
    pos_dot = postition()
    print('坐标：',pos_dot)
    data = {
        'answer': pos_dot,
        'login_site': 'E',
        'rand': 'sjrand'
    }

    data = urllib.parse.urlencode(data).encode(encoding='UTF8')
    req = opener.open(req, data=data).read().decode('utf-8')
    print("验证码响应值：", req)

    # 登陆请求
    req = urllib.request.Request('https://kyfw.12306.cn/passport/web/login')
    data = {
        'username': user,
        'password': password,
        'appid': 'otn'
    }
    data = urllib.parse.urlencode(data).encode(encoding='UTF8')
    req = opener.open(req, data=data).read().decode('utf-8')
    print("登陆响应值：", req)

    req = urllib.request.Request('https://kyfw.12306.cn/otn/login/userLogin')
    data = {
        '_json_att': ''
    }
    data = urllib.parse.urlencode(data).encode(encoding='UTF8')

    req = opener.open(req, data=data).read().decode('utf-8')

    req = urllib.request.Request('https://kyfw.12306.cn/passport/web/auth/uamtk')
    data = {
        'appid': 'otn'
    }
    data = urllib.parse.urlencode(data).encode(encoding='UTF8')
    req = opener.open(req, data=data).read().decode('utf-8')
    apptk = json.loads(req)
    #
    req = urllib.request.Request('https://kyfw.12306.cn/otn/uamauthclient')
    data = {
        'tk': apptk['newapptk']
    }
    data = urllib.parse.urlencode(data).encode(encoding='UTF8')
    req = opener.open(req, data=data).read().decode('utf-8')
    print(req)
    jsonObj = json.loads(req)
    if not jsonObj['result_code'] == 0:
        print(jsonObj['result_message'], '重新验证')
        login()


login()

req = urllib.request.Request('https://kyfw.12306.cn/otn/index/initMy12306', headers=header)
req = opener.open(req).read().decode('utf-8')
print('\n\n', req)
