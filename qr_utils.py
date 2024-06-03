import qrcode
import camera_reader
import image_reader

def create_qr_code(data):
    img_name = "qr.png"
    img = qrcode.make(data)
    img.save(img_name)
    print("QR code created")

def read_qr_code():
    print("To read a QR code from an image, write the name of the image. (For example, \"qr.png\")")
    print("If you want to read from the camera, write \"Cam\"")
    inp = input()
    
    if inp == "Cam":
        # Call camera_reader.py function
        pass
    else:
        # Call image_reader.py function
        pass
