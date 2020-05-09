# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)
data['Gender'].replace('-','Agender',inplace = True)
print(data)
gender_count = data['Gender'].value_counts()

#Code starts here 




# --------------
#Code starts here
alignment = data['Alignment'].value_counts()
plt.pie(alignment)


# --------------
#Code starts here
sc_df = data[['Strength','Combat']].copy()
sc_covariance = sc_df.cov().iloc[0,1]
sc_strength = data['Strength'].std()
sc_combat = data['Combat'].std()

sc_pearson = sc_covariance/(sc_strength*sc_combat)


ic_df = data[['Intelligence','Combat']]
ic_covariance = ic_df.cov().iloc[0,1]
ic_intelligence = data['Intelligence'].std()
ic_combat = data['Combat'].std()


ic_pearson = ic_covariance/(ic_intelligence*ic_combat)


# --------------
#Code starts here

total_high = data['Total'].quantile(q=0.99)
super_best = data[data['Total'] > total_high]
super_best_names = list(super_best['Name'])
print(super_best_names)


# --------------
#Code starts here
fig,(ax_1,ax_2,ax_3) = plt.subplots(1,3,figsize=(20,8))
ax_1.boxplot(super_best['Intelligence'])
ax_1.set(title = 'Intelligence')

ax_2.boxplot(super_best['Speed'])
ax_1.set(title = 'Speed')

ax_3.boxplot(super_best['Power'])
ax_1.set(title = 'Power')


