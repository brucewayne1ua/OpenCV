import qr_utils

def main():
    print("To create a QR code, simply write what you want to encode.")
    print("To read a QR code, write: \"Read\"")
    print("To exit, type exit")

    data = ""

    while data != "exit":
        data = input()
        
        if data != "Read":
            qr_utils.create_qr_code(data)
        else:
            qr_utils.read_qr_code()

if __name__ == "__main__":
    main()
