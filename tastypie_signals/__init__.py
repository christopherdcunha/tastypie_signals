# -*- coding: utf-8 -*-

__author__ = 'Christopher D\'Cunha'
__email__ = 'me@christopherdcunha.com'
__version__ = '0.1.0'

from .signals import *

__all__ = [
    'pre_get_detail', 'pre_put_detail', 'pre_post_detail', 'pre_delete_detail',
    'pre_get_list', 'pre_put_list', 'pre_post_list', 'pre_delete_list',
    'post_get_detail', 'post_put_detail', 'post_post_detail',
    'post_delete_detail',
    'post_get_list', 'post_put_list', 'post_post_list', 'post_delete_list'
]
