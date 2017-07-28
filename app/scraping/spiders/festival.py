# -*- coding: utf-8 -*-

from typing import Generator

import scrapy
from scrapy.http import Request
from scrapy.http.response.html import HtmlResponse

from scraping.itemloaders import FestivalItemLoader


class FestivalSpider(scrapy.Spider):
    name: str = 'festival:august'

    def start_requests(self) -> Generator[Request, None, None]:
        url: str = (
            'http://www.enjoytokyo.jp'
            '/amuse/event/list/cate-94/august/'
        )
        yield Request(url=url, callback=self.parse)

    def parse(
        self,
        response: HtmlResponse,
    ) -> Generator[Request, None, None]:
        for li in response.css('#result_list01 > li'):
            loader = FestivalItemLoader(
                response=response,
                selector=li,
            )
            loader.set_load_items()
            yield loader.load_item()
