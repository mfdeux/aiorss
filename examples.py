import asyncio

from aiorss import RSSFeed

nyt_rss = 'http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'
various_rss = ['http://rss.nytimes.com/services/xml/rss/nyt/Technology.xml',
               'http://feeds.reuters.com/reuters/businessNews', 'http://feeds.abcnews.com/abcnews/topstories',
               'http://rss.cnn.com/rss/cnn_topstories.rss',
               'https://news.google.com/news/rss/headlines/section/topic/WORLD?ned=us&hl=en&gl=US',
               'http://feeds.bbci.co.uk/news/world/rss.xml', 'https://www.theguardian.com/world/rss']


async def one_feed():
    feed = RSSFeed(nyt_rss)
    return await feed.parse()


async def many_feeds():
    feeds = [RSSFeed(url) for url in various_rss]
    return await asyncio.gather(*[feed.parse() for feed in feeds])


loop = asyncio.get_event_loop()

task1 = loop.create_task(one_feed())
task2 = loop.create_task(many_feeds())
print(loop.run_until_complete(task1))
print(loop.run_until_complete(task2))
