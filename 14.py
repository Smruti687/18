import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

data = [
    {"Text": "Beautiful day park", "Sentiment": "Positive"},
    {"Text": "Traffic terrible", "Sentiment": "Negative"},
    {"Text": "Amazing workout", "Sentiment": "Positive"},
    {"Text": "Excited weekend trip", "Sentiment": "Positive"},
    {"Text": "Trying new recipe", "Sentiment": "Neutral"},
    {"Text": "Feeling grateful", "Sentiment": "Positive"},
    {"Text": "Rainy cozy day", "Sentiment": "Positive"},
    {"Text": "Movie must watch", "Sentiment": "Positive"},
    {"Text": "Political debate", "Sentiment": "Negative"},
    {"Text": "Missing beach", "Sentiment": "Neutral"},
    {"Text": "New blog post", "Sentiment": "Positive"},
    {"Text": "Feeling sick", "Sentiment": "Negative"},
    {"Text": "Explore city", "Sentiment": "Positive"},
    {"Text": "Fitness goals", "Sentiment": "Positive"},
    {"Text": "Tech changing life", "Sentiment": "Neutral"},
    {"Text": "Reflecting past", "Sentiment": "Positive"},
    {"Text": "Adopted pet", "Sentiment": "Positive"},
    {"Text": "Gaming friends", "Sentiment": "Positive"},
    {"Text": "AI conference", "Sentiment": "Neutral"},
    {"Text": "Winter blues", "Sentiment": "Negative"}
]

df = pd.DataFrame(data)

# WordCloud function
def show_cloud(text, title):
    wc = WordCloud(background_color='white').generate(text)
    plt.imshow(wc)
    plt.axis("off")
    plt.title(title)
    plt.show()

# Generate clouds
positive_text = " ".join(df[df['Sentiment']=='Positive'].Text)
negative_text = " ".join(df[df['Sentiment']=='Negative'].Text)
neutral_text  = " ".join(df[df['Sentiment']=='Neutral'].Text)

show_cloud(positive_text, "Positive")
show_cloud(negative_text, "Negative")
show_cloud(neutral_text, "Neutral")