# -*- coding: utf-8 -*-
from django.dispatch import Signal


# pre detail

pre_get_detail = Signal(
    providing_args=["resource", "request"],
    use_caching=True
)
pre_put_detail = Signal(
    providing_args=["resource", "request"],
    use_caching=True
)
pre_post_detail = Signal(
    providing_args=["resource", "request"],
    use_caching=True
)
pre_delete_detail = Signal(
    providing_args=["resource", "request"],
    use_caching=True
)


# pre list

pre_get_list = Signal(
    providing_args=["resource", "request"],
    use_caching=True
)
pre_put_list = Signal(
    providing_args=["resource", "request"],
    use_caching=True
)
pre_post_list = Signal(
    providing_args=["resource", "request"],
    use_caching=True
)
pre_delete_list = Signal(
    providing_args=["resource", "request"],
    use_caching=True
)


# post detail

post_get_detail = Signal(
    providing_args=["resource", "request"],
    use_caching=True
)

post_put_detail = Signal(
    providing_args=["resource", "request"],
    use_caching=True
)

post_post_detail = Signal(
    providing_args=["resource", "request"],
    use_caching=True
)

post_delete_detail = Signal(
    providing_args=["resource", "request"],
    use_caching=True
)

# post list

post_get_list = Signal(
    providing_args=["resource", "request"],
    use_caching=True
)

post_put_list = Signal(
    providing_args=["resource", "request"],
    use_caching=True
)

post_post_list = Signal(
    providing_args=["resource", "request"],
    use_caching=True
)

post_delete_list = Signal(
    providing_args=["resource", "request"],
    use_caching=True
)
