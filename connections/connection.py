# -*- coding: utf-8 -*-
import requests
import queue
class Connection:
    _end = ''

    def _set_url(self, url):
        user_agent = {'User-agent': 'Mozilla/5.0'}
        self._end = requests.get(url, headers=user_agent, timeout=123)

        if self._end.status_code != 200:
            print(" =[ ")

    def _get_url(self):
        return self._end.text

    ref = property(fget=_get_url, fset=_set_url)
