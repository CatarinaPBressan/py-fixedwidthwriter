# coding: UTF-8
from __future__ import absolute_import

from unittest import TestCase

import six
if six.PY2:
    from StringIO import StringIO
else:
    from io import StringIO

from fixedwidthwriter import FixedWidthWriter


class TestFixedWidthWriter(TestCase):

    def setUp(self):
        self.s = StringIO()
        self.objs = [
            {'ID': 0, 'NAME': 'Jack', 'BALANCE': 100.50},
            {'ID': 1, 'NAME': 'Mary', 'BALANCE': 100},
            {'ID': 2, 'NAME': u'João', 'BALANCE': 100.25},
        ]

    def test_fixed_width_writer(self):
        cols = [
            ('ID', 2),
            ('NAME', 5),
            ('BALANCE', 10, {'direction': '>', 'decimal_spaces': 2}),
        ]

        fww = FixedWidthWriter(self.s, cols)
        fww.writerows(self.objs)

        lines = self.s.getvalue()

        self.assertIn(u'0 Jack     100.50', lines)
        self.assertIn(u'1 Mary     100.00', lines)
        self.assertIn(u'2 João     100.25', lines)

    def test_fixed_width_writer_direction(self):
        cols = [
            ('ID', 2),
            ('NAME', 5),
            ('BALANCE', 10, {'direction': '<', 'decimal_spaces': 2}),
        ]

        fww = FixedWidthWriter(self.s, cols)
        fww.writerows(self.objs)

        lines = self.s.getvalue()

        self.assertIn(u'0 Jack 100.50    ', lines)
        self.assertIn(u'1 Mary 100.00    ', lines)
        self.assertIn(u'2 João 100.25    ', lines)

    def test_fixed_width_writer_decimals(self):
        cols = [
            ('ID', 2),
            ('NAME', 5),
            ('BALANCE', 10, {'direction': '>', 'decimal_spaces': 0}),
        ]

        fww = FixedWidthWriter(self.s, cols)
        fww.writerows(self.objs)

        lines = self.s.getvalue()

        self.assertIn(u'0 Jack        100', lines)
        self.assertIn(u'1 Mary        100', lines)
        self.assertIn(u'2 João        100', lines)
