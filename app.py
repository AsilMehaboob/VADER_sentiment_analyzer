from flask import Flask, render_template, request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    analyzer = SentimentIntensityAnalyzer()
    sentiment_dict = analyzer.polarity_scores(text)
    sentiment = "Neutral"
    if sentiment_dict['compound'] >= 0.05:
        sentiment = "Positive"
    elif sentiment_dict['compound'] <= -0.05:
        sentiment = "Negative"
    return render_template('index.html', text=text, sentiment=sentiment, scores=sentiment_dict)

if __name__ == '__main__':
    app.run(debug=True)
