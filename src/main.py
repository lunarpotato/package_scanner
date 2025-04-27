from pathlib import Path
from finder import FindFile, readNodePackage
import json

aktuellerPfad = Path(__file__).resolve().parent

pfad = aktuellerPfad.parent / 'test'   

packageJsonObjects = FindFile(pfad)


dependencyPropsDic = packageJsonObjects['dependencies']

devDependencyPropsDic = packageJsonObjects['devDependencies']

for key, value in dependencyPropsDic.items():

    print(key, value)



nodeLockJson = readNodePackage(pfad)
