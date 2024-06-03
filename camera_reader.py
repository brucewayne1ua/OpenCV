import cv2
import webbrowser
import re

def read_from_camera():
    windowName = "QR code detector cam"
    cv2.namedWindow(windowName)
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()
    oldData = ""
    count = 0
    
    while True:
        _, img = cap.read() 
        data, _, _ = detector.detectAndDecode(img) 
        
        if data and data != oldData:
            if re.search(r'((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])',data):
                webbrowser.open_new(data)
            else:
                print("Message from QR code:", data)
            oldData = data
        
        img = cv2.flip(img, 1)
        cv2.imshow(windowName, img)
        count += 1
        
        if count == 100:
            oldData = ""
            count = 0
        
        if cv2.waitKey(1) & 0xFF == 27:
            break
                
    cap.release()
    cv2.destroyAllWindows()
