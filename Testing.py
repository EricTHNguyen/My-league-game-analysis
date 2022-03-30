from riotwatcher import LolWatcher, ApiError
import pandas as pd
import numpy as np
#global info
api_key='RGAPI-724657ae-04b5-46e7-ba46-82bbe5bf152e'
watcher= LolWatcher(api_key)
my_region='na1'
me= watcher.summoner.by_name(my_region,'Barbjune')
#print(me)
#rank info
my_ranked_stats=watcher.league.by_summoner(my_region, me['id'])
#print(my_ranked_stats)
#games played
my_matches=watcher.match.matchlist_by_puuid("americas", me['puuid'],type='ranked', count=100)
#print(my_matches)
match_detail=watcher.match.by_id("americas", my_matches[0])
match_detail2=match_detail['info']
match_detail3=match_detail2['participants']
del match_detail3[0:8]

print(match_detail3)
participants=[]
for row in match_detail['info']['participants']:
    participants_row={}
    participants_row['win']=int(row['win'])
    
    participants.append(participants_row)
df=pd.DataFrame(participants)
print(df)

#checks league's patch version
latest= watcher.data_dragon.versions_for_region(my_region)['n']['champion']
#champion static info
static_champ_list=watcher.data_dragon.champions(latest, False, 'en_US')

