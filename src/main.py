from pathlib import Path
from finder import FindFile, readNodePackage
import json

aktuellerPfad = Path(__file__).resolve().parent

pfad = aktuellerPfad.parent / 'test'   

#dictionaries aus den json files erstellen:
packageJsonObjects = FindFile(pfad)
nodeLockJson = readNodePackage(pfad)

dependencyPropsDic = packageJsonObjects['dependencies']

devDependencyPropsDic = packageJsonObjects['devDependencies']

for key, value in dependencyPropsDic.items():

    print(key, value)




nodePackageProps = nodeLockJson['packages']

missedProps = list()

strNodeModules = 'node_modules/'
for key in dependencyPropsDic:
 
    prop = nodePackageProps.get(strNodeModules+key)
    #Ist das Property vorhanden?
    if prop == None:
        print('Datei nicht gefunden')
        missedProps.append(key)
    else:
        print('Datei vorhanden')