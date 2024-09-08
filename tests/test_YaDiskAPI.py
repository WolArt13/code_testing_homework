import unittest
import API_methods


class TestYaApi(unittest.TestCase):

    def setUp(self):
        API_methods.create_folder('test_passed')

    def test_success_create_folder(self):
        self.assertEqual(API_methods.create_folder('test'), 201)

    def test_passed_create_folder(self):
        self.assertEqual(API_methods.create_folder('test_passed'), 409)

    def tearDown(self):
        # Удаляем папку после прохождения теста на создание папки
        API_methods.delete_folder('test')
        API_methods.delete_folder('test_passed')


if __name__ == '__main__':
    unittest.main()