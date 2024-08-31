from flask import Flask, render_template
import feedparser

app = Flask(__name__)

@app.route('/')
def index():
    # Path to the local RSS feed file
    rss_url = 'aggregated_forex_feed.xml'

    # Parse the RSS feed
    feed = feedparser.parse(rss_url)

    # Extract the news items
    news_items = [{'title': entry.title, 'link': entry.link, 'published': entry.published} for entry in feed.entries]

    # Render the HTML template
    return render_template('index.html', news_items=news_items)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
