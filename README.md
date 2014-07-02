py-fixedwidthwriter
===================

A class to write fixed-width files with an interface similar to python`s csv writer


Usage
=====

The constructor takes the following arguments:


#### fd

The file descriptor to write to.


#### fields

A list of tuples containing the title of the column and the width of the corresponding field.
For example:

```python
cols = [
    ('ID', 5),
    ('NAME', 40),
]
```

Can optionally contain a `options` dictionary containing the keys `direction` and `decimal_spaces`.

The `direction` key accepts the character `'>'` to right-align or the character `'<'` to left-align.
Defaults to `'<'` when omitted.

**Note that** when using the `decimal_spaces` key, the length of the integer part plus the length of the fractional part plus one, for the decimal mark, must not exceed the set column width.
If omitted, defaults to `unicode(value)` behaviour.

For example:

```python
cols = [
    ('BALANCE', 6, {'direction': '>', 'decimal_spaces': 2}),
]
```

Will result in a right-aligned, 6-wide column. The value will be "quantized" to two decimal spaces.



#### lineterminator

(Optional) The line terminator to append to each line. Can be any string.
Defaults to `'\r\n'`


### Methods

#### writerow(rowdict)

A dictonary with keys corresponding to the defined column names and their respective values. Extra keys are ignored.

##### writerows(rowdicts)

A list of dictionaries with the format accepted by `writerow`.



Example
===================

```python
from fixedwidth import FixedWidthWriter

cols = [
    ('ID', 5),
    ('NAME', 40),
    ('BALANCE', 6, {'direction': '>', 'decimal_spaces': 2}),
]

objs = [
    {'ID': 0, 'NAME': 'Jack', 'BALANCE': 100.50},
    {'ID': 1, 'NAME': 'Mary', 'BALANCE': 100}
]

with open('file.txt', 'wb') as fixed_file:
    fww = FixedWidthWriter(fixed_file, cols)
    fww.writerows(objs)

```
