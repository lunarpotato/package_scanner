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



for datei in pfad.iterdir():
        dateiname = datei.name 

        if dateiname == 'node_modules':
            modulePfad = pfad / 'node_modules'

            for inhalt in modulePfad.iterdir():
                 dateiname = inhalt.name

                 if dateiname == '.package-lock.json':     
                    with inhalt.open() as f:
                        dateiinhalt = f.read()
                        print(dateiinhalt)
                   

            
   

                

            