import unittest

from dict_tools import get


class Mock(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class GetTest(unittest.TestCase):

    def test_simple(self):
        d = {'1': {'2': {'3': 3}}}
        self.assertEqual(get(d, '1', '2', '3'), 3)

    def test_list(self):
        d = {'1': {'2': [3, 4, 5, {'6': {'7': 8}}]}}
        self.assertEqual(get(d, '1', '2', 0), 3)
        self.assertEqual(get(d, '1', '2', 1), 4)
        self.assertEqual(get(d, '1', '2', 2), 5)
        self.assertEqual(get(d, '1', '2', 3, '6', '7'), 8)

    def test_list2(self):
        d = [[[[1]]], [2, [3]]]
        self.assertEqual(get(d, 0, 0, 0, 0), 1)
        self.assertEqual(get(d, 1, 1, 0), 3)

    def test_implicit_type(self):
        d = {'1': {'2': [3, 4, 5, {'6': {'7': 8}}]}}
        self.assertEqual(get(d, 1, 2, '0'), 3)
        self.assertEqual(get(d, 1, 2, '3', 6, 7), 8)

    def test_attribute(self):
        d = {'1': {'2': Mock(a3=3, a4={5: Mock(a6=6)})}}
        self.assertEqual(get(d, '1', '2', 'a3'), 3)
        self.assertEqual(get(d, '1', '2', 'a4', '5', 'a6'), 6)

    def test_default(self):
        d = {'1': {'2': {'3': 4}}}
        self.assertIs(get(d, '1', '2', '3', '4'), None)
        self.assertIs(get(d, '1', '2', '3', '4', default=5), 5)

    def test_strict_mode(self):
        d = {'1': {'2': {'3': 4}}}
        try:
            get(d, '1', '2', '3', '4', strict=True)
            self.fail()
        except Exception as e:
            self.assertIs(type(e), KeyError)
