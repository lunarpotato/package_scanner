from pathlib import Path
from finder import FindFile, readNodePackage
import json
from tools import checkVersion 
aktuellerPfad = Path(__file__).resolve().parent

pfad = aktuellerPfad.parent / 'test'   

#dictionaries aus den json files erstellen:
packageJsonObjects = FindFile(pfad)
nodeLockJson = readNodePackage(pfad)

dependencyPropsDic = packageJsonObjects['dependencies']

devDependencyPropsDic = packageJsonObjects['devDependencies']


nodePackageProps = nodeLockJson['packages']

missedProps = list()

strNodeModules = 'node_modules/'
for key in dependencyPropsDic:
 
    prop = nodePackageProps.get(strNodeModules+key)
    #Ist das Package vorhanden?
    if prop == None:
        print(key,'wurde nicht gefunden')
        missedProps.append(key)
    else:
        packageCredential =checkVersion(nodePackageProps, strNodeModules, dependencyPropsDic, key)
       

