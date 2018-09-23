import sys
import time
from multiprocessing import Process

import requests

from app import api


def client(query, choice, keyword):
    search_url = 'http://localhost:10000/search/?q={}&c={}&k={}'.format(
        query,
        choice,
        keyword
    )
    details_base_url = 'http://localhost:10000/detail'
    response = requests.get(search_url)
    try:
        response.raise_for_status()
    except requests.HTTPError:
        print('ERROR')
    else:
        search_results = response.json()['SearchResult']
        for sr in search_results:
            print('getting details for {}'.format(sr['nom']))
            detailed_resp = requests.get(
                details_base_url + '/{}'.format(sr['slug'])
            )
            details = detailed_resp.json()['Detail']
            log_msg_format = '{}: {}'
            for detail in details:
                print(
                    log_msg_format.format(detail['field'], detail['value'])
                )


if __name__ == '__main__':
    server_process = Process(target=api.serve, kwargs={'port': 10000})
    server_process.start()
    time.sleep(5)
    client_process = Process(target=client, args=sys.argv[1:])
    client_process.start()
    try:
        client_process.join()
        server_process.terminate()
    except KeyboardInterrupt:
        pass
