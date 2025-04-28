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


nodePackageProps = nodeLockJson['packages']

missedProps = list()
# existingProps = list()

strNodeModules = 'node_modules/'
for key in dependencyPropsDic:
 
    prop = nodePackageProps.get(strNodeModules+key)
    #Ist das Package vorhanden?
    if prop == None:
        print(key,'wurde nicht gefunden')
        missedProps.append(key)
    else:
        print(key,'vorhanden')
        # existingProps.append(key)
        nodeVersion = nodePackageProps.get(strNodeModules+key)
        nodeVersionValue = nodeVersion['version']
        print('Version',nodeVersionValue)

        packageJsonValue = dependencyPropsDic[key]
        print(packageJsonValue)


# print(existingProps)

# testVar = strNodeModules+existingProps+'version'
# print(testVar)

# version = nodePackageProps.get(strNodeModules+existingProps+['version'])
# print(version)

