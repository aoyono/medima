from toapi import Item, XPath


class Detail(Item):
    __base_url__ = 'https://medicament.ma/medicament'

    field = XPath('//td[@class="field"]')
    value = XPath('//td[@class="value"]')

    class Meta:
        source = XPath('//div[@class="single single-medicament"]//table//tr')
        route = {
            '/detail/:slug': '/:slug'
        }

    def clean_field(self, field):
        return field.split(':')[0].rstrip()
