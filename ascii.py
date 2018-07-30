from PIL import Image
im = Image.open('ascii-pineapple.jpg')
str = str(im.size)

print('Successfully loaded image!')
print('Image size: ' + str )
