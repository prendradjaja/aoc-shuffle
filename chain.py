'''
TODO: Quick lambdas? Some possible syntaxes:

lambda x: x
L >> '_'
L.x >> 'x'
L('_')

lambda x: x.strip().upper()
L >> '_.strip().upper()'
L.x >> 'x.strip().upper()'
L('_.strip().upper()')
'''


from operator import methodcaller as dot


class _L:
    def __getattr__(self, name):
        return _LambdaShorthand(name)
L = _L()

class _LambdaShorthand:
    def __init__(self, varname):
        self.varname = varname
    def __rshift__(self, other):
        return eval(f'lambda {self.varname}: {other}')

class F:
    def __init__(self, fn):
        self.fn = fn
    def __ror__(self, other):
        return self.fn(other)


class map_:
    def __init__(self, fn):
        self.fn = fn
    def __ror__(self, other):
        return [self.fn(x) for x in other]


class filter_:
    def __init__(self, fn):
        self.fn = fn
    def __ror__(self, other):
        return [x for x in other if self.fn(x)]


class join:
    def __init__(self, sep):
        self.sep = sep
    def __ror__(self, other):
        return self.sep.join(other)


class sort:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
    def __ror__(self, other):
        other = other[:]
        other.sort(**self.kwargs)
        return other


class flat:
    def __ror__(self, other):
        xss = other
        return [x for xs in xss for x in xs]
