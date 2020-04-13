# 这样丢数据。。。布吉岛为啥

import time
import asyncio
import functools
import aiohttp
from lxml import etree
total_list = []
from time import perf_counter
now = lambda: time.time()
index = 1
index_2 = 1
head = {}
cookies = {
    '_ga': 'GA1.2.686941634.1586762129',
    '_gid': 'GA1.2.1492972283.1586762129',
    'footprints': 'eyJpdiI6IlJ0a0Jqb1krRWdaWEtwZWprZmNCeHc9PSIsInZhbHVlIjoiWnZoVTBhTU5iVFZHVGRucjlUTUU3NE9RU2k4aXpMc3V2MTVQNmRNam40eGhiNTFielpxZWxLUHg1bUQwNGtpeCIsIm1hYyI6IjA0N2I4ZTRkYjNlY2MwMzc4NWQ3OTZjZTczYzQ1YzRjOWNiYjJiZDIzMDEwZTFlMDc4Nzg2OTkxOTk2MGExNzAifQ%3D%3D',
    'Hm_lvt_020fbaad6104bcddd1db12d6b78812f6': '1586762129,1586764255',
    '_gat_gtag_UA_75859356_3': '1',
    'XSRF-TOKEN': 'eyJpdiI6InF4bkNsdjRaUEtGdXJDb0ZOSjFkY3c9PSIsInZhbHVlIjoiSnQ2MEM2Q2laNCtkcmFJQUd4OEVib2pvUU9YdzY3QlpQQUt1Slh1XC9jbGVDMXpzcTV0bFZzVXAyWXFBZ2VXcFoiLCJtYWMiOiI1MzhmMTExNTU3OTNkM2EzOTRhOTVhNzJhZTU1ODdhODYyNTI3YmE1ZWM5MjNjMmM2YjEzMTA2ZTA0ZDYyOTdkIn0%3D',
    'glidedsky_session': 'eyJpdiI6IklBV2c4RVFSeEszSnJqZWZaWjVJNGc9PSIsInZhbHVlIjoiVVdidGJGMk85TnNMQVh0a2RyS1AwRERSSWM1emducVNxXC9nYlRsUGtETENvcEpJa0VFODBcL3ZrRWZSQ0QrTUVQIiwibWFjIjoiNDhjZjE3ZjRjNjQ0ZWZiNzAwNzA5ODU1NDU2YmFhMmVkNjM0ZmYxNmQ4NTZiNmU3ODY2NDYyNDQ5Y2NmZmY2OCJ9',
    'Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6': '1586764527',
}

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'http://glidedsky.com/level/crawler-basic-2',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

async def do_some_work(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, cookies=cookies) as response:
            ns = await response.text()
            html = etree.HTML(ns)
            html_data = html.xpath('//*[@id="app"]/main/div[1]/div/div/div/div//text()')
            html_data = [int(i.replace("\n", "").replace(" ", "")) for i in html_data if
                         i.replace("\n", "").replace(" ", "")]
            if html_data:
                global index
                index = index+1
                print(index)
                print(html_data, ">>>", type(html_data), len(html_data))
                total_list.extend(html_data)
            else:
                global index_2
                print('index2',index_2)
                index_2 = index_2+1

def callback(t, future):
    print('Callback: ', t, future.result())

start = now()
tasks = []
# for i in range(1,3):
for i in range(1,1001):
    url = f'http://glidedsky.com/level/web/crawler-basic-2?page={i}'
    coroutine = do_some_work(url)
    tasks.append(asyncio.ensure_future(coroutine))
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

# for task in tasks:
#     task.add_done_callback(functools.partial(callback, 2))
#     print('Task return: {}'.format(task.result()))

print("total",len(total_list))
print('TIME: ', now() - start)
