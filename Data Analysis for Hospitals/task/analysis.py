import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 8)
general = pd.read_csv('test/general.csv')
prenatal = pd.read_csv('test/prenatal.csv')
sports = pd.read_csv('test/sports.csv')

#print(general.head(20))
#print(prenatal.head(20))
#print(sports.head(20))

prenatal.rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'}, inplace=True)
sports.rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'}, inplace=True)

df = pd.concat([general, prenatal,sports], ignore_index=True)
df.drop(columns=['Unnamed: 0'], inplace=True)
#print(df.sample(n=20, random_state=30))

#df.dropna()
df.dropna(axis=0, how='all', inplace=True)
df['gender'] = df['gender'].replace(['female','woman'],'f')
df['gender'] = df['gender'].replace(['male','man'],'m')

df['gender'] = df['gender'].fillna('f')
cols = ['bmi', 'diagnosis', 'blood_test', 'ecg', 'ultrasound', 'mri', 'xray', 'children', 'months']
df[cols]=df[cols].fillna(0)
#print(df.shape)
#print(df.sample(n=20, random_state=30))

first = df['hospital'].value_counts().idxmax()
#print(first)

second = df.loc[(df['hospital'] == 'general')]
second_1 = df.loc[(df['hospital'] == 'general') & (df['diagnosis'] == 'stomach')]
second_ans = round(len(second_1)/len(second),3)
#print(second_ans)

third = df.loc[(df['hospital'] == 'sports')]
third_1= df.loc[(df['hospital'] == 'sports') & (df['diagnosis'] == 'dislocation')]
third_ans = round(len(third_1)/len(third), 3)
#print(third_ans)

fourth = df.loc[(df['hospital']=='general')]
fourth_1 = fourth['age'].median()
#print(fourth_1)
fourth_2 = df.loc[(df['hospital'] == 'sports')]
fourth_3 = fourth_2['age'].median()
#print(fourth_3)
fourth_ans = fourth_1 - fourth_3
#print(fourth_ans)

fifth = pd.pivot_table(df, index=['hospital','blood_test'],aggfunc='count')
#print(fifth)
# print('The answer to the 5th question is',first)
# print('The answer to the 5th question is',second_ans)
# print('The answer to the 5th question is',third_ans)
# print('The answer to the 5th question is',fourth_ans)
# print('The answer to the 5th question is prenatal, 325 blood tests')
#
histo = df.hist(column='age',bins=[0,15,35,55,70,80])
plt.show(histo)
pieplot = df['diagnosis'].value_counts().plot(kind='pie')
plt.show(pieplot)
import seaborn as sns
ax = sns.violinplot(x='hospital', y="height", data=df)
plt.show(ax)

print('The answer the 1st question: 15-35')
print('The answer the 2nd question: pregnancy')
print('The answer the 3rd question: It\'s because sports players tend to be taller than babies and the general population')
