from pathlib import Path
from finder import FindFile

aktuellerPfad = Path(__file__).resolve().parent

pfad = aktuellerPfad.parent / 'test'   



Inhalt = FindFile(pfad)


