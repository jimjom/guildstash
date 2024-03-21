import sys
sys.path.append(f"{sys.path[0]}/..")

from guild.http.poewebrequest import PoEWebRequest
import unittest


class testPoEWebRequest(unittest.TestCase):

    def test_request(self):
        
        poeRequest = PoEWebRequest()

        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()