import qrcode
from tkinter import filedialog, colorchooser, simpledialog, Tk, messagebox

def main():
    # create Tkinter root
    root = Tk()
    root.withdraw() # hide root

    # choose a color
    fill_color = colorchooser.askcolor(title="Set QR code color")[1]
    back_color = colorchooser.askcolor(title="Set background color")[1]

    # Select the file path to save
    file_path = filedialog.asksaveasfilename(defaultextension=".png")

    # Enter the website URL
    url = simpledialog.askstring("Input", "Enter website url:")

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Make the QR code into an image
    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    # Save the image as a file
    img.save(file_path)

    # print success message
    messagebox.showinfo("Success", f"QR code saved as {file_path}")

# execute main function
if __name__ == "__main__":
    main()
