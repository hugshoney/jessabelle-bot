# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""Plugin to get random quotes"""
import requests
import random


class Quotes:
    """Define word from Urban Dictionary"""
    def __init__(self, number=1):
        self.number = number

    def get_response(self):
        """Get full result and return"""
        url = 'https://type.fit/api/quotes'
        r = requests.get(url)
        response = r.json()

        return response

    def get_quote(self):
        """Get random quote"""
        list_quotes = self.get_response()
        quotes = []
        for _ in range(self.number):
            quotes.append(random.choice(list_quotes))
        return quotes
