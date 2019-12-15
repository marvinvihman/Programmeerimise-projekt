from PIL import Image

class Level:
    "Leveli .png fail läheb muutujaks"
    def __init__(self, piltFail):
        self.piltFail = piltFail

    "PIL Image'iga avab pildi, et andmed saada kätte"
    def open_pic(self):
        return Image.open(self.piltFail, "r") #Originaal pilt

    "Pildi downscalimiseks" \
    "Avab leveli ning teeb etteantud suuruseks" \
    "tagastab uue leveli"
    def resize_level(self, new_size):
        self.new_size = new_size # Uus (width, height)
        piltFail = self.open_pic().copy() # Avab leveli, Image.open(level)
        level = piltFail.resize(new_size, Image.LANCZOS) # Tagastab uue leveli uute mõõtmetega
        return level

    "Funktsioon tagastab, mis ette antud positsioonil värvi data on"
    def get_pixel_value(self, level, pos):
        self.level = level # Image.open(level)
        self.pos = pos # (x, y) kujul positsioon, kust soovid data't saada
        pix_value = level.getpixel(pos) # Tagastab (r,g,b)
        return pix_value