import re

from toapi import Item, XPath


class SearchResult(Item):
    __base_url__ = 'https://medicament.ma'
    slug = XPath('//td/a/@href')
    nom = XPath('//td/a/span[@class="details"]/text()')
    type = XPath('//td/a/span[@class="details"]/text()')
    format = XPath('//td/a/span[@class="details"]/span[@class="small"]/text()')

    class Meta:
        source = XPath('//div[@class="search-results"]//table/tbody/tr')
        route = {
            '/search/?q=:query&c=:choice&k=:keyword': ('/?s=:query&choice=:choi'
                                                       'ce&keyword=:keyword')
        }

    def clean_slug(self, urls):
        for url in urls:
            if re.match('^{}/medicament/'.format(self.__base_url__), url):
                return url.rstrip('/').split('/')[-1]

    def clean_nom(self, nom):
        return nom[0].strip().split(',')[0].strip()

    def clean_type(self, type):
        return type[0].strip().split(',')[1].strip()
