#this script is used to visualize the results of the model
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import Scraped as sc 
import datetime as dt

#what function in Pandas will help me group by date and average Sentimen_scores
sc.df['date']=pd.to_datetime(sc.df['created_utc'], unit='s')
sc.df['avg_sentiment_scores']=sc.df['Sentimen_scores'].groupby(sc.df['date']).transform('mean')
# Group by date and calculate the average sentiment scores
grouped_df = sc.df.groupby('date')['Sentimen_scores'].mean().reset_index()

sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))
sns.lineplot(data=grouped_df, x='date', y='Sentimen_scores', marker='o')
plt.title('Average Daily Sentiment Score Over Time')
plt.xlabel('Date')
plt.ylabel('Average Sentiment Score')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
