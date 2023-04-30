import requests

url = "https://smartmll.com/ajax.php?"
# print("请输入你想查询的垃圾名称:")


def get_gbclass(gbname = '纸巾'):
    gbname = gbname
    params = {
        'gbname': gbname,
        'city': '上海'
    }
    headers = {
        'Host': 'smartmll.com',
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
        'sec-ch-ua-platform': "macOS",
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://smartmll.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'device_id=y8dpx1brh5tue6onp2rt; Hm_lvt_5cefb991d4264143c886e49a1f9f8124=1635607716; CURRENT_CITY=%25E4%25B8%258A%25E6%25B5%25B7%25E5%25B8%2582%252F%25E4%25B8%258A%25E6%25B5%25B7%25E5%25B8%2582; SDU=8; Hm_lpvt_5cefb991d4264143c886e49a1f9f8124=1635607755'
    }
    resp = requests.get(url, headers=headers, params=params)
    gbclass = resp.json()['res']['cat']
    return gbclass


if __name__ == '__main__':
    gbclass = get_gbclass()
    while gbclass == "重新输入":
        print("请重新输入")
        gbclass = get_gbclass()
    print(f'您所查询的垃圾的类别为{gbclass}')
    print("此次查询结果是否认可？ 认可请输入1 否则输入0")
    try:
        accept = int(input())
        if accept == 1:
            print("感谢您的使用")
            exit()
        else:
            print("请您将所需要分类的垃圾详细描述")
        gbname = input()
        gbclass = get_gbclass(gbname)
        print(f'您所查询的垃圾的类别为{gbclass}')
    except Exception as e:
        print(e)
