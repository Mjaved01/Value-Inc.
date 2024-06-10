import pandas as pd

# file name= pd.read_csv('file.csv')<----- format of file read.csv
data = pd.read_csv('transaction2.csv') 
data = pd.read_csv('transaction2.csv', sep= ';') 
#summary of data
data.info() 

#working with calculations 

#defining calculations 
CostPerItem=11.73
SellingPricePerItem=21.11
NoofItemsPurchased=6

#Mathematical operations

profitperitem= SellingPricePerItem - CostPerItem

profitpertransaction= profitperitem * NoofItemsPurchased
costpertransaction= CostPerItem*NoofItemsPurchased
sellingpricepertransaction= SellingPricePerItem*NoofItemsPurchased

#column calculatiuons
#variable = dataframe('variable')
costperitem = data['CostPerItem']
sellingpriceperitem = data ['SellingPricePerItem']
noofitemspurchased = data['NumberOfItemsPurchased']

profitpertransaction= costpertransaction*noofitemspurchased
costpertransaction= costperitem*noofitemspurchased
sellingpricepertransaction= sellingpriceperitem*noofitemspurchased

#adding new column to the data
data['CostPerTransaction']= data['CostPerItem']*data['NumberOfItemsPurchased']

#SalesPerTransaction
data['SalesPerTransaction']=data ['SellingPricePerItem']*data['NumberOfItemsPurchased']
#profit per tansaction
data['ProfitPerTransaction']=data['SalesPerTransaction']-data['CostPerTransaction']
#markup 
data['Markup']=(data['SalesPerTransaction']-data['CostPerTransaction']) /data['CostPerTransaction']

#roundingmarkup
roundmarkup= round (data['Markup'],2)

#combining columns in data
#step 1 check the data type
print(data['Day'].dtype)
print(data['Year'].dtype)
print(data['Month'].dtype)
print(data['Time'].dtype)

#step 2 change the data type
day=data['Day'].astype(str)
year=data['Year'].astype(str)
print(day.dtype)
print(year.dtype)

#combining columns in 1
my_date=day+'-'+data['Month']+'-'+year

#adding column to data
data['Date']=my_date

#using iloc to view data
data.iloc[0] #views the row with index=0
data.iloc[0:4] #first 3 rows
data.iloc[-5:] #last five rows
data.head(5) #brings in first five rows
data.iloc[:,2] #brings in single column and all rows
data.iloc[4,2] #brings in specific row and column

#spliting columns
#new_var=column.str.split ('sep', expand=True)

split_col=data['ClientKeywords'].str.split(',', expand=True)

#creating new columns for client key words in data
data['ClientAge']= split_col[0]
data['ClientType']= split_col[1]
data['LengthofContract']=split_col[2]

#using lower case function

data.info()
data['ItemDescription']=data['ItemDescription'].str.capitalize()

#using replace function
data['ClientAge']=data['ClientAge'].str.replace('[','')
data['LengthofContract']=data['LengthofContract'].str.replace(']','')

#merging to data sources 

#brining in new data set
seasons=pd.read_csv('value_inc_seasons.csv', sep=';')
#merging files merge_df= pd.merge[old_df,new_df, on=key]
data=pd.merge(data, seasons, on='Month') 

#dropping columns
#df=df.drop(columnname, axis=1) <-----1 for column and 0 for row
#dropping multiple columns at once 
#data=data.drop(['columnname','columnname','columnname'], axis=1)

#export into csv.
data.to_csv('ValueInc_Cleaned.csv', index= False)
# if want to keep the index then index = True



