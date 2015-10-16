import collections


def get(d, *path, **kwargs):
    default = kwargs.get('default', None)
    strict = kwargs.get('strict', False)

    for member in path:
        # try index as is
        try:
            d = d[member]
            continue
        except (TypeError, KeyError, AttributeError) as e:
            if strict:
                raise KeyError('%s undefined' % '.'.join(map(repr, path)))

        # try index as str
        try:
            d = d[str(member)]
            continue
        except (TypeError, KeyError, AttributeError) as e:
            if strict:
                raise KeyError('%s undefined' % '.'.join(map(repr, path)))

        # try attribute
        try:
            d = getattr(d, member)
            continue
        except (AttributeError, TypeError) as e:
            if strict:
                raise KeyError('%s undefined' % '.'.join(map(repr, path)))

        # try int index
        try:
            d = d[int(member)]
            continue
        except (TypeError, KeyError, ValueError, AttributeError) as e:
            if strict:
                raise KeyError('%s undefined' % '.'.join(map(repr, path)))

        d = default
        break
    return d


def merge(d1, d2):
    for k, v in d2.iteritems():
        if isinstance(v, collections.Mapping):
            r = merge(d1.get(k, {}), v)
            d1[k] = r
        else:
            d1[k] = d2[k]
    return d1


def copy(d):
    out = d.copy()
    for k, v in d.iteritems():
        if isinstance(v, dict):
            out[k] = copy(v)
        elif isinstance(v, list):
            out[k] = v[:]
    return out


def expand(*path, **kwargs):
    chain = kwargs.get('value') or None
    for segment in reversed(path):
        chain = { segment: chain }
    return chain
