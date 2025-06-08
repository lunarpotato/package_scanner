from pathlib import Path
from finder import FindFile, readNodePackage
import json
from tools import checkVersion 
pfad = Path(__file__).resolve().parent

#dictionaries aus den json files erstellen:
packageJsonObjects = FindFile(pfad)
nodeLockJson = readNodePackage(pfad)

dependencyPropsDic = packageJsonObjects['dependencies'] | packageJsonObjects['devDependencies']

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
        if packageCredential != None:
            credentials.append(packageCredential)


anzahlElemente = len(missedProps)         
if anzahlElemente >0:
    print('Following packages missing: ', missedProps)
           
else: print('All packages installed')

anzahlCredentials = len(credentials)
if anzahlCredentials >0:
    print('These versions are not matching:')
    for element in credentials:
        packageName = element.nodePackageName
        nodeVersion = element.nodePackageVersion
        jsonVersion = element.jsonPackageVersion
        print('Installed version of', packageName, ': ' + nodeVersion, ', current version: ' + jsonVersion, 'type "npm install" to update')

else: print('All versions match')

