from flask import Flask, render_template, request
from PyKakao import KoGPT 
app = Flask(__name__)

api = KoGPT(service_key = "0a4de529e0392f4e061a94adf9cce499")
input = ''
prompt = """
주어진 단어를 영어로 바꿔주세요

단어 : 사과
결과 : apple

단어 : 생산하다
결과 : product

단어 : 물
결과 : water

단어 : 핑크 크리스탈 스컬 폰 참
결과 : PINK CRYSTAL SKULL PHONE CHARM

단어 : 컵
결과 : cup

단어 : 라면
결과 : ramen

단어 : 분홍 인형
결과 : pink doll

단어 : 우산
결과 : umbrella

단어 : 물병
결과 : water bottle

단어 : {input}
결과 : """
max_tokens = 20
result = api.generate(prompt, max_tokens, temperature=0.3)
result['generations'][0]['text'].split(',')[0].split('\n')[0].strip()


# [1]상품 discription 속성을 통한 상품 유사도 필터링
### [1]-1 목적 : 검색 시 유사 discription 출력 
### 데이터셋 walmart
# - StockCode: 구매별 코드 구분
# - Description: 상품 설명
# - UnitPrice: 상품 가격
# - CustomerID: 고객ID
# - Country: 구매국가
#모듈로딩
import pandas as pd
import numpy as np
import warnings; warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#데이터 로딩
product_df = pd.read_excel("Online Retail.xlsx")
#결측치 확인
product_copy_df = product_df.copy()
product_copy_df.drop(['InvoiceNo','InvoiceDate'], axis=1,inplace=True)
product_copy_df.isnull().sum()
#결측치 처리
print(product_copy_df['Description'].isnull().sum())
x = product_copy_df[product_copy_df['Description'].isnull() ==True]
print(x.CustomerID.isnull().sum())
#CustomerID는 결측치 처리를 Imputer를 사용해서 하기에는 애매함 drop
product_copy_df.dropna(inplace=True)
#결측치 처리 완료
product_copy_df.reset_index(inplace=True)
product_copy_df.drop('index',axis = 1,inplace=True)
product_copy_df.info()
# 상품데이터 설명 split
product_copy_df['Description_literal'] = product_copy_df['Description'].apply(lambda x: x.split(' '))

Quantity_sum = product_copy_df.groupby('StockCode').sum('Quantity')
Quantity_sum = Quantity_sum.reset_index()
Quantity_sum

Quantity_sum = Quantity_sum[['StockCode', 'Quantity']]

#중복 제거
product_copy_df= product_copy_df.drop_duplicates(subset=["StockCode"])
product_copy_df.info()
product_copy_df = product_copy_df.drop('Quantity',axis=1)
product_copy_df = pd.merge(product_copy_df, Quantity_sum, on= 'StockCode')
product_copy_df
product_copy_df['Country'] = product_copy_df['Country'].astype('category')
product_copy_df['Country'].value_counts()
count_vect = CountVectorizer(min_df=0, ngram_range=(1,2))
# description_mat = count_vect.fit_transform(product_copy_df['Description'])
# print(description_mat)
count_vect.fit(product_copy_df['Description'])
description_mat = count_vect.transform(product_copy_df['Description'])

print(description_mat.shape)
product_sim = cosine_similarity(description_mat,description_mat)

product_sim_sorted_ind = product_sim.argsort()[:,::-1]
product_sim_sorted_ind
similarity = np.round(np.sort(product_sim)[:,::-1],3)
similarity

product_sim_sorted_ind[:1]
product_copy_df
def find_sim_product(df, sorted_ind, similarity,product_description, top_n = 10):
    product_description = df[df['Description'] == product_description]
    product_index = product_description.index.values
    similar_indexes = sorted_ind[product_index,:(top_n)]
                    
    similar_indexes = similar_indexes.reshape(-1)
    a = similarity[product_index,:(top_n)]
    a= list(a)
    a.split(' ')
    print(a)
    new_df = df.iloc[similar_indexes].copy()
    # new_df['similarity'] = similarity[product_index,:(top_n)]
    return new_df
similar_product = find_sim_product(product_copy_df, product_sim_sorted_ind, similarity,'CLASSIC WHITE FRAME',10)
similar_product