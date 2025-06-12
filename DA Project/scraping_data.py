import praw
import re
import pandas as pd
# This script uses the PRAW library to connect to Reddit and fetch posts from the 'depression' subreddit.
reddit= praw.Reddit(client_id='MB90kG-j6AEu4K0gUXhp9Q',
                     client_secret='V_oxv8D3HwnoqMizGPP3GrdSj1oufA',
                     user_agent='Mental Health Scraping')
reddit=reddit.subreddit('depression')
data=[]
for post in reddit.hot(limit=100):
    data.append({
        'id': post.id,
        'title': post.title,
        'selftext': post.selftext,
        'created_utc': post.created_utc,
        'subreddit': post.subreddit.display_name,
        'score': post.score,
        'num_comments': post.num_comments
    })
df=pd.DataFrame(data)
df['created_datetime'] = pd.to_datetime(df['created_utc'], unit='s')
df['day']= df['created_datetime'].dt.day
df['month']= df['created_datetime'].dt.month
df['year']  = df['created_datetime'].dt.year
df['weekday']  = df['created_datetime'].dt.weekday
df['date']= df['created_datetime'].dt.date
df['text']=df['title'].fillna('')+ ' ' + df['selftext'].fillna('')

def clean_text(text):
    text = re.sub(r'http\S+', '', text)            
    text = re.sub(r'[^a-zA-Z\s]', '', text)        
    text = text.lower()                            
    return text

df['clean_text'] = df['text'].apply(clean_text)