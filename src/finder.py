from pathlib import Path

def FindFile(pfad):
    for datei in pfad.iterdir():
        dateiname = datei.name 

        if dateiname == 'testpackage.json':
            print(dateiname) 
        
            with datei.open() as f:
                dateiInhalt = f.read()
                print(dateiInhalt)
                return dateiInhalt