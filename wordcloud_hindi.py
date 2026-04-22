import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# -----------------------------
# Marathi Dataset
# -----------------------------
data = [
    {"Text": "सुंदर दिन पार्क में", "Sentiment": "Positive"},
    {"Text": "आज बहुत ट्रैफिक था", "Sentiment": "Negative"},
    {"Text": "अच्छा वर्कआउट किया", "Sentiment": "Positive"},
    {"Text": "वीकेंड ट्रिप का इंतजार", "Sentiment": "Positive"},
    {"Text": "नई रेसिपी ट्राई की", "Sentiment": "Neutral"},
    {"Text": "मैं बहुत खुश हूँ", "Sentiment": "Positive"},
    {"Text": "बारिश का मजा लिया", "Sentiment": "Positive"},
    {"Text": "फिल्म बहुत अच्छी थी", "Sentiment": "Positive"},
    {"Text": "राजनीतिक बहस चल रही है", "Sentiment": "Negative"},
    {"Text": "समुद्र किनारे की यादें", "Sentiment": "Neutral"},
    {"Text": "नई ब्लॉग पोस्ट लिखी", "Sentiment": "Positive"},
    {"Text": "आज तबीयत ठीक नहीं", "Sentiment": "Negative"},
    {"Text": "शहर घूम रहा हूँ", "Sentiment": "Positive"},
    {"Text": "फिटनेस लक्ष्य सेट किया", "Sentiment": "Positive"},
    {"Text": "तकनीक तेजी से बदल रही है", "Sentiment": "Neutral"},
    {"Text": "पुरानी यादों में खो गया", "Sentiment": "Positive"},
    {"Text": "प्यारा पालतू जानवर", "Sentiment": "Positive"},
    {"Text": "दोस्तों के साथ गेम खेला", "Sentiment": "Positive"},
    {"Text": "एआई कॉन्फ्रेंस में हिस्सा लिया", "Sentiment": "Neutral"},
    {"Text": "सर्दी में उदासी महसूस हुई", "Sentiment": "Negative"}
]

df = pd.DataFrame(data)

# -----------------------------
# WordCloud Function
# -----------------------------
def show_cloud(text, title):
    wc = WordCloud(
        font_path = r"C:\Windows\Fonts\Nirmala.ttc",
        background_color='white'
    ).generate(text)

    plt.imshow(wc)
    plt.axis("off")
    plt.title(title)
    plt.show()

# -----------------------------
# Prepare Text
# -----------------------------
positive_text = " ".join(df[df['Sentiment']=='Positive'].Text)
negative_text = " ".join(df[df['Sentiment']=='Negative'].Text)
neutral_text  = " ".join(df[df['Sentiment']=='Neutral'].Text)

# -----------------------------
# Generate Word Clouds
# -----------------------------
show_cloud(positive_text, "Positive")
show_cloud(negative_text, "Negative")
show_cloud(neutral_text, "Neutral")
