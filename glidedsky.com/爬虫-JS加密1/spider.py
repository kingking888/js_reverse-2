
from loguru import logger
import asyncio
import aiohttp
from lxml import etree
import math
import hashlib
total_list = []
from time import perf_counter
import requests
index = 1
cookies = {
    'Hm_lvt_020fbaad6104bcddd1db12d6b78812f6': '1586762129,1586764255,1586840738,1586921470',
    '_ga': 'GA1.2.1418418863.1586921470',
    '_gid': 'GA1.2.811575715.1586921470',
    'footprints': 'eyJpdiI6IlwvdnJJR2pNS3V0TnBaZ1I5eGNGZEt3PT0iLCJ2YWx1ZSI6IkZ2c3oxWkM5Sk9zRnZzcjI2bFFuXC9NYmx4ZXZYUVl1aWEwc01vUzh2ZkRtMHBrWnRaVXlDRzJGZjZTN0N2NG1oIiwibWFjIjoiZmMyNzFlMGJkMjczZGM3OGY0YmFmNWM4YjUwMTM5MDM1N2MxMDYwM2MyMDI4NTI3NGU4YTlmOTc1YzJlMmMwNiJ9',
    'XSRF-TOKEN': 'eyJpdiI6ImY3SDN4bkVkd1VsMGZVamtMZTFkdWc9PSIsInZhbHVlIjoiRUFEMGpuc0puNkhLeWNsWmM2RDZUaWlcL0FWV1BDdldaUmNYTHVFM1BGYVZZSzdBWnZGaGJ0Sk9Ya1lBeTAySkYiLCJtYWMiOiIwMTVjYmY4ZjQ2NmFlYTI0ZGJhNDlhYWIzNzJlYThkODlkYWRmODg1N2NjZWM0OTc2NTQ1MGMzYjM1Mjc2ODU0In0%3D',
    'glidedsky_session': 'eyJpdiI6Imt2aGQxZTZZaHl0WnZzTit0OVRTUWc9PSIsInZhbHVlIjoidG1PWDgxTk9cL2ZFbWZQc2pSZUZhQVNRSHBUWmV5VlJBd3pMcVhXelVsckFQaHU3QjNTTldRZDcwT1lndFwvSG5TIiwibWFjIjoiZmM1MTY0ZDBhMGI3ZmI4MzMwMDlmMWJkYmIzYzllY2FmMDhlMWQ4ZWFlNTMwNzUxOTk1OTBiODI1YmFlZjJiYiJ9',
    'Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6': '1586942836',
    '_gat_gtag_UA_75859356_3': '1',
}

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'http://glidedsky.com/level/web/crawler-javascript-obfuscation-1',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}


class SJS():
    def __init__(self,loop):
        self._loop = loop

    async def getText(self, url, semaphore,page):
        async with semaphore:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers, cookies=cookies) as response:
                    ns = await response.text()
                    html = etree.HTML(ns)
                    p = html.xpath('//*[@id="app"]/main/div[1]//@p')[0]
                    t = math.floor((int(html.xpath('//*[@id="app"]/main/div[1]//@t')[0])-99)/99)
                    res = 'Xr0Z-javascript-obfuscation-1'+str(t)
                    sha = hashlib.sha1(res.encode('utf-8'))
                    sign = sha.hexdigest()
                    url = f"""http://glidedsky.com/api/level/web/crawler-javascript-obfuscation-1/items?page={p}&t={t}&sign={sign}"""
                    async with session.get(url, headers=headers, cookies=cookies) as response:
                        item = await response.text()
                        import json
                        item = json.loads(item)
                        if item:
                            total_list.append(item['items'])
                        else:
                            print("wei>>")
                        print(">>>1", item)

async def main(loop):
    spider = SJS(loop=loop)
    semaphore = asyncio.Semaphore(50)
    for i in range(1, 1001):
        url = f'http://glidedsky.com/level/web/crawler-javascript-obfuscation-1?page={i}'
        task_list.append(asyncio.create_task(spider.getText(url, semaphore,i)))
    await asyncio.gather(*task_list)



if __name__ == "__main__":
    end = perf_counter()
    task_list = []
    total_list = []
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))

    mid_temp= [_ for c in total_list for _ in c]
    print("total", len(mid_temp))
    print("total_count", sum(mid_temp))
    print('TIME: ', perf_counter()-end)




