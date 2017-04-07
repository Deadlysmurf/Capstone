
#Added, Age, Years Played, Country of Birth, First and Last Names, Weight, Height, Bat Hand, Throwing Hand

Trim_Master = Master[['playerID','birthYear', 'birthCountry', 'nameFirst','nameLast', 'weight','height','bats','throws','debut']]
Data = Salaries.merge(Trim_Master,how='left', left_on='playerID', right_on='playerID')
Data['age'] = Data['yearID'] - Data['birthYear']
Data['debut'] = pd.to_datetime(Data['debut'])
Data['debutYear'] = pd.DatetimeIndex(Data['debut']).year
Data['yearsPlayed'] = Data['yearID'] - Data['debutYear']
Data = Data.drop(['birthYear', 'debut', 'debutYear'], axis=1)

#Adding in the appearance chart
Data = pd.merge(Data, Appearances,  how='left', left_on=['yearID','teamID', 'playerID', 'lgID'], right_on = ['yearID','teamID','playerID','lgID'])
