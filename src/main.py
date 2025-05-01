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
credentials = list()

strNodeModules = 'node_modules/'
for key in dependencyPropsDic:
 
    prop = nodePackageProps.get(strNodeModules+key)
    #Ist das Package vorhanden?
    if prop == None:
        missedProps.append(key)
    else:
        packageCredential = checkVersion(nodePackageProps, strNodeModules, dependencyPropsDic, key)
        credentials.append(packageCredential)


anzahlElemente = len(missedProps)         
if anzahlElemente >0:
    print('Folgende Packages wurden nicht installiert: ', missedProps)
           

anzahlCredentials = len(credentials)
if anzahlCredentials >0:
    print('Folgende Versionen stimmen nicht überein:')
    for element in credentials:
        packageName = element.nodePackageName
        nodeVersion = element.nodePackageVersion
        jsonVersion = element.jsonPackageVersion
        print(packageName, 'installiert: ' + nodeVersion, 'nicht installiert: ' + jsonVersion)