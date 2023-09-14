import qrcode

image= qrcode.make("https://www.youtube.com/watch?v=oHg5SJYRHA0")
image.save("qr.png","PNG")