# -*- encoding: utf-8 -*-
'''
@File    :   font.py
@Time    :   2020/4/13 10:00:00
@Author  :   xahoo
@PythonVersion  :   3.6
@purpose ：  获取所有字体获取所有字体所被代表的  数字+坐标(放在列表)
'''
import random
import re
import time
import base64
from pathlib import Path  # 以后要习惯用 pathlib(新模块)
import requests
from fontTools.ttLib import TTFont
cookies = {
    'footprints': 'eyJpdiI6IkVyc21xbFNzQmVVN29mSTZGcnIxMnc9PSIsInZhbHVlIjoiUWdGSStSNGxzU3NHMysxYmNxMjhxWVNlaUJzZ0VPZjhvTytlQVpCck90NitpR1RNZUZtOCtuQWY3NTJ1WHdsaiIsIm1hYyI6IjMzOTZmMDFlZmYxMTExNjdjMTliODcwOGYyZDYzM2E2YzVlZDM1MGVmNGJiZGY3MjAyOGMzM2E5NzhmMTljY2YifQ%3D%3D',
    'Hm_lvt_020fbaad6104bcddd1db12d6b78812f6': '1586762129,1586764255,1586840738',
    '_ga': 'GA1.2.1654869159.1586840738',
    '_gid': 'GA1.2.253173194.1586840738',
    'XSRF-TOKEN': 'eyJpdiI6IkE2MWF1RjJEM1wvNWxkRVB4MVVCVHdBPT0iLCJ2YWx1ZSI6ImN5WVAwTUU3VmdQcVwvXC9BSmdSclIrQnBRY1NnbnB6Mlo4NUd4cFNVNms4UW5oUjQ2RXpaZFFWUE5ZOXc4YTNJZSIsIm1hYyI6IjJjZTk5NjRiZmFmMDYxNTg0ZTJmZjc1MDQ4ZjQyN2JlMDU4MTc4YWQzYTRiYTk3ODRhNmMxNDk2MGQ3ZGE4M2QifQ%3D%3D',
    'glidedsky_session': 'eyJpdiI6IjBwNTY0NlRtaVU1K0FUNlFFSmx6TUE9PSIsInZhbHVlIjoiVDZ2MGZ1QnBodWZwdlRFa0RJS2pucUJKVWMzSnVcL21YYzlOZnRNWGU0MUpNNDJveHJxc0ViZXR2dGlKQ1ZrQ3EiLCJtYWMiOiI3NjkwMDc4OTAxNzc1MDQ1NTM2NTcwYzU4YWZiYjU4OTY2NTYyMGU1YjkzN2EwYTdhZTE2M2M5ZjNjYjIxNDlmIn0%3D',
    'Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6': '1586840830',
}

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'http://glidedsky.com/level/crawler-font-puzzle-1',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

# 定义默认文件 定义默认url  定义默认headers
_fonts_path = Path(__file__).absolute().parent / "fonts"
_brand_url = "http://glidedsky.com/level/web/crawler-font-puzzle-1?page=1"
_headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
}
_proxies = random.choice([
    {"HTTP": "你的代理ip"},
])

def get_font_contengt(i):
    res = requests.get(f'http://glidedsky.com/level/web/crawler-font-puzzle-1?page={1}', headers=headers, cookies=cookies,
                       verify=False)
    base64Str = re.findall(r'font;charset=utf-8;base64,(.*?)format', res.text.replace("\n", "").replace(" ", ""))[0]

    binData = base64.decodebytes(base64Str.encode())
    # 写入ttf字体文件
    filePath01 = f'{i}.ttf'

    with open(filePath01, 'wb') as f:
        f.write(binData)
        f.close()
# 
# for x in range(1,6):
#     get_font_contengt(x)




# 获取所有字体所被代表的  数字+坐标
def get_coor_info(font, cli):  # 参数font指的是 字体文件(.ttf); 参数cli指的是字体文件里面的数字顺序 例如[6, 7, 4, 9, 1, 2, 5, 0, 3, 8]
    glyf_order = font.getGlyphOrder()[1:]
    info = list()
    for i, g in enumerate(glyf_order):
        coors = font['glyf'][g].coordinates  # 获取字体的所有横纵坐标
        # print("111111", coors)
        # GlyphCoordinates([(420, 521),(408, 574),(386, 597),(349, 635),(302, 635),(248, 635),(220, 612),(177, 580),(154, 531),(141, 492),(137, 449),(128, 407),(128, 352),(161, 402),(254, 449),(306, 449),(395, 449),(522, 316),(522, 211),(522, 143),(493, 83),(463, 36),(412, -7),(360, -39),(284, -39),(180, -39),(39, 124),(39, 317),(39, 530),(117, 619),(185, 710),(301, 710),(388, 710),(443, 661),(498, 614),(510, 528),(420, 518),(142, 214),(143, 166),(154, 122),(182, 79),(254, 35),(292, 29),(347, 41),(386, 81),(430, 127),(430, 206),(428, 287),(381, 326),(349, 370),(228, 370),(142, 282),(142, 211)])

        coors = [_ for c in coors for _ in c]
        # print("2222222", coors)
        # [420, 521, 408, 574, 386, 597, 349, 635, 302, 635, 248, 635, 220, 612, 177, 580, 154, 531, 141, 492, 137, 449, 128, 407, 128, 352, 161, 402, 254, 449, 306, 449, 395, 449, 522, 316, 522, 211, 522, 143, 493, 83, 463, 36, 412, -7, 360, -39, 284, -39, 180, -39, 39, 124, 39, 317, 39, 530, 117, 619, 185, 710, 301, 710, 388, 710, 443, 661, 498, 614, 510, 528, 420, 518, 142, 214, 143, 166, 154, 122, 182, 79, 254, 35, 292, 29, 347, 41, 386, 81, 430, 127, 430, 206, 428, 287, 381, 326, 349, 370, 228, 370, 142, 282, 142, 211]
        coors.insert(0, cli[i])
        # [6, 420, 521, 408, 574, 386, 597, 349, 635, 302, 635, 248, 635, 220, 612, 177, 580, 154, 531, 141, 492, 137, 449, 128, 407, 128, 352, 161, 402, 254, 449, 306, 449, 395, 449, 522, 316, 522, 211, 522, 143, 493, 83, 463, 36, 412, -7, 360, -39, 284, -39, 180, -39, 39, 124, 39, 317, 39, 530, 117, 619, 185, 710, 301, 710, 388, 710, 443, 661, 498, 614, 510, 528, 420, 518, 142, 214, 143, 166, 154, 122, 182, 79, 254, 35, 292, 29, 347, 41, 386, 81, 430, 127, 430, 206, 428, 287, 381, 326, 349, 370, 228, 370, 142, 282, 142, 211]
        # print(coors)
        # print("3333333333", coors)
        info.append(coors)
    return info


# get_coor_info(TTFont(_fonts_path/"1.ttf"),[6,7,4,9,1,2,5,0,2,8])

def get_font_data():
    font_1 = TTFont("1.ttf")
    font_1.saveXML('1.ttf.xml')
    cli_1 = ['zero','eight','seven','two','three','one','four','six','nine','five']
    coor_info_1 = get_coor_info(font_1, cli_1)
    # print(coor_info_1)
    # print("*"*30)
    font_2 = TTFont("2.ttf")
    font_2.saveXML('2.ttf.xml')
    cli_2 = ["three","nine","zero","seven","six","one","two","eight","four","five"]
    coor_info_2 = get_coor_info(font_2, cli_2)

    font_3 = TTFont("3.ttf")
    font_3.saveXML('3.ttf.xml')
    cli_3 = ["three","nine","zero","seven","six","one","two","eight","four","five"]
    coor_info_3 = get_coor_info(font_3, cli_3)
    #
    font_4 = TTFont("4.ttf")
    font_4.saveXML('4.ttf.xml')
    cli_4 = ["eight","six","four","one","nine","zero","seven","three","five","two"]
    coor_info_4 = get_coor_info(font_4, cli_4)

    font_5 = TTFont("5.ttf")
    font_5.saveXML('5.ttf.xml')
    cli_5 = ["zero","one","two","four","six","five","eight","seven","nine","three"]
    coor_info_5 = get_coor_info(font_5, cli_5)

    # 列表相加
    infos = coor_info_1 + coor_info_2 + coor_info_3 + coor_info_4 + coor_info_5
    dics = {'zero': 0, 'eight': 8, 'seven': 7, 'two': 2, 'three': 3, 'one': 1, 'four': 4, 'six': 6, 'nine': 9,
            'five': 5}
    for i in infos:
        i[0] = dics[i[0]]

    return infos

import pprint

pprint.pprint(get_font_data())