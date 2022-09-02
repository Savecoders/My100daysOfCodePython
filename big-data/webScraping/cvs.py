import pandas as pd

# cvs in the website
link = 'https://www.football-data.co.uk/mmz4281/2122/E0.csv'

dtPremier = pd.read_csv(link)

dtPremier.rename(columns={'HomeTeam': 'HomeTeamLige',
                          'AwayTeam': 'AwayTeamLige',
                          }, inplace=True)


print(dtPremier)
