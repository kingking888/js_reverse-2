import base64
from io import BytesIO
from fontTools.ttLib import TTFont
import requests
import re,time
import xml
from concurrent.futures import ThreadPoolExecutor, as_completed
import xml.dom.minidom as xmldom
from lxml import etree
import requests
total = []
def get_text(i):
    cookies = {
        'footprints': 'eyJpdiI6IklMaHFLd28wVGRoajhYS0lBMVFSU2c9PSIsInZhbHVlIjoiSnhrRjZ3NnY1Y3QwK2tSbGxOeW1xYXRDXC9JMkhcL1B3WWxmQURRMEszU29kNUhXVzR3cHd4UXlhOUxFZGF3ckdJIiwibWFjIjoiYTQ1NjBiNGNiOWYwZTY5ZWI0OGQzMzU3MDkwOGUwNDEzMzczNjNkYmRhNmI5M2Y5NzBiYzlhOTFlYjJhMTAxYSJ9',
        'Hm_lvt_020fbaad6104bcddd1db12d6b78812f6': '1586762129,1586764255,1586840738,1586921470',
        '_ga': 'GA1.2.1418418863.1586921470',
        '_gid': 'GA1.2.811575715.1586921470',
        'XSRF-TOKEN': 'eyJpdiI6InR4Zll1K1k4MWhZa250N3F6MjNrZ1E9PSIsInZhbHVlIjoiVlZ5SmxSQ2hncDFLQlE4REVvNzlneTUwUlk2Zmg5aUxMOE0rQXY3MFBZMWhhOFp2c2xPaFJlYTA5NVoyN3QweSIsIm1hYyI6ImUzOWI2YTdjYmI0OGUyYTJhOTgxNGRjZTZkMDMwZTk5OTllNGQyMTVlZDQzODE0ZDBkNzdlYmI2Zjk0YmMzOWQifQ%3D%3D',
        'glidedsky_session': 'eyJpdiI6IjlGU1NldzZBTTFuY24xcE5GYWJKYkE9PSIsInZhbHVlIjoiK2l5RkRUaTRJUFVTK1B6NW5kTTErS3MrcFQya3JRTEV1b3E4VmQxcUV5N0RWeFR6K0QraVV1bXBtV0NJMXJRSiIsIm1hYyI6Ijk4ZGVjYmQ3MjViNmFlY2QwYzczNDc2MjlkNWI5MGFlMjYyZDk4NTY5YjVmYjA3ZWY0MzljMGY4NDNhNjE1NzMifQ%3D%3D',
        'Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6': '1586921501',
    }
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://glidedsky.com/rank',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    url = f'http://glidedsky.com/level/web/crawler-font-puzzle-1?page={i}'
    res = requests.get(url, headers=headers, cookies=cookies, verify=False)
    create_file(res.text,url)



def create_file(text,url):
    base64Str = re.findall(r'font;charset=utf-8;base64,(.*?)format', text.replace("\n", "").replace(" ", ""))[0]
    binData = base64.decodebytes(base64Str.encode())
    # 写入ttf字体文件
    filePath01 = r'test.ttf'
    with open(filePath01, 'wb') as f:
        f.write(binData)
        f.close()
    # 解析字体库
    try:
        font01 = TTFont(filePath01)
        font01.saveXML('test.ttf.xml')
    except:
        print(url, base64Str)

    replace_text(text)


def replace_text(text):
    dict = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    newdict = {}
    dom = xmldom.parse('test.ttf.xml')
    root = dom.documentElement
    bb = root.getElementsByTagName('GlyphID')
    for j in range(1, 11):
        # 下标从 1 开始，获取的是zero,
        k = bb[j].getAttribute("name")
        # 在字体文件 xml 中对应关系就是 j-1, 也就是0， zero对应的就是0，注释仅针对第一个字体文件
        # 建立对应关系，取出真实的 name 对应的数字。
        newdict[dict[k]] = str(j - 1)
    html = etree.HTML(text)
    result_li = html.xpath('//*[@id="app"]/main/div[1]/div/div/div/div//text()')
    result_li = [str(x).replace(' ',"").replace("\n","") for x in result_li]
    result_res = []
    for index, a in enumerate(result_li):
        temp = list(a)
        for index, b in enumerate(a):
            temp[index] = newdict[b]
        result_res.append("".join(temp))
    print(result_res)
    total.append(result_res)

# for i in range(1,10):
#     get_text(i)
# # print(sum(total_list))


# with ThreadPoolExecutor(max_workers=18) as t:
#     obj_list = []
#     begin = time.time()
#     for page in range(1, 15):
#         obj = t.submit(get_text, page)
#         obj_list.append(obj)
#
#     for future in as_completed(obj_list):
#         data = future.result()
#         print(data)
#         print('*' * 50)
#     times = time.time() - begin
#     print(times)
for page in range(1, 1001):
    get_text(page)

start = time.perf_counter()
sum_list = [_ for c in total for _ in c]
sum_list = [int(x) for x in sum_list]
print('total', len(total))
print('total_list', len(sum_list))
print('total_sum', sum(sum_list))
print("total_time", time.perf_counter()-start)

