# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path)
p_a = df[df['fico'].astype(float)>700].shape[0]/df.shape[0]
print(p_a)

p_b = df[df['purpose']== 'debt_consolidation'].shape[0]/df.shape[0]
print(p_b)

df1 = df[df['purpose'] == 'debt_consolidation']

p_a_b = df1[df1['fico'].astype(float) > 700].shape[0]/df1.shape[0]
print(p_a_b)

result = (p_a == p_a_b)
print(result)
# code ends here


# --------------
# probability of paid_back_loan is Yes
prob_lp = df[df['paid.back.loan'] == 'Yes'].shape[0] / df.shape[0]
print(prob_lp)

# probability of the credit policy is Yes
prob_cs = df[df['credit.policy'] == 'Yes'].shape[0]  / df.shape[0]
print(prob_cs)
# create new dataframe for paid.back.loan == 'Yes'
new_df = df[df['paid.back.loan'] == 'Yes']

# Calculate the P(B|A)
prob_pd_cs = new_df[new_df['credit.policy'] == 'Yes'].shape[0] / new_df.shape[0]

print(prob_pd_cs)

# bayes theorem 

bayes = (prob_pd_cs * prob_lp)/ prob_cs

# print bayes
print(bayes)


# --------------
# code starts here
df.purpose.value_counts(normalize=True).plot(kind='bar')
plt.title("Probability Distribution of Purpose")
plt.ylabel("Probability")
plt.xlabel("Number of Purpose")
plt.show()

#create new dataframe for paid.back.loan == 'No'
df1= df[df['paid.back.loan'] == 'No']

# plot the bar plot for 'purpose' where paid.back.loan == No 
df1.purpose.value_counts(normalize=True).plot(kind='bar')
plt.title("Probability Distribution of Purpose")
plt.ylabel("Probability")
plt.xlabel("Number of Purpose")
plt.show()


# code ends here


# --------------
# code starts here
inst_median = df['installment'].median()
inst_mean = df['installment'].mean()
df['installment'].hist(normed =True , bins = 50)
df['log.annual.inc'].hist(normed = True , bins = 50)


# code ends here


