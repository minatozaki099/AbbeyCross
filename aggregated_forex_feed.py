import feedparser
from feedgen.feed import FeedGenerator
import requests
from bs4 import BeautifulSoup  # This import is not needed for the current code but is fine if you plan to use it later

# Function to parse a standard RSS feed
def parse_rss_feed(url):
    feed = feedparser.parse(url)
    return [{'title': entry.title, 'link': entry.link, 'published': entry.published} for entry in feed.entries]

# Function to get Twitter content (requires TwitRSS.me or similar service)
def parse_twitter_feed(twitter_handle):
    twitter_rss_url = f'https://twitrss.me/twitter_user_to_rss/?user={twitter_handle}'
    return parse_rss_feed(twitter_rss_url)

# Function to get Reddit content
def parse_reddit_feed(subreddit):
    reddit_rss_url = f'https://www.reddit.com/r/{subreddit}/.rss'
    return parse_rss_feed(reddit_rss_url)

# Combine multiple feeds
def combine_feeds():
    fg = FeedGenerator()
    fg.title('Aggregated Forex News and Social Media Opinions')
    fg.link(href='http://yourwebsite.com', rel='alternate')
    fg.description('A custom RSS feed aggregating Forex news and social media opinions.')

    # Forex news feeds
    forex_feeds = [
        'https://www.dailyfx.com/feeds/trading-news-analysis',
        'https://www.forexfactory.com/ffcal_week_this.xml',
        'https://www.fxstreet.com/rss'
    ]

    for url in forex_feeds:
        for entry in parse_rss_feed(url):
            fe = fg.add_entry()
            fe.title(entry['title'])
            fe.link(href=entry['link'])
            fe.pubDate(entry['published'])

    # Twitter opinions (example Twitter handles)
    twitter_handles = ['forex', 'FXStreetNews']

    for handle in twitter_handles:
        for entry in parse_twitter_feed(handle):
            fe = fg.add_entry()
            fe.title(entry['title'])
            fe.link(href=entry['link'])
            fe.pubDate(entry['published'])

    # Reddit opinions (example subreddits)
    subreddits = ['Forex', 'ForexTrading']

    for subreddit in subreddits:
        for entry in parse_reddit_feed(subreddit):
            fe = fg.add_entry()
            fe.title(entry['title'])
            fe.link(href=entry['link'])
            fe.pubDate(entry['published'])

    # Generate the RSS feed XML
    rss_feed = fg.rss_str(pretty=True)
    return rss_feed.decode('utf-8')  # Decode bytes to string

# Save RSS feed to a file
rss_feed = combine_feeds()
with open('aggregated_forex_feed.xml', 'w', encoding='utf-8') as f:
    f.write(rss_feed)  # Write the string directly

print("RSS feed generated and saved as 'aggregated_forex_feed.xml'")
