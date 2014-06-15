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
        _row = []
        for field in self.fields:
            try:
                _key, _width, _options = field
            except ValueError:
                _key, _width = field
                _options = {}
            _value = rowdict[_key]
            _decimal_spaces = _options.get('decimal_spaces', 0)
            if _decimal_spaces:
                _value = unicode(Decimal(_value)
                                 .quantize(Decimal(10)**-_decimal_spaces))
            _part = '{0: {1}{2}}' \
                .format(_value, _options.get('direction', '<'), _width)
            _row.append(_part)
        _row = ''.join(_row)
        self.fd.write(_row + self.line_ending)

    def writerows(self, rowdicts):
        for rowdict in rowdicts:
            self.writerow(rowdict)
