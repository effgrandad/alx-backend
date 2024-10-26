#!/usr/bin/env python3

'''
This module includes a portion of the basic
pagination assistance function.
'''

from typing import Tuple

return_type = Tuple[int, int]


def index_range(page: int, page_size: int) -> return_type:
    '''
    The Actuall helper function
    Args:
        page (int):
        page_size (int):
    Returns:
        Returns an tupple of ints
    '''
    if isinstance(page, int) and isinstance(page_size, int):
        return ((page - 1) * page_size, page_size * page)
    raise TypeError('Expected `page` and `page_size` to be ints')
