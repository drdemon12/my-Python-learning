from PIL import Image
img = Image.open('google.png').convert('L')
img.save('output_file.jpg')