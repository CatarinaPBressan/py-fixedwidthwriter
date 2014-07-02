# coding: utf-8
from decimal import Decimal


class FixedWidthWriter():

    def __init__(self, fd, fields, lineterminator='\r\n'):
        self.fd = fd
        self.fields = fields

    def writerow(self, rowdict):
        row = []
        for field in self.fields:
            try:
                key, width, options = field
            except ValueError:
                key, width = field
                options = {}
            value = rowdict[key]
            decimal_spaces = options.get('decimal_spaces', 0)
            if decimal_spaces:
                value = Decimal(value).quantize(Decimal(10)**-decimal_spaces)
            value = unicode(value)  # forcing the value to be a string so we can easily check its length
            if len(value) > width:
                raise ValueError('Value {0} is too wide to fit in column {1}.'
                                 .format(value, key))
            part = '{0: {1}{2}}' \
                .format(value, options.get('direction', '<'), width)
            row.append(part)
        row = ''.join(row)
        self.fd.write(row + self.lineterminator)

    def writerows(self, rowdicts):
        for rowdict in rowdicts:
            self.writerow(rowdict)
