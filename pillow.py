from PIL import Image, ImageFilter

before = Image.open("downloed.jpg")



after = before.filter(ImageFilter.RankFilter)
after.save("nnn.png")