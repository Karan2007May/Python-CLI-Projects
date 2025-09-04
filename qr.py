import qrcode

data = input("Enter text to generate QR code: ")
qr = qrcode.make(data)
qr.show()
