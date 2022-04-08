from riotwatcher import LolWatcher, ApiError
import pandas as pd
import numpy as np
#global info
api_key='RGAPI-fb70e63b-a37c-4e03-9585-d40abdf02603'
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
match_detail3=match_detail2['participants'][8]
barbjune={}
participant=[]
barbjune['GameID']=match_detail['info']['gameId']
barbjune['Win']=int(match_detail3['win'])
barbjune['WardsPlaced']=match_detail3['wardsPlaced']
barbjune['WardsDestroyed']=match_detail3['wardsKilled']
barbjune['FirstBlood']=match_detail3['firstBloodKill']+match_detail3['firstBloodAssist']
barbjune['Kills']=match_detail3['kills']
barbjune['Deaths']=match_detail3['deaths']
barbjune['Assist']=match_detail3['assists']
barbjune['EpicMonsters']=match_detail3["challenges"]['dragonTakedowns']+match_detail3["challenges"]['riftHeraldTakedowns']
barbjune['DragonKilled']=match_detail3["challenges"]['dragonTakedowns']
barbjune['HeraldKilled']=match_detail3["challenges"]['riftHeraldTakedowns']
barbjune['TowersKilled']=match_detail3['turretTakedowns']
barbjune['TotalGold']=match_detail3['goldEarned']
barbjune['Level']=match_detail3['champLevel']
barbjune['TotalExperience']=match_detail3['champExperience']
barbjune['TotalMinionsKilled']=match_detail3['totalMinionsKilled']
barbjune['TotalJungleMinionsKilled ']=match_detail3['neutralMinionsKilled']
barbjune['GoldPerMin']=match_detail3["challenges"]['goldPerMinute']
barbjune['totalDamageDeal']=match_detail3['totalDamageDealt']
barbjune['TotalDamagetoChamps']=match_detail3['totalDamageDealtToChampions']
barbjune['DmgPerMin']=match_detail3["challenges"]['damagePerMinute']

participant.append(barbjune)
df=pd.DataFrame(participant)
print(df)

