
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs  #라이브러리 불러오기 

url="https://www.starbucks.co.kr/store/getSidoList.do"

response=requests.post(url) #post로 받기

starbucks_sido=response.json() #API는 거의 제이슨 형식 
 

#시도 리스트 받아오기  
starbucks_sidolist=starbucks_sido['list']

df1=pd.DataFrame(starbucks_sidolist)

df1=df1.drop_duplicates()

pd.set_option('display.max_seq_items', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None) --#판다스 옵션세팅


df1=df1[['sido_cd','sido_nm']] #필요한 컬럼만 정리하기


#매장 리스트 받아오기 

sido_cd='01'

params = f"in_biz_cds=0&in_scodes=0&ins_lat=37.368665899999996&ins_lng=127.11512619999999&search_text=&p_sido_cd={sido_cd}&p_gugun_cd=&isError=true&in_distance=0&in_biz_cd=&iend=1000&searchType=C&set_date=&rndCod=3WBZBCPSZ8&all_store=0&T03=0&T01=0&T12=0&T09=0&T30=0&T05=0&T22=0&T21=0&T10=0&T36=0&P10=0&P50=0&P20=0&P60=0&P30=0&P70=0&P40=0&P80=0&whcroad_yn=0&P90=0&new_bool=0"

url="https://www.starbucks.co.kr/store/getStore.do?r=RO98U559C0"
response=requests.post(url,params=params)


starbucks_list=response.json()['list']

df2=pd.DataFrame(starbucks_list)

#정리를 위한 전처리
df3=df2[['s_name','sido_name','gugun_name','doro_address']]

cols=['sido_name','gugun_name','s_name','doro_address']
df3=df3[cols]

df3.columns=['도시','구군','지점명','도로명주소']

df3=df3.drop_duplicates()

df3.isnull().sum() 


#전국(모든 시도코드) 매장의 리스트 받아오기 위한 함수 정의

def starbucks(sido_cd):
    params = f"in_biz_cds=0&in_scodes=0&ins_lat=37.368665899999996&ins_lng=127.11512619999999&search_text=&p_sido_cd={sido_cd}&p_gugun_cd=&isError=true&in_distance=0&in_biz_cd=&iend=1000&searchType=C&set_date=&rndCod=3WBZBCPSZ8&all_store=0&T03=0&T01=0&T12=0&T09=0&T30=0&T05=0&T22=0&T21=0&T10=0&T36=0&P10=0&P50=0&P20=0&P60=0&P30=0&P70=0&P40=0&P80=0&whcroad_yn=0&P90=0&new_bool=0"
    url="https://www.starbucks.co.kr/store/getStore.do?r=RO98U559C0"
    response=requests.post(url,params =params)
    starbucks_list=response.json()['list']
    df2=pd.DataFrame(starbucks_list)
    df3=df2[['s_name','sido_name','gugun_name','doro_address']]
    cols=['sido_name','gugun_name','s_name','doro_address']
    df3=df3[cols]
    df3.columns=['도시','구군','지점명','도로명주소']
    return df3


#for문 이용해서 전국 매장 리스트 합치기   
a=[]
for i in [w for w in (df1['sido_cd'].sort_values().values)]:
    a.append(starbucks(i))
    df_final=pd.concat(a)



df_final=df_final.reset_index().drop('index',axis=1)

df_final['도시']=df_final['도시'].replace('강원도','강원')
