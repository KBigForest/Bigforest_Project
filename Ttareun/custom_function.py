import numpy
import matplotlib.pyplot as plt
import pandas

##################################################################################################################################################

def check_na(df:pandas.DataFrame ,target:list=[],ignore:list=[]):
    
    na_list = [numpy.inf,numpy.nan,'',' ',None,'nan','NaN']+target
    na_list = list(set(na_list)-set(ignore))
    contain_na = False    
    
    for na in na_list:
        sum_na = (df==na).sum()
        
        if not sum(sum_na):
            continue
        
        else:
            contain_na = True
            col_count_dict = dict((df==na).sum())
            
            for col in col_count_dict:
                if not col_count_dict[col]:
                    continue
                
                else:
                    print(f'{col}열에 {na}값이 {col_count_dict[col]}개 있습니다.')
        
    print(f'결측치가 없습니다' if not contain_na else f'결측치가 있습니다')

##################################################################################################################################################

def check_hist(df:pandas.DataFrame,rows:int,cols:int,fig_size:tuple=(12,20)):
    if len(df.columns)>rows*cols:
        print('행과 열의 수를 확인하시오.')
        return
    fig, axs = plt.subplots(rows, cols, figsize=fig_size)
    df_col_idx = 0

    for row in range(rows):
        for col in range(cols):
            axs[row,col].hist(df[df.columns[df_col_idx]])
            axs[row,col].set_title(df.columns[df_col_idx])
            df_col_idx+=1
    plt.show()

##################################################################################################################################################

def check_scatter(df:pandas.DataFrame,features:list,target:str,rows:int,cols:int,figsize:tuple):
    
    fig, axs = plt.subplots(rows, cols, figsize=figsize)
    idx = 0
    
    for row in range(rows):
        for col in range(cols):
            axs[row,col].scatter(df[features[idx]],df[target])
            axs[row,col].set_title(features[idx])
            idx+=1
    plt.show()
    
##################################################################################################################################################    
   
def check_unique_rate(df:pandas.DataFrame):
    for col in df:
        print(f'{col}: {len(df[col].unique())/len(df)*100:2f}%')
        
##################################################################################################################################################

def sort_by_corr(df:pandas.DataFrame,target_col:list,abs_value=True):
    for col in target_col:
        if abs_value==True:
            corr_dict = dict(abs(df.corr()[col]))
        else:
            corr_dict = dict(df.corr()[col])
        sorted_corr_dict =(dict(sorted(corr_dict.items(),key = lambda x: x[1],reverse=True)))
        print(f'---------------{col}---------------')
        for i in sorted_corr_dict:
            if i == col:
                continue
            print(f'{i}: {sorted_corr_dict[i]*100:2f}%')
        print()
    print('-'*40)
            
##################################################################################################################################################

def min_max_scaler(series:pandas.Series):
    return (series-min(series))/(max(series)-min(series))

##################################################################################################################################################

def standard_scaler(series:pandas.Series):
    return (series-series.mean())/series.std()

##################################################################################################################################################

def kfold_generator(df:pandas.DataFrame,K:int=5,drop_last:bool=True,shuffle:bool=False):
    
    if shuffle:
        df = df.sample(frac=1)
        
    
    kfold_dict = dict()
    
    val_len = len(df)//K
    val_start_idx = 0
    val_end_idx = val_len
    
    if drop_last:
        for i in range(K):
            

            train_head = df.iloc[:val_start_idx,:]
            val_data = df.iloc[val_start_idx:val_end_idx,:]
            train_tail = df.iloc[val_end_idx:,:]
                
            train_data = pandas.concat([train_head,train_tail],axis=0)
                       
            kfold_dict[i] = (train_data,val_data)
            
            val_start_idx+= val_len
            val_end_idx += val_len
        
        return kfold_dict


    
    else:
        for i in range(K):
            
            if i != K-1:
                train_head = df.iloc[:val_start_idx,:]
                val_data = df.iloc[val_start_idx:val_end_idx,:]
                train_tail = df.iloc[val_end_idx:,:]
                
                train_data = pandas.concat([train_head,train_tail],axis=0)
            
            else:
                val_data = df.iloc[val_start_idx:,:]
                train_data = df.iloc[:val_start_idx,:]
            
            
            kfold_dict[i] = (train_data,val_data)
            
            val_start_idx+= val_len
            val_end_idx += val_len
        
        return kfold_dict
 
 ##################################################################################################################################################
    
def feature_label_spliter(df:pandas.DataFrame,label_index:int):
    X_head = df.iloc[:,:label_index]
    X_tail = df.iloc[:,label_index+1:]
    
    X = pandas.concat([X_head,X_tail],axis=1)
    X = X.values
    y = df.iloc[:,label_index].values
    
    return X,y