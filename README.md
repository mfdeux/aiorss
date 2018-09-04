# aiorss

Asyncio client for interacting with rss feeds

Installation instructions:

```bash
pip install aiorss
```

Usage:
```python
from aiorss import RSSFeed

async def main():
	url = 'http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'
	feed = RSSFeed(url)
	return await feed.parse()

```

Note
---------
aiorss is not affiliated or endorsed by any of the web services it interacts with.

