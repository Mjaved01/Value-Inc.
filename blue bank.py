import json
import pandas as pd
import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt


#method 1 to read json data
json_file=open('loan_data_json.json')
data= json.load(json_file)

#method 2 to read json data
with open('loan_data_json.json') as json_file:
   data=json.load(json_file)
   
#transform to data frame
loan_data= pd.DataFrame(data)

#finding unique values for purpose column
loan_data['purpose'].unique()

#describe the data
loan_data.describe()

#decribe specific column
loan_data['int.rate'].describe()
loan_data['fico'].describe()
loan_data['dti'].describe()

#using EXP to get annual income
income=np.exp(loan_data['log.annual.inc'])
loan_data['AnnualIncome']=income

fico=200

# fico >= 300 and < 400: 'Very Poor'
# fico >= 400 and ficoscore < 600: 'Poor'
# fico >= 601 and ficoscore < 660: 'Fair'
# fico >= 660 and ficoscore < 780: 'Good'
# fico >=780: 'Excellent

if fico>= 300 and fico <400:
    ficocat= 'very poor'
elif fico >= 400 and fico < 600: 
    ficocat='Poor'
elif fico >= 601 and fico < 660: 
    ficocat='Fair'
elif fico >= 660 and fico < 780: 
    ficocat='Good'
elif fico >=780: 
    ficocat= 'Excellent'
else:
    ficocat='unknown'
print(ficocat)
 
length=len(loan_data)
ficocat=[]
loan_data['fico']
for x in range(0,length):
    category=loan_data['fico'][x]
    try:
        
        if category>= 300 and category <400:
            cat= 'very poor'
        elif category>= 400 and category <600:
                cat= 'poor'
        elif category>= 601 and category <660:
            cat= 'fair'
        elif category>= 660 and category <780:
            cat= 'good'
        elif category>=780:
            cat= 'excellent'
        else:
            cat= 'unknown'
    except:
        cat='Unknown'
    ficocat.append(cat)

ficocat= pd.Series(ficocat)

loan_data['Fico.Category']= ficocat

#for unterest rates new data column  = rate> 0.12 high else low
loan_data.loc[loan_data['int.rate'] >0.12, 'int. rate.type']= 'High'
loan_data.loc[loan_data['int.rate'] <= 0.12, 'int. rate.type']= 'Low'
 
#no. of loans/rows by fico category
catplot=loan_data.groupby(['Fico.Category']).size()
catplot.plot.bar(color='green', width= 0.1)
plt.show()

catplot=loan_data.groupby(['purpose']).size()
catplot=loan_data.groupby(['purpose']).size()
catplot.plot.bar(color='red')
plt.show()

#scatter plots
ypoint= loan_data['AnnualIncome']
xpoint= loan_data['dti']
plt.scatter(xpoint, ypoint)
plt.show()

#writing to csv
loan_data.to_csv('loan_data_cleaned.csv', index=True)










































 








