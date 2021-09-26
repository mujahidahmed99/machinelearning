import http.client
import json
import pandas as pd

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': '22330ed898de4fb5a1539f3188dfa851' }
connection.request('GET', '/v2/competitions/PL/matches?status=SCHEDULED', None, headers )
fixtures = json.loads(connection.getresponse().read().decode('unicode_escape'))

homeTeam = []
awayTeam = []
match_date = []
match_time = []
col_name = ['Date','Time','HomeTeam','AwayTeam']

for index in range(len(fixtures['matches'])):
    homeTeam.append(fixtures['matches'][index]['homeTeam']['name'][:-3])
    awayTeam.append(fixtures['matches'][index]['awayTeam']['name'][:-3])
    match_date.append(fixtures['matches'][index]['utcDate'][:-10])
    match_time.append(fixtures['matches'][index]['utcDate'][11:16])
df = pd.DataFrame([match_date,match_time,homeTeam,awayTeam], index=col_name)
df = df.T
df.to_csv('fixtures.csv')

print(fixtures['matches'][0]['utcDate'][:-10])
print(fixtures['matches'][0]['utcDate'][11:16])
