from decimal import Decimal
class FixedWidthWriter():

    def __init__(self, fd, fields):
        self.fd = fd
        self.fields = fields

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
        self.fd.write(_row + '\n')

    def writerows(self, rowdicts):
        for rowdict in rowdicts:
            self.writerow(rowdict)
