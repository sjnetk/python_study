# 네이버 API 셋팅 주소 : https://developers.naver.com/main/
import os
import sys
import urllib.request
import pandas as pd
import json  # Added this line

client_id = "각자 입력"
client_secret = "각자 입력"

word=input("검색어")
encText = urllib.parse.quote(word)  # urllib.parse.quote()는 아스키코드 형식이 아닌 글자를 URL 인코딩 
url = "https://openapi.naver.com/v1/search/blog?query=" + encText  # json 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)  # html 오픈
rescode = response.getcode()

if rescode == 200:  # URL 통신가능
    response_body = response.read()
    print(response_body.decode('utf-8'))

    # json => df => csv 변환 저장
    test = json.loads(response_body)
    df = pd.json_normalize(test['items'])
    df.to_csv("%s.csv" % (word))
    # /content/drive/MyDrive/Colab Notebooks/%s.csv

else:
    print("Error Code:" + str(rescode))
