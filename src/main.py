from pathlib import Path
from finder import FindFile
import json

aktuellerPfad = Path(__file__).resolve().parent

pfad = aktuellerPfad.parent / 'test'   



inhalt = FindFile(pfad)


jsonObjects = json.loads(inhalt)
print(jsonObjects)


dependencyPropsDic = jsonObjects['dependencies']

devDependencyPropsDic = jsonObjects['devDependencies']

for item, value in dependencyPropsDic.items():

    print(item, value)