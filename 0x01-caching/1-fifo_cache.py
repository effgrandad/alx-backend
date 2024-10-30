#!/usr/bin/env python3


"""
This module demonstrates simple caching in Python.
This time, we'll do FIFO caching.
When the cache reaches its maximum capacity,
we remove the first item and add the next one (FIFO)
"""

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    '''
    A minimal basic implementation of cache system
    Based on a FIFO list
    '''

    def __init__(self):
        '''
        The constructor
        '''
        super().__init__()

    def put(self, key, item):
        '''
        Add an item to the cache
        Args:
            key (str): the key for the cache
            item (str): the value to se
        Returns:
        Returns None (explicitly)
        '''
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data.keys()) > super().MAX_ITEMS:
                last_key = list(self.cache_data.keys())[0]
                self.cache_data.pop(last_key)
                print(f'DISCARD: {last_key}')

    def get(self, key):
        '''
        Let's get the cache item by the key
        Args:
            key (str): Key to the item
        Returns:
            if key in self.cached_items, return the
            item, None otherwise
        '''
        return self.cache_data.get(key)
