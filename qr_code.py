import qrcode
links_input = input("Enter website links separated by commas: ")
version = int(input("Enter the version of the QR code (1-40): "))
box_size = int(input("Enter the box size of the QR code (1-10): "))
border = int(input("Enter the border size of the QR code (1-10): "))
fill_color = input("Enter the fill color of the QR code (e.g. black, red, blue): ")
back_color = input("Enter the background color of the QR code (e.g. white, yellow, green): ")
output_file_name = input("Enter the base name for output files: ")

links = [link.strip() for link in links_input.split(",") if link.strip()]

for idx, website_link in enumerate(links, start=1):
    qr = qrcode.QRCode(version=version, box_size=box_size, border=border)
    qr.add_data(website_link)
    qr.make()
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(f"{output_file_name}_{idx}.png")