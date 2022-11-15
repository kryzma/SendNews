from abc import ABC, abstractmethod
from typing import List
import xml.etree.ElementTree as ET

import schema

import requests


class RssRepo(ABC):

    @abstractmethod
    def get_posts_from_urls(self, urls: List[str]) -> List[schema.Post]:
        pass


class RssRepoImpl(RssRepo):

    def get_posts_from_urls(self, urls: List[str]) -> List[schema.Post]:
        '''
        gets rss feed from urls and sends back formed posts
        '''
        result: List[schema.Post] = []
        for url in urls:
            result = self.__add_posts_from_url(result, url)
        return result

    def __add_posts_from_url(self, posts: List[schema.Post], url: str) -> List[schema.Post]:
        '''
        gets rss feed from url and sends back formed posts
        '''
        rss_bytes = requests.get(url)
        rss_string = rss_bytes.content.decode("utf-8")
        return self.__posts_from_rss_string(rss_string, posts, url)

    @staticmethod
    def __posts_from_rss_string(rss_string: str, posts: List[schema.Post], source: str) -> List[schema.Post]:
        '''
        Fills posts list with new posts which are parsed from rss_string
        '''
        rss_root = ET.fromstring(rss_string)
        rss_posts = list(rss_root.iter("item"))
        for rss_post in rss_posts:
            assert rss_post.find("title") is not None
            title = rss_post.find("title").text
            description = rss_post.find("description").text
            source = source
            link = rss_post.find("link").text
            posts.append(schema.Post(title, description, source, link))

        return posts
