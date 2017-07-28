# -*- coding: utf-8 -*-

import scrapy
from scrapy.loader.processors import (
    Identity,
    MapCompose,
    TakeFirst,
)
from w3lib.html import remove_tags, strip_html5_whitespace


class FestivalItem(scrapy.Item):
    name = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst(),
    )
    term_text = scrapy.Field(
        input_processor=MapCompose(remove_tags, strip_html5_whitespace),
        output_processor=TakeFirst(),
    )
    stations = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=Identity(),
    )
