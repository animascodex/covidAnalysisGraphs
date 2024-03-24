import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')



def Change_Report_Week(Date_Reported,Report_Week):
    df[Date_Reported] = pd.to_datetime(df[Date_Reported])
    df[Report_Week] = pd.to_datetime(df[Report_Week])
    df[Report_Week] = df[Date_Reported].dt.strftime('%a') #Change Column Report_Week to Day of the Week with data aquired from Date_Reported
df = pd.read_csv('TMAQ1.csv', sep=',',index_col=[0])



#Grab Province 'Ontario' Only
Data_Ontario_Only = df[~df['province'].isin(['Alberta','BC','New Brunswick','Nova Scotia'])]

Number_of_Province = df.groupby('province')['province'].count().reset_index(name='Total_cases_by_provinces')
Total_Case_By_Province = (Number_of_Province['Total_cases_by_provinces'])
fig = plt.figure()
axises = fig.add_axes([0, 0, 1, 1])
Province_name = ['Alberta', 'BC', 'New Brunswick', 'Nova Scotia', 'Ontario']
axises.bar(Province_name, Total_Case_By_Province)
plt.show()
df.groupby('province')['province'].count()
print(Number_of_Province)

#Calculate Number of Male Infectors in Ontario
Data_Ontario_Only_Male = Data_Ontario_Only[~Data_Ontario_Only['sex'].isin(['Female'])]
Data_Ontario_Only_Male = Data_Ontario_Only_Male.groupby('age')['age'].count()                            .reset_index(name='No. of Male Infectors:')                            .sort_values(['age'],ascending = False)
#Calculate Number of Female Infectors in Ontario
Data_Ontario_Only_Female = Data_Ontario_Only[~Data_Ontario_Only['sex'].isin(['Male'])]
Data_Ontario_Only_Female = Data_Ontario_Only_Female.groupby('age')['age'].count()                            .reset_index(name='No. of Female Infectors:')                            .sort_values(['age'],ascending = False)
#Set 9 Bar Plots, each for 1 age group
N = 9
menMeans = list(Data_Ontario_Only_Male['No. of Male Infectors:'])
womenMeans = list(Data_Ontario_Only_Female['No. of Female Infectors:'])
ind = np.arange(N) # the x locations for the groups
width = 0.35
fig = plt.figure()
axises = fig.add_axes([0,0,1,1])
axises.bar(ind, menMeans, width, color='r')
axises.bar(ind, womenMeans, width,bottom=menMeans, color='b')
axises.set_ylabel('Number of Men and Women Infected')
axises.set_title('Categorized by Agegroup and Gender')
axises.set_xticks([0,1,2,3,4,5,6,7,8])
axises.set_xticklabels(['0-19','20-29','30-39','40-49','50-59','60-69','70-79','80-89','90-99'])
axises.set_yticks(np.arange(0, 100, 10))
axises.legend(labels=['Men', 'Women'])
plt.show()


Change_Report_Week('date_report','report_week')           #Call Function

# Top three Days that COVID-19 Cases were detected
print(df['date_report'].value_counts().nlargest(3))


#Calculate Number of Male Infectors and sort them by Month
Monthly_Only_Male = df[~df['sex'].isin(['Female'])]
Monthly_Only_Male = Monthly_Only_Male.groupby(Monthly_Only_Male['date_report'].dt.strftime('%B'))['date_report'].                        count().reset_index(name='Total_cases_by_Month_Male').                        sort_values(['Total_cases_by_Month_Male'],ascending = False,ignore_index=True)

#Calculate Number of Female Infectors and sort them by Month
Monthly_Only_Female = df[~df['sex'].isin(['Male'])]
Monthly_Only_Female = Monthly_Only_Female.groupby(Monthly_Only_Female['date_report'].dt.strftime('%B'))['date_report'].                        count().reset_index(name='Total_cases_by_Month_Female').                        sort_values(['Total_cases_by_Month_Female'],ascending = False,ignore_index=True)
#Plot Graph
N = 3
menMeans = list(Monthly_Only_Male['Total_cases_by_Month_Male'])
womenMeans = list(Monthly_Only_Female['Total_cases_by_Month_Female'])
ind = np.arange(N) # the x locations for the groups
width = 0.35
fig = plt.figure()
axises = fig.add_axes([0,0,1,1])
axises.bar(ind, menMeans, width, color='r')
axises.bar(ind, womenMeans, width,bottom=menMeans, color='b')
axises.set_ylabel('Number of Men and Women Infected')
axises.set_title('Categorized by Month and Gender')
axises.set_xticks([0,1,2])
axises.set_xticklabels(['April','March','February'])
axises.set_yticks(np.arange(0, 400, 40))
axises.legend(labels=['Men', 'Women'])
plt.show()
print(Monthly_Only_Female)
print(Monthly_Only_Male)
