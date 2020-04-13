import requests
from lxml import etree

cookies = {
    'Hm_lvt_020fbaad6104bcddd1db12d6b78812f6': '1586762129',
    '_ga': 'GA1.2.686941634.1586762129',
    '_gid': 'GA1.2.1492972283.1586762129',
    'footprints': 'eyJpdiI6IlJ0a0Jqb1krRWdaWEtwZWprZmNCeHc9PSIsInZhbHVlIjoiWnZoVTBhTU5iVFZHVGRucjlUTUU3NE9RU2k4aXpMc3V2MTVQNmRNam40eGhiNTFielpxZWxLUHg1bUQwNGtpeCIsIm1hYyI6IjA0N2I4ZTRkYjNlY2MwMzc4NWQ3OTZjZTczYzQ1YzRjOWNiYjJiZDIzMDEwZTFlMDc4Nzg2OTkxOTk2MGExNzAifQ%3D%3D',
    'XSRF-TOKEN': 'eyJpdiI6IkI4S0xjc0wyNzhIZmlDU0FpUlQybVE9PSIsInZhbHVlIjoiQmJ1empBNUlpRE1LTFladVFJdVBkbTdYTnhsdXJyWjV3eG9sZTZrWE03VFkwYW5RbVwvRVF6ZWVLODNJTWlmM2ciLCJtYWMiOiI1MjA0MjkxYWY3YjY4OGY3ZDc1ZWVhYzljOTU1OGY5YTkyZGNlYjNkZWI0MzZhNmFiOWIyN2Y0OGQ1NGRkMTM0In0%3D',
    'glidedsky_session': 'eyJpdiI6InBzUmVuVEJtaUYrUXRUa0dWVmRaMGc9PSIsInZhbHVlIjoiSXJxZnlHaDhcL0xGenY3bHdZZCtLNHBicFY0cEtGM0dTbGg3SHpJQ0s1N0xQSjBLdTF1NXJKd1dIN3ZvTGdDZUciLCJtYWMiOiIzZDM1MzlmNTM2MTdjOGJiNDYzMDZhYzRkNWU2OWQyYzI0MzM3OTVkYmQxMTFkYmRhMDRkZGZhNTk5MzQ2OGU5In0%3D',
    'Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6': '1586763105',
}

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'http://glidedsky.com/level/crawler-basic-1',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

response = requests.get('http://glidedsky.com/level/web/crawler-basic-1', headers=headers, cookies=cookies, verify=False)
html = etree.HTML(response.text)

html_data = html.xpath('//*[@id="app"]/main/div[1]/div/div/div//text()')
html_data = [int(i.replace("\n","").replace(" ","")) for i in html_data if i.replace("\n","").replace(" ","")]
print(html_data,">>>", type(html_data),len(html_data))
print(sum(html_data))