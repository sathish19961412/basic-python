import qrcode
img = qrcode.make('https://youtu.be/ogsoYymZ7H0')
type(img)  # qrcode.image.pil.PilImage
img.save("you.png")