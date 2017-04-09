
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
Data = Data.drop(['G_batting', 'G_defense'], axis=1)


#Remove the pitchers and catchers
#Data = Data[Data["G_p"] == 0]
#Data = Data[Data["G_c"] == 0]
#Data = Data.drop(["G_p", "G_c"], axis=1)

#Add fielding stats
Data = pd.merge(Data, Fielding,  how='left', left_on=['yearID','teamID', 'playerID', 'lgID'], right_on = ['yearID','teamID','playerID','lgID'])
Data = Data.drop(['stint', 'POS', 'PB', 'WP', 'SB', 'CS', 'ZR', 'GS_y'], axis=1)

#Converting to the stats to per game
Data['Games'] = Data['InnOuts']/3/9
Data[['POg','Ag', 'Eg', 'DPg']] = Data[['PO','A', 'E', 'DP']].divide(Data.Games, axis=0).fillna(0)
Data = Data.drop(['InnOuts', 'PO','A', 'E', 'DP'], axis=1)


#Add Batting stats
Data = pd.merge(Data, Batting,  how='left', left_on=['yearID','teamID', 'playerID', 'lgID'], right_on = ['yearID','teamID','playerID','lgID'])
Data = Data.drop(['stint', 'G_y'], axis=1)

#Adding Calc Stats
Data['1B'] = Data['H'].subtract(Data['2B'].subtract(Data['3B'].subtract(Data['HR'])))
Data['SLG'] = (Data['1B'].add(Data['2B']*2).add(Data['3B']*3).add(Data['HR']*4)).divide(Data['AB'])
Data['OBP'] = (Data['H']+Data['BB']+Data['HBP'])/(Data['AB']+Data['BB']+Data['HBP']+Data['SF'])
Data['OPS'] = Data['SLG'] + Data['OBP']


#Converting to the stats per at Bat
Data[['R', 'H', '2B', '3B', 'HR', 'RBI', 'SB','CS', 'BB', 'SO', 'IBB', 'HBP', 'SH', 'SF', 'GIDP']] = Data[['R', 'H', '2B', '3B', 'HR', 'RBI', 'SB','CS', 'BB', 'SO', 'IBB', 'HBP', 'SH', 'SF', 'GIDP']].divide(Data.AB, axis=0).fillna(0)


#Remove infs and Nans
Data = Data.replace(np.inf, np.nan)
Data = Data.replace(np.nan, 0)
