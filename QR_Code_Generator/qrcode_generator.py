import qrcode

def generate_qrcode(text):
    
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )
    
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrimg001.png")

def generate_contact_qr(name, email, phone):
    # Create vCard string
    vcard = f"BEGIN:VCARD\nVERSION:3.0\nN:{name}\nEMAIL:{email}\nTEL:{phone}\nEND:VCARD"
    # Generate QR code
    qr = qrcode.QRCode(box_size=10)
    qr.add_data(vcard)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    return qr_img

def generate_wifi_qr(ssid, password):
    # Create Wi-Fi network string
    wifi = f"WIFI:T:WPA;S:{ssid};P:{password};;"
    # Generate QR code
    qr = qrcode.QRCode(box_size=10)
    qr.add_data(wifi)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    return qr_img

# Example usage for contact information
contact_name = "John Doe"
contact_email = "johndoe@example.com"
contact_phone = "+123456789"
contact_qr = generate_contact_qr(contact_name, contact_email, contact_phone)
contact_qr.save("contact_qr.png")

# Example usage for Wi-Fi credentials
wifi_ssid = "MyWiFiNetwork"
wifi_password = "MyPassword123"
wifi_qr = generate_wifi_qr(wifi_ssid, wifi_password)
wifi_qr.save("wifi_qr.png")    

url = input("Enter your url: ")
generate_qrcode(url)
