from mock import patch
from service import Service
import unittest


class test_service(unittest.TestCase):
    @patch('service.Service.bad_random', return_value = 10)
    def test_bad_random(self, bad_random):
        service = Service()
    
        assert service.bad_random() == 10

    @patch('service.Service.bad_random', return_value = 10)
    def test_divide(self, bad_random):
        service = Service()

        assert service.divide(1) == 10
        #assert service.divide(0) == "Division by zero"
        with self.assertRaises(ZeroDivisionError):
            service.divide(0)
        assert service.divide(-1) == -10
    

    def test_abs_plus(self):
        service = Service()

        assert service.abs_plus(1) == 2
        assert service.abs_plus(0) == 1
        assert service.abs_plus(-1) == 2

    
    @patch('service.Service.bad_random', return_value=15)
    def test_complicated_function(self, bad_random):
        service = Service()

        assert service.complicated_function(5) == (3, 1)
        #assert service.complicated_function(0) == (11, 1)
        with self.assertRaises(ZeroDivisionError):
            service.complicated_function(0)
        assert service.complicated_function(-5) == (-3, 1)


if __name__ == '__main__':
  unittest.main()

