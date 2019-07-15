import pandas as pd
import numpy as np

###Import data
data_200 = pd.read_csv("/Users/eileenschilliger/Documents/Studium/01_Geografie/Master_neu2/Geodata analysis and modelling/Eigenes Projekt/pyCharm/Einzugsgebiete_200mB.csv", sep=";")
#print(data_200)


###Test Spaltenauswahl, einfache Berechnungen
#mean_H = data_200['mH_04'].mean()
#print ('The middle high of ' + 'str(id) ' + 'is ' + str(mean_H) + ' m ü.M.')
#min_H = data_200['Hmin_06'].min()
#print ('The lowest high of ' + 'str(id) ' + 'is ' + str(min_H) + ' m ü.M.')

###Berechnung der Grenzwerte
#quantile = data_200.quantile([0,0.25,0.5,0.75,1], axis=0)
#print(quantile['mH_04'])


#ID auswählen und gesuchte Spalte der ID extrahieren
featureID = int(input("Choose your feature ID: "))
#print("You choose the id" + " " + str(featureID))

###Auswahl Quantils durch Benutzer
quantile = int(input("Choose your quantile: "))

###enumerate
#properties = ['mH_04']
#for variable, row in data_200.iloc('mH_04'):
    #print(properties)


###Berechnung Quantile mittlere Höhe und Slope
data_200['Quantile_rank_mH'] = pd.qcut(data_200['mH_04'], quantile, labels=False)
data_200['Quantile_rank_slope'] = pd.qcut(data_200['N20slp8_12'], quantile, labels=False)
print(data_200)

###Zeile der ausgesuchten id extrahieren und index neu aufsetzten (damit der neue Index der Zeile 0 wird)
chosenID = data_200.loc[data_200.id==featureID, : ]
chosenID.reset_index(inplace = True)
print(chosenID)

###Gib das Quantil der ausgewählten ID aus (der mittleren Höhe und Slpe)
#mH
Q_mH_04 = chosenID.at[0,'Quantile_rank_mH']
print("The middle hight of the chosen catchment is in the {} Quantile." .format(Q_mH_04))
#Slope
Q_N20slp8_12 = chosenID.at[0,'Quantile_rank_slope']
print("The slope of the chosen catchment is in the {} Quantile." .format(Q_N20slp8_12))

###wähle alle IDs mit dem selben Quantil bei der mittleren Höhe aus
mH_sameq = data_200.loc[data_200.Quantile_rank_mH==Q_mH_04, 'id']
print(list(mH_sameq))

slope_sameq = data_200.loc[data_200.Quantile_rank_slope==Q_N20slp8_12, 'id']
print(list(slope_sameq))

    #if (mH_sameq in slope_sameq):



#similar_catchement = int(mH_sameq, slope_sameq)
    #if mH_sameq = slope_sameq:
#print(similar_catchement)
    #else: print('no similar catchments')
