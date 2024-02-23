# QR_Code_Generator_with_GUI.py
This Python script lets the user select a website URL, QR code color, background color, and save path, and then generates a QR code for that website URL. The script uses a graphical user interface (GUI) to accept input from the user.


![스크린샷 2024-02-23 235156](https://github.com/dldbfla/QR_Code_Generator_with_GUI.py/assets/89433437/b89d2f7b-7916-4506-b984-9e9541b6b4a0)
![스크린샷 2024-02-23 235153](https://github.com/dldbfla/QR_Code_Generator_with_GUI.py/assets/89433437/c1e4b5cc-72ab-4c78-b2c3-1e9c546b9542)
![스크린샷 2024-02-23 235134](https://github.com/dldbfla/QR_Code_Generator_with_GUI.py/assets/89433437/fffa5fb6-9e71-4e3d-8c6d-9c2cf6d1f1df)
![스크린샷 2024-02-23 235129](https://github.com/dldbfla/QR_Code_Generator_with_GUI.py/assets/89433437/1e4668df-418d-4ec9-870f-6f481ce0ddc1)
![스크린샷 2024-02-23 235047](https://github.com/dldbfla/QR_Code_Generator_with_GUI.py/assets/89433437/c25bc000-de8e-4d85-a2ca-ec05e6d9aea9)
![스크린샷 2024-02-23 235024](https://github.com/dldbfla/QR_Code_Generator_with_GUI.py/assets/89433437/57dcbb2f-21d9-4a44-9607-c88331658420)
![스크린샷 2024-02-23 235015](https://github.com/dldbfla/QR_Code_Generator_with_GUI.py/assets/89433437/40f0f548-2b11-4d67-bb56-3e81d01db315)

## qrcode: Used to generate QR codes. To install this library, type the following in the terminal

 ```
    pip install qrcode[pil]
 ```

tkinter: Used to generate the GUI. These are included by default in Python 3.x versions, so you don't need to install them separately.


These two libraries must be installed for this Python code to run properly. 

If you need additional libraries, you can install them using the pip install [library_name] command. where [library_name] is the name of the library you want to install.

## Here are some things to keep in mind while using this code

Python version: This code is written to work with Python 3.x versions. Please note that it may not work properly on Python 2.x versions.


Install the required libraries: The qrcode library is required, which can be installed using the pip install qrcode[pil] command. The tkinter library is also required, which is included by default in Python 3.x versions. If you don't have this library installed, you'll need to reinstall Python or install tkinter using the appropriate method.


File save permissions: When saving a file, if you don't have write access to the path to save it, the file save may fail. In this case, you'll need to use a different path or set the appropriate permissions.


Internet connection: The website URL is entered to generate the QR code. Therefore, it is important to enter the correct URL and the behavior may vary depending on your internet connection.


UI language: The UI of the colorchoosercolor and filedialog.asksaveasfilename functions follows the language settings of the operating system. You cannot change the UI language directly in the code.


Please keep these things in mind when using the code.
