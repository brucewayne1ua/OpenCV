import cv2
import webbrowser
import re

def read_from_image(image_path):
    img = cv2.imread(image_path)
    detector = cv2.QRCodeDetector()
    data, _, _ = detector.detectAndDecode(img)
    
    if re.search(r'((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])',data):
        webbrowser.open_new(data)
    else:
        print("Message from QR code:", data)
