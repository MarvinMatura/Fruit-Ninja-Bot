## py -m pip install opencv-python
## py -m pip install pyautogui
## py -m pip install numpy
## py -m pip install pillow
import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab

## Infos über die verschiedenen Versuche

## Versuch 1  | 63 positive Bilder, 0.5 maximale Fehlalarmrate, 3 Stufen
## Versuch 1  | 103 positive Bilder, 0.5 maximale Fehlalarmrate, 3 Stufen
## Versuch 1  | 144 positive Bilder, 0.5 maximale Fehlalarmrate, 3 Stufen
## Versuch 1  | 184 positive Bilder, 0.5 maximale Fehlalarmrate, 3 Stufen
## Versuch 1  | 225 positive Bilder, 0.5 maximale Fehlalarmrate, 3 Stufen


## Versuch 6  | 225 positive Bilder, 0.5 maximale Fehlalarmrate, 3 Stufen
## Versuch 6  | 225 positive Bilder, 0.4 maximale Fehlalarmrate, 3 Stufen
## Versuch 6  | 225 positive Bilder, 0.3 maximale Fehlalarmrate, 3 Stufen
## Versuch 6  | 225 positive Bilder, 0.2 maximale Fehlalarmrate, 3 Stufen
## Versuch 6  | 225 positive Bilder, 0.1 maximale Fehlalarmrate, 3 Stufen


## Versuch 11 | 225 positive Bilder, 0.1 maximale Fehlalarmrate, 3 Stufen
## Versuch 11 | 225 positive Bilder, 0.1 maximale Fehlalarmrate, 5 Stufen
## Versuch 11 | 225 positive Bilder, 0.1 maximale Fehlalarmrate, 8 Stufen
## Versuch 11 | 225 positive Bilder, 0.1 maximale Fehlalarmrate, 10 Stufen
## Versuch 11 | 225 positive Bilder, 0.1 maximale Fehlalarmrate, 12 Stufen

## Versuch 16 | 450 positive Bilder (mit 90° gedrehte Bilder), 0.1 maximale Fehlalarmrate, 12 Stufen
## Versuch 17 | 450 positive Bilder (mit 270° gedrehte Bilder), 0.1 maximale Fehlalarmrate, 12 Stufen
## Versuch 18 | 675 positive Bilder (mit 90° und 270° gedrehte Bilder), 0.1 maximale Fehlalarmrate, 12 Stufen

cascade = 'Versuch18.xml' ## Hier die gewünschte Cascade hinein schreiben (z.b. 'Versuch7.xml')

maximale_frucht_grösse = (160,150)
minimale_frucht_grösse = (40,50)
maximale_bombe_grösse = (140,140)
minimale_bombe_grösse = (95,95)

def maus(x,y):
    pyautogui.mouseDown()
    pyautogui.moveTo(x+25, y+115)
    print("Frucht zerschnitten.")

def frucht_erkennung(cascade_name):
    früchte_cascade = cv2.CascadeClassifier(cascade_name)
    bomben_cascade = cv2.CascadeClassifier('bomb_cascadeV1.xml')
    frucht_gefunden = früchte_cascade.detectMultiScale(aufnahme,
                                                       minSize=minimale_frucht_grösse,
                                                       maxSize=maximale_frucht_grösse)
    bombe_gefunden = bomben_cascade.detectMultiScale(aufnahme,
                                                     minSize=minimale_bombe_grösse,
                                                     maxSize=maximale_bombe_grösse)

    anzahl_früchte_gefunden = len(frucht_gefunden)
    anzahl_bomben_gefunden = len(bombe_gefunden)

    if anzahl_bomben_gefunden != 0:
        for (x, y, breite, höhe) in bombe_gefunden:
            cv2.rectangle(aufnahme, (x, y),
                            (x + höhe, y + breite),
                            (0, 0, 255), 5)
    if anzahl_früchte_gefunden != 0:
        for (x, y, breite, höhe) in frucht_gefunden:
            cv2.rectangle(aufnahme, (x, y),
                            (x + höhe, y + breite),
                            (0, 255, 0), 5)
        if anzahl_bomben_gefunden == 0:
            maus(x, y)

while True:
    aufnahme = ImageGrab.grab(bbox=(0, 100, 900, 580))
    aufnahme = np.array(aufnahme)
    aufnahme = cv2.cvtColor(aufnahme, cv2.COLOR_RGB2BGR)

    frucht_erkennung(cascade)

    cv2.imshow('Fruit Ninja Bot', aufnahme)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        cv2.destroyAllWindows()
        print("Programm geschlossen.")
        break
