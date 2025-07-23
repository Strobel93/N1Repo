# dict = {'key1':1}
# dict2 = {'a':1,'b':2}
# print(dict['key1'])
# print(dict2['b'])

# for Key,Value in dict2.items():
#     print(Key,Value)

# fklist = [1,2,3,4,5,6,7]
# print(fklist[0])


import pandas as pd
 
data = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18]}
 
df = pd.DataFrame(data)
 
print(df[['Name','Age']])
print(df[df['Age']>=20])
print(df[df['Age']>=20])
print(df.iloc[0]) #First Row
print(df.iloc[[0],[0,1]]) #First Row 2 columns
print(df.loc[0],['Name','Age'])
