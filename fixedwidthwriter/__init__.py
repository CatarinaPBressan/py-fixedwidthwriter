# coding: utf-8
from __future__ import absolute_import

from decimal import Decimal

import six


class FixedWidthWriter():

    def __init__(self, fd, fields, lineterminator='\r\n'):
        self.fd = fd
        self.fields = fields
        self.lineterminator = lineterminator

    def writerow(self, rowdict):
        row = []
        for field in self.fields:
            try:
                key, width, options = field
            except ValueError:
                key, width = field
                options = {}
            value = rowdict[key]
            decimal_spaces = options.get('decimal_spaces')
            if decimal_spaces and decimal_spaces >= 0:
                value = Decimal(value).quantize(Decimal(10)**-decimal_spaces)
            value = six.text_type(value)
            if len(value) > width:
                raise ValueError('Value {0} is too wide to fit in column {1}.'
                                 .format(value, key))
            part = u'{0: {1}{2}}' \
                .format(value, options.get('direction', '<'), width)
            row.append(part)
        row = ''.join(row)
        if six.PY2:
            row = row.encode('utf-8')
        self.fd.write(row + self.lineterminator)

    def writerows(self, rowdicts):
        for rowdict in rowdicts:
            self.writerow(rowdict)
