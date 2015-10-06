# Style Guide

* [PEP 8]
* [Beyond PEP 8]





## Definitions

Functions

    Compute things; return a value.

Procedures

    Do things; modify values.





## Code lay-out

### Indentations

Four spaces.

### Line Length

80 suggested.

Use common sense! (see: [Beyond PEP 8])

### String Quotes

Whichever is easier to format; single-quote (') preferred.


## Optimizations

### String Formatting

([String concatenation is expensive])

Good:

    '%s%s' % ( beginning, end )

    OR

    parts = []
    for x in mylist:
        parts.append(foo(x))
    s = ''.join(parts)

Bad:

    s += foo(x)





[PEP 8]: https://www.python.org/dev/peps/pep-0008/
[Beyond PEP 8]: https://www.youtube.com/watch?v=wf-BqAjZb8M

[String concatenation is expensive]: http://pypy.org/performance.html#string-concatenation-is-expensive