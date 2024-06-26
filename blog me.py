import pandas as pd 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
 #reading excel or xlsx file 
data= pd.read_excel('articles.xlsx')
#summary of the data
data.describe()

#summary of columns
data.info()

#counting no of articles per source
#format of groupby: df.groupby(['column_to_group]['column_to_count])
data.groupby(['source_id'])['article_id'].count()

#no ofreaction by publisher
data.groupby(['source_id'])['engagement_reaction_count'].sum()

#droping a column
data= data.drop('engagement_comment_plugin_count', axis=1)

#creating a keyword flag
#keyword= 'crash'

#loop for isloating title row
# length=len(data)
# keyword_flag=[]
# for x in range(0,length):
#     heading=data['title'][x]
#     if keyword in heading:
#         flag=1
#     else:
#         flag=0
#     keyword_flag.append(flag)
    
#creating a function
def keywordflag(keyword):
    length = len(data)
    keyword_flag = []
    for x in range(length):
        heading = data['title'][x]
        try:
            if keyword in heading:
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
        keyword_flag.append(flag)
    return keyword_flag

# Call the function
keyword_flag = keywordflag('murder')

# Ensure the keyword_flag list matches the index of the DataFrame
data['keywordflag'] = pd.Series(keyword_flag, index=data.index)

print(data)
#SentimentIntensityAnalyzer
sent_int = SentimentIntensityAnalyzer()

text=data ['title'][15]
sent= sent_int.polarity_scores(text)

neg=sent['neg']
pos=sent['pos']
neu=sent['neu']

#adding a for loop to extract sentiment per title
title_neg_sentiment=[]
title_pos_sentiment=[]
title_neu_sentiment=[]

length= len(data)
for x in range (0,length):
    try:
        text=data['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent= sent_int.polarity_scores(text)
        neg=sent['neg']
        pos=sent['pos']
        neu=sent['neu']
    except:
        neg=0
        pos=0
        neu=0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)

ttitle_neg_sentiment= pd.Series(title_neg_sentiment)
ttitle_pos_sentiment= pd.Series(title_pos_sentiment)
ttitle_neu_sentiment= pd.Series(title_neu_sentiment)

data['title_neg_sentiment']=ttitle_neg_sentiment
data['title_pos_sentiment']=ttitle_pos_sentiment
data['title_neu_sentiment']=ttitle_neu_sentiment

#writing the data
data.to_excel('Blogme_cleaned.xlsx', sheet_name= 'Blogmedata', index=False)










