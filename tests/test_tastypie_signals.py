#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_tastypie_signals
----------------------------------

Tests for `tastypie_signals` module.
"""

import unittest
from tastypie_signals import post_put_detail


class TestSignals(unittest.TestCase):

    resource = object()
    request = object()

    @staticmethod
    def signal_handler(signal, sender, resource, request):
        assert signal == post_put_detail
        assert sender == TestSignals
        assert resource == TestSignals.resource
        assert request == TestSignals.request

    def setUp(self):
        post_put_detail.connect(
            self.signal_handler,
            sender=TestSignals
        )

    def test_signal(self):
        post_put_detail.send(
            sender=self.__class__,
            resource=self.resource,
            request=self.request
        )

if __name__ == '__main__':
    unittest.main()
