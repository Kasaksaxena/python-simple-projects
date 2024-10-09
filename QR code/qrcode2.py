import qrcode 
from PIL import Image


 

qr=qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H,#accrately read even if qr exposed wear and tear
        box_size=12,
        border=3
)

qr.add_data("https://www.youtube.com/@wscubetech")#use to add the data that u want to encoded
qr.make(fit=True)#make method in qr code lib use to generate qrcode and fit ensures that qrcode generates should 
#adjust  the size of data optimally even if size varies
 
img=qr.make_image(fill_color="blue",back_color="white").convert("RGBA")#generates image of qr code
img.save("q.png")  