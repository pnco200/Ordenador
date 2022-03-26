import os
import shutil


fhand = 'D:/Users/Panico/Downloads'
cumplio = bool
cumplio = False

for filename in os.listdir(fhand):
    if filename.endswith('.rar') or filename.endswith('.zip') or filename.endswith('.7z'):
        destiny = 'D:/Users/Panico/Downloads/.rars'
        cumplio = True
    elif filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg') or filename.endswith('.gif'):
        destiny = 'D:/Users/Panico/Downloads/.png'
        cumplio = True
    elif filename.endswith('.exe'):
        destiny = 'D:/Users/Panico/Downloads/.exe'
        cumplio = True
    elif filename.endswith('.pdf'):
        destiny = 'D:/Users/Panico/Downloads/.pdf'
        cumplio = True
    elif filename.endswith('.jar'):
        destiny = 'D:/Users/Panico/Downloads/.jar'
        cumplio = True
    elif filename.endswith('.txt') or filename.endswith('.log'):
        destiny = 'D:/Users/Panico/Downloads/.txt'
        cumplio = True
    elif filename.endswith('.mp3') or filename.endswith('.wav'):
        destiny = 'D:/Users/Panico/Downloads/.mp3'
        cumplio = True
    
    if cumplio:
        src = 'D:/Users/Panico/Downloads/' + filename
        shutil.move(src, destiny)
    cumplio = False