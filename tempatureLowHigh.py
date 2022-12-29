#demonstrades the use of the panda and DataFrame

import pandas as pd

temps = {'Mon': [68, 89], 'Tue': [71, 93], 'Wed': [66, 82], 'Thu': [75, 97], 'Fri': [62, 79]}
temperatures = pd.DataFrame(temps, index=['Low', 'High'])
print(temperatures)

tempLocation = temperatures.loc[:, 'Mon':'Wed']
print()
print(tempLocation)

tempLow = temperatures.loc['Low']
print()
print(tempLow)

tempMean = temperatures.mean()
print()
print(tempMean)
