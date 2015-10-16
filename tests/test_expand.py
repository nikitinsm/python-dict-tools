import unittest

from dict_tools import expand


class ExpandTest(unittest.TestCase):

    def test_base(self):
        result = expand(1, 2, 3)
        self.assertDictEqual(result, {1: {2: {3: None}}})

    def test_base_with_value(self):
        result = expand(1, 2, 3, value='foo')
        self.assertDictEqual(result, {1: {2: {3: 'foo'}}})

    def test_generic(self):
        result = expand(1, 'foo', (1, 2, 3), frozenset({1, 2, 3}), value='bar')
        self.assertDictEqual(result, {1: {'foo': {(1, 2, 3): {frozenset({1, 2, 3}): 'bar'}}}})
