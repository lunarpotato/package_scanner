import json
from pathlib import Path

def FindFile(pfad):
    for datei in pfad.iterdir():
        dateiname = datei.name 

        if dateiname == 'testpackage.json':
        
            with datei.open() as f:
                dateiInhalt = f.read()
                packageJson = json.loads(dateiInhalt)
    return packageJson
            




def readNodePackage(pfad):
    """Lies die package.lock.json im node_modules
        Returns: dic: package im json Format    
    """
    for datei in pfad.iterdir():
            dateiname = datei.name 

            if dateiname == 'node_modules':
                modulePfad = pfad / 'node_modules'

                for modulesDatei in modulePfad.iterdir():
                     dateiname = modulesDatei.name

                     if dateiname == '.package-lock.json':     
                        with modulesDatei.open() as f:
                            jsoncontent = f.read()
                            nodeLockJson = json.loads(jsoncontent)
    return nodeLockJson