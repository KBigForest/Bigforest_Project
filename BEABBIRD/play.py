# %%
import pandas as pd
data = pd.read_csv('C:/Users/dddf/Desktop/play.csv')
data.columns
data['소재지전체주소'].isna().sum()
data = data[data['소재지전체주소'].isnull() == False]

data.drop(['개방서비스명','영업상태명','상세영업상태코드','소재지전화','소재지우편번호','최종수정시점','데이터갱신구분','데이터갱신일자'], axis=1, inplace=True)
print(data['위생업태명'].values)
data = data[data['위생업태명']!='7/2/21 0:23']
data = data[data['위생업태명']!='2/25/22 2:40']
data = data[data['위생업태명']!='단란주점']
data['위생업태명'].value_counts()
data = data[data['위생업태명']!='한식']
df = data['소재지전체주소'].str.split(" ", expand=True)
df = df[[0,1]]
data =  pd.concat([data,df],axis=1)
data.rename(columns={0:'시도',1:'시군구'},inplace=True)
data
data.to_csv('C:/Users/dddf/Desktop/play2.csv')

#%%
import pandas as pd
dalran = pd.read_csv('C:/Users/dddf/Desktop/dalran.csv')
dalran['소재지전체주소'].isna().sum()
dalran = dalran[dalran['소재지전체주소'].isnull() == False]
dalran.isna().sum()
df = dalran['소재지전체주소'].str.split(" ", expand=True)
df = df[[0,1]]
dalran =  pd.concat([dalran,df],axis=1)
dalran.rename(columns={0:'시도',1:'시군구'},inplace=True)

dalran['시도 시군구'] = dalran['시도']+' '+dalran['시군구']
dalran.to_csv('C:/Users/dddf/Desktop/dalran2.csv')
# %%
#%%
import pandas as pd
you = pd.read_csv('C:/Users/dddf/Desktop/play2.csv')
pop = pd.read_csv('C:/Users/dddf/Desktop/pop_data.csv')
you= you.groupby(['시도']).count()
you.sort_index(inplace=True)
pop.sort_index(inplace=True)
you['인당 유흥업체 수'] = you['영업상태구분코드']/pop['인구']
# %%
you
# %%
import pandas as pd
t = pd.read_csv('C:/Users/dddf/Desktop/time_.csv')
t   
# %%
