import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import unittest
from ping_check import ping
class T(unittest.TestCase):
    def test_localhost_up(self):
        self.assertTrue(ping("127.0.0.1"))
    def test_invalid_host_down(self):
        self.assertFalse(ping("256.256.256.256"))
if __name__ == "__main__": unittest.main()
