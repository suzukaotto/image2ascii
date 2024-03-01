from image2ascii import image2ascii

image_path = r'src/pepe.jpg'
width = 100
height = 50

ascii_art = image2ascii(image_path, width, height)
print(ascii_art)