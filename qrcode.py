
import qrcode
from PIL import Image
from pystyle import Colorate, Colors

print(Colorate.Vertical(Colors.red_to_blue, """ 
 ██████╗ ██████╗      ██████╗ ██████╗ ██████╗ ███████╗
██╔═══██╗██╔══██╗    ██╔════╝██╔═══██╗██╔══██╗██╔════╝
██║   ██║██████╔╝    ██║     ██║   ██║██║  ██║█████╗  
██║▄▄ ██║██╔══██╗    ██║     ██║   ██║██║  ██║██╔══╝  
╚██████╔╝██║  ██║    ╚██████╗╚██████╔╝██████╔╝███████╗
 ╚══▀▀═╝ ╚═╝  ╚═╝     ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝
                                                      """))
dat = input(Colorate.Horizontal(Colors.red_to_blue, "введи ссылку: " ))
qrcode = qrcode.QRCode(version=None,
                       error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=10,
                       border=4)
qrcode.add_data(dat)
qrcode.make(fit=True)

img = qrcode.make_image(fill_color ="black", back_color ="white")
img.show()

