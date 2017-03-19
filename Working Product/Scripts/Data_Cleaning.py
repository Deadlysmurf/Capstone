
#Added, Age, Years Played, Country of Birth, First and Last Names, Weight, Height, Bat Hand, Throwing Hand

Trim_Master = Master[['playerID','birthYear', 'birthCountry', 'nameFirst','nameLast', 'weight','height','bats','throws','debut']]
Salary_Analysis = Salaries.merge(Trim_Master,how='left', left_on='playerID', right_on='playerID')
Salary_Analysis['age'] = Salary_Analysis['yearID'] - Salary_Analysis['birthYear']
Salary_Analysis['debut'] = pd.to_datetime(Salary_Analysis['debut'])
Salary_Analysis['debutYear'] = pd.DatetimeIndex(Salary_Analysis['debut']).year
Salary_Analysis['yearsPlayed'] = Salary_Analysis['yearID'] - Salary_Analysis['debutYear']
Salary_Analysis = Salary_Analysis.drop(['birthYear', 'debut', 'debutYear'], axis=1)
