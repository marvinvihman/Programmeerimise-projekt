from tkinter import Tk #monitori mõõtmete saamiseks

#leitakse monitori mõõtmed
root = Tk()
disp_orig_w  = root.winfo_screenwidth()
disp_orig_h = root.winfo_screenheight()

#määratakse akna mõõtmed
disp_w = int(disp_orig_w/2)
disp_h = int(disp_orig_h/2)

#määratakse leveli originaalpikkus ja akna pikkus suhe(hiljem, et transformeerida pilt õigeks suuruseks), pikkuseks arvutamisel on vastavalt kas kõrgus või laius, olenevalt monitorist
if disp_orig_w*3 < 4*disp_orig_h:
    scale_ratio = 0
else:
    scale_ratio = 0

#kas aken on FULLSCREEN mode peal või mitte
FULLSCREEN = 0

bgColor = (0, 255, 255)

positionX, positionY = 10, 10
startPos = (positionX, positionY)


