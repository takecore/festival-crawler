# -*- coding: utf-8 -*-

import scrapy
from scrapy.loader import ItemLoader

from scraping.items import FestivalItem

class FestivalItemLoader(ItemLoader):
    default_item_class = FestivalItem

    def set_load_items(self) -> None:
        s: str = '.rl_header .summary'
        self.add_css('name', s)
        s = '.rl_main .dtstart::text'
        self.add_css('term_text', s)
        s = '.rl_main .rl_shop .rl_shop_access'
        self.add_css('stations', s)
