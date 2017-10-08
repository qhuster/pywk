from src import api


def get_recent_mathces(account_id):
    dota_api = api.dota2py()
    dota_api.init_key('39059503CFC8B0D8ADF685871CA0C00D')

    matches = dota_api.get_match_history(account_id, matches_requested=500)

    radiant_match_list = list()
    dire_match_list = list()
    for match in matches:
        #print(match)
        players = match['players']
        for player in players:
            if player['account_id'] == account_id:
                if (player['player_slot'] & 0x80) == 0:
                    radiant_match_list.append(match)
                else:
                    dire_match_list.append(match)
                break

    win_num = 0
    lose_num = 0
    for match_brief in radiant_match_list:
        match = dota_api.get_match_details(match_brief['match_id'])
        print(match)
        if match['radiant_win'] == True:
            win_num += 1
        else:
            lose_num += 1

    print('天辉方场数：' + len(radiant_match_list).__str__())
    print(win_num.__str__() + '-' + lose_num.__str__())

    win_num = 0
    lose_num = 0
    for match_brief in dire_match_list:
        match = dota_api.get_match_details(match_brief['match_id'])
        print(match)
        if match['radiant_win'] == False:
            win_num += 1
        else:
            lose_num += 1

    print('夜魇方场数：' + len(dire_match_list).__str__())
    print(win_num.__str__() + '-' + lose_num.__str__())


def steam_id_to_account_id(steam_id):
    return steam_id.__sub__(76561197960265728)

def account_id_to_steam_id(account_id):
    return account_id.__add__(76561197960265728)


#def analysis_win_rate(account_id):
#    matches = get_recent_mathces

steam_id = 76561198073591511
account_id = steam_id_to_account_id(steam_id)
get_recent_mathces(account_id)
#get_all_matches(76561198073591511)