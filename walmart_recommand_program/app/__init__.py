from PIL import Image
import matplotlib.pyplot as plt
from PyKakao import Karlo
from flask import Flask, render_template, request
app = Flask(__name__)

search_result_eng = 'box'

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
import random as rd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


@app.route('/')
def index():
    return render_template('index.html')











product_copy_df = pd.read_csv('product_copy.csv')


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
    new_df = df.iloc[similar_indexes].copy()
    # new_df['similarity'] = similarity[product_index,:(top_n)]
    return new_df



if len(product_copy_df[product_copy_df['Description'].str.contains('box',case = False)]) > 0:
    x = rd.randint(0,len(product_copy_df[product_copy_df['Description'].str.contains('box',case = False)]))
    similar_target = product_copy_df[product_copy_df['Description'].str.contains('box',case = False)].iloc[x]['Description']
else:
    # 검색어가 포함된 행이 없으면 '없음'을 출력
    print('검색어가 포함된 행이 없습니다.')

similar_product = find_sim_product(product_copy_df, product_sim_sorted_ind, similarity,similar_target,5)
similar_product.drop(['Unnamed: 0', 'Country','CustomerID','Description_literal'], axis=1,inplace=True)
similar_product
similar_product.columns = ['상품코드', '상품명', '가격', '누적구매량']
present_image_name = similar_product['상품명'].iloc[0].strip()


# 발급받은 API 키 설정
KAKAO_API_KEY = '0a4de529e0392f4e061a94adf9cce499'

# Karlo API 인스턴스 생성
karlo = Karlo(service_key = KAKAO_API_KEY)

text = present_image_name

# 이미지 생성하기 REST API 호출
img_dict = karlo.text_to_image(text, 1)

# 생성된 이미지 정보
img_str = img_dict.get("images")[0].get('image')

# base64 string을 이미지로 변환
present_image = karlo.string_to_image(base64_string = img_str, mode = 'RGBA')

if __name__ ==  '__init__':
    app.run(debug = True)


