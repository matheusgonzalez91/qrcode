import qrcode

img = qrcode.make('mcgonzalez.com.br')
img.save('M&C Gonzalez.png')
img.show()
