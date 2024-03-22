import sys
sys.path.append(f"{sys.path[0]}/..")

from guild.http.poeguildrequest import PoEGuildRequest
import unittest
from datetime import date
import time

class testPoEGuildRequest(unittest.TestCase):

    def test_initialize(self):
        
        poeRequest = PoEGuildRequest()

        self.assertIsNotNone(poeRequest)

    def test_getGuildHistory(self):
        
        startDate = date(year=2023, month=12, day=8)
        endDate = date(year=2024, month=3, day=20)
        guildRequest = PoEGuildRequest()

        start = (int(time.mktime(startDate.timetuple())))
        end = (int(time.mktime(endDate.timetuple())))

        result = guildRequest.getGuildHistory(start, end, 0)
        self.assertIsNotNone(result)

    def test_getAllGuildHistory(self):

        league = "Affliction"
        guildRequest = PoEGuildRequest()

        result = guildRequest.getAllGuildHistory(league)
        self.assertIsNotNone(result)

if __name__ == "__main__":
    unittest.main()