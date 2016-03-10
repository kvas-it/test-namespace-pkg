from __future__ import print_function

try:
    from foo import bar
    print('>>> imported foo.bar:', bar.__doc__)
except ImportError:
    print('>>> importing foo.bar failed')

try:
    from foo import baz
    print('>>> imported foo.baz:', baz.__doc__)
except ImportError:
    print('>>> importing foo.baz failed')
