import json
import requests

from src import urls


class dota2py:

    __apikey = 0

    def init_key(self, apikey):
        self.__apikey = apikey

    def get_friends_list(self, steamid):
        url = urls.BASE_URL + urls.GET_FRIEND_LIST

        params = dict()
        params['key'] = self.__apikey
        params['steamid'] = steamid
        params['relationship'] = 'friend'
        #print(url)
        ret = requests.get(url, params)
        if ret.status_code != 200:
            return None
        else:
            friends = json.loads(ret.text)['friendslist']['friends']
            friendids = list()
            for friend in friends:
                friendids.append(friend['steamid'])
            return friendids

    def get_match_history(self, account_id, matches_requested=5):
        url = urls.BASE_URL + urls.GET_MATCH_HISTORY

        params = dict()
        params['key'] = self.__apikey
        params['account_id'] = account_id
        date_max = 0
        start_at_match_id = 0
        params['matches_requested'] = 1
        ret = requests.get(url, params)
        last_match = json.loads(ret.text)['result']['matches'][0]
        start_at_match_id = last_match['match_id']
        date_max = last_match['start_time']

        match_history = list()
        while matches_requested > 0:
            params['matches_requested'] = matches_requested
            params['start_at_match_id'] = start_at_match_id
            params['date_max'] = date_max
            ret = requests.get(url, params)
            matches = json.loads(ret.text)['result']['matches']

            matches_requested -= len(matches)
            if matches_requested == 0:
                match_history += matches
                break

            if len(matches) <= 1:
                match_history += matches
                break
            start_at_match_id = matches[-1]['match_id']
            date_max = matches[-1]['start_time']
            matches.pop()
            matches_requested += 1
            match_history += matches
            print(len(matches))

        print(match_history[-1]['match_id'])
        return match_history

    def get_match_details(self, match_id):
        url = urls.BASE_URL + urls.GET_MATCH_DETAILS

        params = dict()
        params['key'] = self.__apikey
        params['match_id'] = match_id
        ret = requests.get(url, params)
        if ret.status_code != 200:
            return None
        else:
            match = json.loads(ret.text)['result']
            return match

    def get_player(self, steamid):
        url = urls.BASE_URL + urls.GET_PLAYER_SUMMARIES

        params = dict()
        params['key'] = self.__apikey
        params['steamids'] = steamid
        ret = requests.get(url, params)
        print(ret.status_code)
        if ret.status_code != 200:
            return None
        else:
            player = json.loads(ret.text)['response']['players'][0]
            return player

    def get_hero_by_id(self, heroid):
        with open('..\\ref\\heroes.json') as fp:
            heroes = json.load(fp)
        for hero in heroes:
            if hero['id'] == heroid:
                print(hero)
                return hero
        return None

    def get_hero_by_name(self, heroname):
        with open('..\\ref\\heroes.json') as fp:
            heroes = json.load(fp)
        for hero in heroes:
            if hero['name'] == heroname:
                print(hero)
                return hero
        return None

    def get_heroes(self):
        url = urls.BASE_URL + urls.GET_HEROES

        params = dict()
        params['key'] = self.__apikey
        ret = requests.get(url, params)
        if ret.status_code != 200:
            return None
        else:
            heroes = json.loads(ret.text)['result']['heroes']
            heroes.sort(key=lambda h: h['id'])
            print(heroes)
            return heroes

    def get_items(self):
        url = urls.BASE_URL + urls.GET_GAME_ITEMS

        params = dict()
        params['key'] = self.__apikey
        ret = requests.get(url, params)
        if ret.status_code != 200:
            return None
        else:
            items = json.loads(ret.text)['result']['items']
            items.sort(key=lambda i: i['id'])
            print(items)
            return items

    def get_item_by_id(self, itemid):
        items = list()
        with open('..\\ref\\items.json') as fp:
            items = json.load(fp)
        for item in items:
            if item['id'] == itemid:
                print(item)
                return item
        return None

    def get_item_by_name(self, itemname):
        items = list()
        with open('..\\ref\\items.json') as fp:
            items = json.load(fp)
        for item in items:
            if item['name'] == itemname:
                print(item)
                return item
        return None



#api = dota2api.Initialise("39059503CFC8B0D8ADF685871CA0C00D")
#do = dota2py()
#do.init_key('39059503CFC8B0D8ADF685871CA0C00D')
#do.GetFriendList(76561198073591511)
#do.get_match_history(76561198073591511)
#do.GetMatchDetails(3487385289)
#do.GetPlayer(76561198073591511)
#do.get_heroes()
#do.get_items()
#do.get_hero_by_name('npc_dota_hero_lina')
#do.get_item_by_name('item_blink')
#api = dota2api.Initialise('39059503CFC8B0D8ADF685871CA0C00D')
#print(api.get_heroes())
