# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data = pd.read_csv(path)

#Code starts here
data.rename(columns={'Total':'Total_Medals'}, inplace=True)
data.head(10)


# --------------
#Code starts here
data['Better_Event'] = np.where(data['Total_Summer']>data['Total_Winter'], 'Summer', 
         (np.where(data['Total_Summer'] < data['Total_Winter'], 'Winter', 'Both')))

better_event = data['Better_Event'].value_counts().index[0]

better_event


# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]

top_countries.drop(data.tail(1).index,inplace=True)

def top_ten(top_countries , column):
    country_list = []
    df_new = top_countries.nlargest(10, column)
    country_list = list(df_new['Country_Name'])
    return country_list

top_10_summer = top_ten(top_countries , 'Total_Summer')
top_10_winter = top_ten(top_countries , 'Total_Winter')
top_10 = top_ten(top_countries , 'Total_Medals')

common = [ x for x in ((set(top_10_summer) & set(top_10_winter) )& set(top_10))]

print(common)


# --------------
#Code starts here

summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

summer_df.groupby(['Country_Name', 'Total_Summer']).size().unstack().plot(kind='bar', stacked=True, figsize=(15,10))
# Label X-axes and Y-axes
plt.xlabel('Country_Name')
plt.ylabel('Total_Summer')
# Display plot
plt.show()

winter_df.groupby(['Country_Name', 'Total_Winter']).size().unstack().plot(kind='bar', stacked=True, figsize=(15,10))
# Label X-axes and Y-axes
plt.xlabel('Country_Name')
plt.ylabel('Total_Winter')
# Display plot
plt.show()

top_df.groupby(['Country_Name', 'Total_Medals']).size().unstack().plot(kind='bar', stacked=True, figsize=(15,10))
# Label X-axes and Y-axes
plt.xlabel('Country_Name')
plt.ylabel('Total_Medals')
# Display plot
plt.show()


# --------------
#Code starts here
summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer'] 
summer_max_ratio=max(summer_df['Golden_Ratio']) 
summer_country_gold=summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']

print("summer_max_ratio =",summer_max_ratio)
print("summer_country_gold =",summer_country_gold)

winter_df['Golden_Ratio'] = winter_df['Gold_Winter'] / winter_df['Total_Winter']

winter_max_ratio = max(winter_df['Golden_Ratio'])
winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']

print("winter_max_ratio =",winter_max_ratio)
print("winter_country_gold =",winter_country_gold)

top_df['Golden_Ratio'] = top_df['Gold_Total'] / top_df['Total_Medals']

top_max_ratio = max(top_df['Golden_Ratio'])
top_country_gold = top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']

print("top_max_ratio =",top_max_ratio)
print("top_country_gold =",top_country_gold)




# --------------
#Code starts here
data_1 = data[:-1]

data_1['Total_Points'] = (data_1['Gold_Total']*3) + (data_1['Silver_Total']*2) + (data_1['Bronze_Total'])

most_points = max(data_1['Total_Points'])
best_country = data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']

print("most_points =",most_points)
print("best_country =",best_country)


# --------------
#Code starts here

#most_points = max(data_1['Total_Points'])
#best_country = data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']

best = data[data['Country_Name']==best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
fig, (ax_1, ax_2) = plt.subplots(1,2, figsize=(20,10))
best.plot(kind='bar', stacked=True, ax=ax_1)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.show()


