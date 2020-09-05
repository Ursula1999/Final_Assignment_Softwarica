import unittest
from frontend.Cos_Interface import *
from model.get_set import *
from backend.dbconnection import *


class TestSearching(unittest.TestCase):
    def setUp(self):
        self.data = [(1, 'Daily Moisturising Cream', 'essencia', 'Rs 1400', 'Men', '2020/12/03', '2021/12/04'),
                     (2, 'LOTUS PROFESSIONAL', 'Lotus', 'Rs 1100', 'Men', '2019/12/03', '2021/12/04'),
                     (3, 'White glow', 'Lotus', 'Rs 1000', 'Men', '2019/12/03', '2021/12/04'),
                     (4, 'NINA RICCI', 'Nina', 'Rs 2100', 'women', '2019/12/03', '2021/12/04'),
                     (5, 'Foundation', 'Akle', 'Rs 2300', 'women', '2020/09/03', '2021/12/04'),
                     (6, 'Neon Beauty Brush', 'NEON', 'Rs 2200', 'women', '2019/12/03', '2028/12/04')]

    def test_search(self):
        self.assertEqual([(4, 'NINA RICCI', 'Nina', 'Rs 2100', 'women', '2019/12/03', '2021/12/04')],
                         Dashboard.search_method_function(self.data, 'Nike RICCI'))

    def tearDown(self):
        self.data = None

class TestSearching(unittest.TestCase):
    def setUp(self):
        self.data = [(1, 'Daily Moisturising Cream', 'essencia', 'Rs 1400', 'Men', '2020/12/03', '2021/12/04'),
                     (2, 'LOTUS PROFESSIONAL', 'Lotus', 'Rs 1100', 'Men', '2019/12/03', '2021/12/04'),
                     (3, 'White glow', 'Lotus', 'Rs 1000', 'Men', '2019/12/03', '2021/12/04'),
                     (4, 'NINA RICCI', 'Nina', 'Rs 2100', 'women', '2019/12/03', '2021/12/04'),
                     (5, 'Foundation', 'Akle', 'Rs 2300', 'women', '2020/09/03', '2021/12/04'),
                     (6, 'Neon Beauty Brush', 'NEON', 'Rs 2200', 'women', '2019/12/03', '2028/12/04')]

    def test_search(self):
        self.assertEqual([(5, 'Foundation', 'Akle', 'Rs 2300', 'women', '2020/09/03', '2021/12/04')],
                         Dashboard.search_method_function(self.data, 'Foundation'))

    def tearDown(self):
        self.data = None


class Test_DbCurd(unittest.TestCase):
    def setUp(self):
        self.dbconnect = Curd()
        self.query = 'insert into product values (%s,%s,%s,%s,%s,%s,%s)'
        self.values = (20, 'White glow', 'Lotus', 'Rs 1000', 'Men', '2019/12/03', '2021/12/04')
        self.sel_query = 'select * from product where product_id=' + str(20)

    def test_insert(self):
        self.dbconnect.add_data(self.query, self.values)
        self.assertEqual([(20, 'White glow', 'Lotus', 'Rs 1000', 'Men', '2019/12/03', '2021/12/04')],
                         self.dbconnect.fetch_data(self.sel_query))
        del_query = 'delete from product where product_id = %s'
        del_value = (20,)
        self.dbconnect.delete_data(del_query, del_value)

    def tearDown(self):
        self.query = None
        self.values = None
        self.sel_query = None
        self.dbconnect = None


class Test_Sorting(unittest.TestCase):
    def setUp(self):
        self.data = [(1, 'Daily Moisturising Cream', 'essencia', 'Rs 1400', 'Men', '2020/12/03', '2021/12/04'),
                     (2, 'LOTUS PROFESSIONAL', 'Lotus', 'Rs 1100', 'Men', '2019/12/03', '2021/12/04'),
                     (3, 'White glow', 'Lotus', 'Rs 1000', 'Men', '2019/12/03', '2021/12/04')]

        self.index = 1

    def test_search(self):
        self.assertEqual([(1, 'Daily Moisturising Cream', 'essencia', 'Rs 1400', 'Men', '2020/12/03', '2021/12/04'),
                          (2, 'LOTUS PROFESSIONAL', 'Lotus', 'Rs 1100', 'Men', '2019/12/03', '2021/12/04'),
                          (3, 'White glow', 'Lotus', 'Rs 1000', 'Men', '2019/12/03', '2021/12/04')],
                         OrderDetails.sort_method(self.data, self.index))

    def tearDown(self):
        self.data = None
        self.index = None


class Test_SetGet(unittest.TestCase):
    def setUp(self):
        self.std = SaveRegistration('user', 'user')

    def test_set_usernamePassword(self):
        self.std.set_username('admin')
        self.std.set_password('admin')
        self.assertEqual('admin',self.std.get_username())
        self.assertEqual('admin',self.std.get_password())

    def test_get_usernamePassword(self):
        self.assertEqual('user', self.std.get_username())
        self.assertEqual('user', self.std.get_password())


if __name__ == '__main__':
    unittest.main()
