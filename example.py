from image2ascii import image2ascii

image_path = r'src/image.png'
width = 100
height = 20
ascii_chars = "# "

ascii_art = image2ascii(image_path, width, height, ascii_chars, black=" ")
print(ascii_art)