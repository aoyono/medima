from toapi import Api

from items.detail import Detail
from items.search_result import SearchResult
from settings import MySettings


api = Api('https://medicament.ma', settings=MySettings)
api.register(SearchResult)
api.register(Detail)

if __name__ == '__main__':
    api.serve(port=10000)
