from bypassNormalCapchaFree import bypass_normal_capcha
from bypassInvisCapcha import  bypass_capcha
from urllib3 import disable_warnings
from define import *
from requests import session
disable_warnings()

def bypass_capcha_demo(bienso='29A34809'):
    ss = session()
    url_check = f'https://www.csgt.vn/tra-cuu-phuong-tien-vi-pham.html?&LoaiXe=1&BienKiemSoat={bienso}'
    url_check_respond_cookie = ss.get(url=url_check,headers=check_header,verify=False).cookies.get_dict()
    PHPSESSID = url_check_respond_cookie['PHPSESSID']
    BIGipServerWeb = url_check_respond_cookie['BIGipServerWeb-csgt-pool']
    tracuu_cookie = f'_ga=GA1.2.1205164913.1684257681; _gid=GA1.2.1479880717.1684257681; PHPSESSID={PHPSESSID}; BIGipServerWeb-csgt-pool={BIGipServerWeb}'

    with open('capcha.png','wb') as f:
        f.write(ss.get(url=api_capcha_image).content)

    capcha_image = bypass_normal_capcha(api_key=capcha_api_key,capcha_option=3,file_capcha_path=r'capcha.png')
    capcha_image = str(capcha_image).replace(' ','').lower()
    capcha_invisible = bypass_capcha(api_get_invisible_capcha,api_post_invisible_capcha)
    print(capcha_invisible)
    tracuu_data = f'BienKS={bienso}&Xe=1&captcha={capcha_image}&token={capcha_invisible}&ipClient=9.9.9.91&cUrl=1'
    print(tracuu_data)

    tracuu_header = {
        'Accept': '*/*',
        'Accept-Language': 'en,vi;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Length': '1980',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': tracuu_cookie,
        'Host': 'www.csgt.vn',
        'Origin': 'https://www.csgt.vn',
        'Pragma': 'no-cache',
        'Referer': 'https://www.csgt.vn/tra-cuu-phuong-tien-vi-pham.html?&LoaiXe=1&BienKiemSoat=29A34809',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
            }
    respond_check = ss.post(url=tracuu_url ,headers=tracuu_header, data=tracuu_data).json()['href']
    respond_tracuu = ss.get(url=respond_check, verify=False)
    print(respond_tracuu.text)
    # print(respond_check.text)



if __name__ == '__main__':
    bypass_capcha_demo()