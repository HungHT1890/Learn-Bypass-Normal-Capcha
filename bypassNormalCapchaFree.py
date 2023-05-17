from requests import session
from urllib3 import disable_warnings
disable_warnings()

solver_false = 'solver_false'

def bypass_normal_capcha(api_key,capcha_option=1,image_url='null',image_b64='null',file_capcha_path='null',proxy=None):
    ss = session()
    TIME_OUT = 20
    # option 1 => image url to capcha result
    if capcha_option == 1:
        api = f'https://api.ocr.space/parse/imageurl?apikey={api_key}&url={image_url}'
        try:
            capcha_respond = ss.get(url=api,proxies=proxy , timeout = TIME_OUT,verify=False).json()['ParsedResults'][0]['ParsedText'].strip()
            return capcha_respond
        except Exception as f:
            return solver_false
    elif capcha_option == 2: #base64 image string to capcha result
        api = f'https://api.ocr.space/parse/image'
        header = {
            'apikey': api_key,
        }
        data = {
            'base64Image': image_b64,
        }
        try:
            capcha_respond = ss.post(url= api ,headers= header ,data= data , timeout = TIME_OUT,verify=False).json()['ParsedResults'][0]['ParsedText'].strip()
            return capcha_respond
        except:
            return solver_false
        
    elif capcha_option == 3: # file image to capcha results
        data = {
            'apikey': api_key,
        }
        api = f'https://api.ocr.space/parse/image'
        with open(file_capcha_path,'rb') as f:
            image_capcha = {
                'filename': f
            }
            try:
                capcha_respond = ss.post(url= api ,data= data , files=image_capcha,  timeout = TIME_OUT,verify=False).json()['ParsedResults'][0]['ParsedText'].strip()
                print(capcha_respond)
                return capcha_respond
            except Exception as f:
                print(f)
                return solver_false
    else:
        return solver_false



if __name__ == "__main__":
    api_key = ''
    # URL CAPCHA IMAGE
    capcha_option = 1
    image_url = 'https://www.textbroker.co.uk/wp-content/uploads/sites/2/2019/12/textbroker_fb.jpg'
    # results = bypass_normal_capcha(api_key,capcha_option,image_url)
    # print(results)


    #BASE64 CAPCHA IMAGE
    base64 = open(r"D:\CODE\REQUESTS\bypassCapchaNormal\base64.txt",'r').read()
    capcha_option = 2
    # results = bypass_normal_capcha(api_key=api_key,capcha_option=2,image_b64=base64)
    # print(results)

    #FILE CAPCHA IMAGE
    capcha_option = 3

    file_capcha_path = r'D:\CODE\REQUESTS\bypassCapchaNormal\demo_capcha.jpg'
    results = bypass_normal_capcha(api_key=api_key , capcha_option=3 , file_capcha_path=file_capcha_path)
    print(results)

