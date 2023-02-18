# 보통 물가가 오르면 물류비용 역시 증가한다고 생각할 것이다.
# 물류비용에 대한 추이를 보여주는 그래

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('컨테이너운임지표.xlsx')
df = df.transpose()
df = df.reset_index()
df.rename(columns={'index':'date', 0:'CCFI',1:'SCFI'},inplace=True)
df = df.drop(0)
y1 = round(df['CCFI'].mean(),2)
y = [y1 for i in range(0,len(df['CCFI']))]
z1 = round(df['SCFI'].mean(),2)
z = [z1 for i in range(0,len(df['SCFI']))]

df['date'] = pd.to_datetime(df['date'])
df['date'] = df['date'].dt.strftime('%Y/%m')

x = range(len(df['date']))
plt.rcParams['font.family'] = 'D2Coding'
plt.figure(figsize=(30,15))
plt.plot(x, df['SCFI'],'-o', color = 'blue', label = '상하이컨테이너운임지수 SCFI')
plt.plot(x, df['CCFI'],'-o', color = 'red',label = '중국컨테이너운임지수 CCFI')
plt.plot(x, z, color = 'lightblue', label = '상하이컨테이너운임지수 SCFI 평균')
plt.plot(x, y, color = 'pink', label = '중국컨테이너운임지수 CCFI 평균')
for i in range(len(df['date'])):
    height = df['SCFI'].iloc[i]
    if i == 24:
        plt.text(i, height + 10,height, ha = 'center', va = 'bottom', size = 15)
        plt.text(i-2, height + 10,'최대', ha = 'center', va = 'bottom', size = 15)
    elif i == 36:
        plt.text(i, height -200,height, ha = 'center', va = 'bottom', size = 15)
        plt.text(i-2, height - 200,'최근', ha = 'center', va = 'bottom', size = 15)
    else:
        plt.text(i, height + 10, height, ha = 'center', va = 'bottom', size = 6)
for i in range(len(df['date'])):
    height = df['CCFI'].iloc[i]
    if i == 24:
        plt.text(i, height + 10, height, ha = 'center', va = 'bottom', size = 15)
        plt.text(i-2, height + 10,'최대', ha = 'center', va = 'bottom', size = 15)
    elif i == 36:
        plt.text(i, height +50,height, ha = 'center', va = 'bottom', size = 15)
        plt.text(i-2, height + 50,'최근', ha = 'center', va = 'bottom', size = 15)    
    else:
        plt.text(i, height + 10, height, ha = 'center', va = 'bottom', size = 6)
    
plt.text(36.3,y1-10 , y1)
plt.text(35.5,y1-10 , '평균')
plt.text(36.3,z1-10 , z1)
plt.text(35.5,z1-10 , '평균')
plt.title('[2020/1 ~ 2023/1] 월별 컨테이너운임지수',fontsize = 25)
plt.xlabel('월별 추이')
plt.ylabel('Index')
plt.xticks(x, df['date'],rotation = 70)
plt.legend()
plt.show()
