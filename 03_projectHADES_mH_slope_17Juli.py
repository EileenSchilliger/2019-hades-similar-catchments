import pandas as pd
import numpy as np

###Import data
data_200 = pd.read_csv("/Users/eileenschilliger/Documents/Studium/01_Geografie/Master_neu2/Geodata analysis and modelling/Eigenes Projekt/pyCharm/Einzugsgebiete_200mB.csv", sep=";")
#print(data_200)


###########################################

#ID auswählen
featureID = int(input("Choose your feature ID: "))
print("You choose the id" + " " + str(featureID))

###Auswahl Quantils durch Benutzer
quantile = int(input("Choose your quantile: "))

#Define list of criteria
criteriaNames =
criteriaIds =

#Ask the user to select the criteria
critSelect = [0, 4, 5]

###########################################

for critRow in critSelect:

    critId = criteriaIds[critRow]
    data_200['Quantile_selection'] = pd.qcut(data_200[critId], quantile, labels=False)

###Berechnung Quantile mittlere Höhe und Slope
data_200['Quantile_rank_mH'] = pd.qcut(data_200['mH_04'], quantile, labels=False)
data_200['Quantile_rank_slope'] = pd.qcut(data_200['N20slp8_12'], quantile, labels=False)
print(data_200)

###Zeile der ausgesuchten id extrahieren und index neu aufsetzten (damit der neue Index der Zeile 0 wird)
chosenID = data_200.loc[data_200.id==featureID, : ]
#chosenID.reset_index(inplace = True)
print(chosenID)

###Gib das Quantil der ausgewählten ID aus (der mittleren Höhe und Slope)
#mH
Q_mH_04 = chosenID['Quantile_rank_mH'].iloc[0]
print(Q_mH_04)
#Q_mH_04 = chosenID.at[0,'Quantile_rank_mH']
print("The middle hight of the chosen catchment is in the {} Quantile." .format(Q_mH_04))
#Slope
Q_N20slp8_12 = chosenID['Quantile_rank_slope'].iloc[0]
print("The slope of the chosen catchment is in the {} Quantile." .format(Q_N20slp8_12))

###wähle alle IDs mit dem selben Quantil bei der mittleren Höhe und dem Slope aus
mH_sameq = list(data_200.loc[data_200.Quantile_rank_mH==Q_mH_04, 'id'])
print('mH_sameq'+ str(mH_sameq))
slope_sameq = list(data_200.loc[data_200.Quantile_rank_slope==Q_N20slp8_12, 'id'])
print('slope_sameq'+ str(slope_sameq) + '\n')

### Schnittmenge der beiden listen
def intersection(mH_sameq, slope_sameq):
    Schnittmenge = [value for value in mH_sameq if value in slope_sameq]
    return Schnittmenge

print('\033[1m' + "the following catchments are similar to your chosen catchment {} "
                  "in regard to the middle hight(mH_04) and the slope(N20slp8_12) as well as your quantile {}:"
                .format(featureID, quantile))
print(str(intersection(mH_sameq, slope_sameq)) + '\033[0m')