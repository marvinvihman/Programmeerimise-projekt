from PIL import Image

im = Image.open("Leveli näide.png", "r")

pix_val = list(im.getdata())
w, h = im.size
pixels = [pix_val[i * w:(i + 1) * w] for i in range(h)]

print(len(pixels[0]), "x", len(pixels))