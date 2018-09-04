import asyncio

import feedparser

from .exceptions import (UnableToParseFeedError)
from .http_client import HTTPClient
from typing import Dict, Any

headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}

DEFAULT_USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
VALIDATION_LEVELS = ('STRICT', 'DROP', 'ALLOW')


def parse_date(date_str):
    from dateutil.parser import parse
    parsed_date = parse(date_str)
    return parsed_date.isoformat()


class RSSFeed(object):
    """
    RSSFeed
    """

    def __init__(self,
                 url: str,
                 user_agent: str = DEFAULT_USER_AGENT,
                 proxy: str = None,
                 loop: asyncio.AbstractEventLoop = None):
        """
        Args:
            user_agent:
            proxy:
            validation:
            loop:
        """
        self.url = url
        if loop:
            self.loop = loop
        else:
            self.loop = asyncio.get_event_loop()
        self.user_agent = user_agent
        self.http_client = HTTPClient(
            user_agent=user_agent, headers=headers, proxy=proxy)

    async def parse(self,
                   query_params: Dict[str, Any] = None,
                   headers: Dict[str, Any] = None):
        try:
            resp = await self.http_client.get(
                url=self.url, params=query_params, headers=headers, is_text=True)
        except Exception as error:
            raise

        parsed_feed = await self.loop.run_in_executor(None, self._parse_feed,
                                                      resp)
        return parsed_feed

    def _parse_feed(self, xml: str):
        """
        Parse XML feed
        """
        parsed_feed = feedparser.parse(xml)
        if parsed_feed.bozo:
            raise UnableToParseFeedError('Unable to parse feed')
        return parsed_feed
