import unittest
from src.utils.say_my_name import sayMyName

class TestSayMyName(unittest.TestCase):
    def test_defaultArgsTest(self):
        self.assertEqual(sayMyName(),"Mayank Pachpande")
        
if __name__ == '__main__':
    print("main() test-say-my-name")
    unittest.main()