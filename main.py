import qrcode
url=input("Enter the Url: ").strip() # catching users information to make qr cod
file_path="C:\\Users\\user\\OneDrive\\Desktop\\qr_code.png" #where to be saved on laptop

qr=qrcode.QRCode() #create qr code object

qr.add_data(url) # add content to qr code you just created

img=qr.make_image()   #generating qr code image
img.save(file_path) # save our qr code on our computer location
