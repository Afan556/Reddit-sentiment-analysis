# 🧠 Mental Health Insights from Reddit

This project analyzes Reddit posts from mental health-related subreddits such as `r/depression` to uncover emotional trends, keyword themes, and shifts in sentiment over time using natural language processing (NLP) techniques. The insights are visualized to help identify patterns in mental distress, positivity, and support-seeking behavior.

---

## 📌 Project Objectives

- 🗣️ Analyze user-generated posts on mental health topics
- 📊 Perform sentiment analysis using VADER
- ⏳ Track emotional trends over time
- 🔍 Identify common keywords and dominant emotional themes
- 🧠 Apply topic modeling to uncover hidden topics in conversations

---

## 🗂️ Dataset

- **Source**: Scraped directly from Reddit using the `PRAW` API
- **Subreddit**: `r/depression` (expandable to others like `r/anxiety`, `r/mentalhealth`)
- **Features Collected**:
  - `title`, `selftext`, `created_utc`
  - `score`, `num_comments`
  - Derived features: `text`, `sentiment_score`, `sentiment_label`, `date`

---

## 🔬 Tools & Technologies

| Purpose                | Stack                                   |
|------------------------|-----------------------------------------|
| Data Collection        | Python, PRAW (Reddit API)               |
| Text Processing        | NLTK, re, pandas                        |
| Sentiment Analysis     | VADER (from nltk.sentiment.vader)       |
| Visualization          | Seaborn, Matplotlib                     |
| Topic Modeling         | Gensim (LDA), spaCy (optional)          |
| Dashboard (optional)   | Power BI or Streamlit                   |

---

## 🧪 NLP Tasks Performed

1. **Preprocessing**:
   - Cleaning text (punctuation, case, stopwords)
   - Combining title and body for full context

2. **Sentiment Analysis**:
   - VADER applied to compute compound score
   - Labeling posts as `Positive`, `Negative`, or `Neutral`

3. **Trend Analysis**:
   - Sentiment scores averaged per day
   - Trends visualized over time to track mental health shifts

4. **Keyword & Topic Mining**:
   - Most common keywords per sentiment label
   - Topic modeling with LDA to discover hidden themes

---

## 📊 Key Visualizations

- 📈 Sentiment trend line (daily)
- 📊 Top emotional keywords per sentiment
- ☁️ Word clouds by label
- 🔥 Topic frequency over time
- 🗓️ Weekly emotional activity heatmap (optional)

---

## 🧠 Insights Uncovered

- Peaks in negative sentiment around weekends and holidays
- Therapy and progress-related posts were generally positive
- Distress-heavy topics like isolation, insomnia, and family conflict dominated negative clusters
- Engagement (comments/upvotes) correlated with emotional depth

---

## 📁 Project Structure

