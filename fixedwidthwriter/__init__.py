# coding: utf-8
from decimal import Decimal


class FixedWidthWriter():

    def __init__(self, fd, fields, line_ending='linux'):
        self.fd = fd
        self.fields = fields
        if line_ending == 'linux':
            self.line_ending = '\n'
        elif line_ending == 'windows':
            self.line_ending = '\r\n'
        else:
            raise ValueError('Only windows or linux line endings supported')

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
                value = unicode(Decimal(value)
                                .quantize(Decimal(10)**-decimal_spaces))
            part = '{0: {1}{2}}' \
                .format(value, options.get('direction', '<'), width)
            row.append(part)
        row = ''.join(row)
        self.fd.write(row + self.line_ending)

    def writerows(self, rowdicts):
        for rowdict in rowdicts:
            self.writerow(rowdict)
