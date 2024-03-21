import os
import datetime
import time
import pickle
from guild.http.poewebrequest import PoEWebRequest

class PoEGuildRequest:

    __guild_id__ = '942574'

    __guild_url__ = f"https://www.pathofexile.com/api/guild/{__guild_id__}/stash/history"

    def getAllGuildHistory(self, league):
        startDate = None
        endDate = None
        index = 0
        searchAgain = True

        if(league == "Affliction"):
            startDate = datetime.date(year=2023, month=12, day=8)
            endDate = datetime.date(year=2024, month=3, day=21)

        if(league == "Necropolis"):
            startDate = datetime.date(year=2024, month=3, day=27)
            endDate = datetime.date(year=2024, month=7, day=27)


        start = (int(time.mktime(startDate.timetuple())))
        end = (int(time.mktime(endDate.timetuple())))

        while(searchAgain):

            results = self.getGuildHistory(start, end, index)
            if(results == None): return
            
            searchAgain = bool(results['truncated'])
            
            if searchAgain:
                index = int(results['entries'][-1]['id'])
                start = int(results['entries'][-1]['time'])
                print(results['entries'][-1])
                print('Sleeping 1 Second')
                time.sleep(1)


        return True

    def getGuildHistory(self, start, end, index):
        request = PoEWebRequest()

        url = self.__guild_url__ + f"?from={start}&end={end}"

        if (index > 0):
            url = url + f"&fromid={index}"

        print(url)
        result = request.makeRequest(url)

        if result.status_code == 200:
            return result.json()
            
        return None
            #entries = data['entries']
            #truncated = data['truncated']
            #for line in entries:
            #    print(f"{line['id']} : {line['account']['name']}")
            
            #with open('./../guild/data/dump.pickle', 'wb') as pickleFile:
            #    pickle.dump(result._content, pickleFile)