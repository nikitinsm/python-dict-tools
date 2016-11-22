import unittest

from dict_tools import merge


class MergeTest(unittest.TestCase):
    def test_base(self):
        d1 = {'sket': {
            'bossun': 'concentration',
            'himeko': 2,
            'switch': True
        }}

        d2 = {'gintama': {
            'gin-san': 'hair',
            'shimpachi': 3,
            'kagura': False
        }}

        d_expecting = {
            'sket': {
                'bossun': 'concentration',
                'himeko': 2,
                'switch': True
            },
            'gintama': {
                'gin-san': 'hair',
                'shimpachi': 3,
                'kagura': False
            }
        }

        print d_expecting
        result = merge(d1, d2)
        print result
        self.assertDictEqual(result, d_expecting)


if __name__ == '__main__':
    unittest.main()
