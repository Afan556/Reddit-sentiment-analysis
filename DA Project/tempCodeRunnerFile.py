# This script analyzes the sentiment of Reddit posts related to depression using the VADER sentiment analysis tool.
import pandas as pd
import datetime as dt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as sit

df=pd.read_csv('reddit_depression_postsss.csv', index_col=False)
def sentiment_scores(sentence):
    sid_obj = sit()
    sentiment_dict = sid_obj.polarity_scores(sentence)

    print(f"Sentiment Scores: {sentiment_dict}")
    print(f"Negative Sentiment: {sentiment_dict['neg']*100}%")
    print(f"Neutral Sentiment: {sentiment_dict['neu']*100}%")
    print(f"Positive Sentiment: {sentiment_dict['pos']*100}%")
    
    if sentiment_dict['compound'] >= 0.05:
        print("Overall Sentiment: Positive")
    elif sentiment_dict['compound'] <= -0.05:
        print("Overall Sentiment: Negative")
    else:
        print("Overall Sentiment: Neutral")
if __name__ == "__main__":
    sentiment_scores(df['text'])

df['Sentimen_scores']=df['text'].apply(lambda x: sit.polarity_scores(text=x)['compound'])
df['Sentiment'] = df['Sentimen_scores'].apply(lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral'))
df.to_csv('reddit_depression_posts_with_sentiment.csv', index=False)
print("Sentiment analysis completed and saved to 'reddit_depression_posts_with_sentiment.csv'.")