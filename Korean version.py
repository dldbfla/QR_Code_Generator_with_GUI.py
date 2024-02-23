import qrcode
from tkinter import filedialog, colorchooser, simpledialog, Tk, messagebox

def main():
    # Tkinter root 생성
    root = Tk()
    root.withdraw()  # root 숨기기

    # 색상 선택
    fill_color = colorchooser.askcolor(title="qr코드 컬러 설정")[1]
    back_color = colorchooser.askcolor(title="배경 컬러 설정")[1]

    # 저장할 파일 경로 선택
    file_path = filedialog.asksaveasfilename(defaultextension=".png")

    # 웹사이트 URL 입력
    url = simpledialog.askstring("Input", "Enter website url:")

    # QR 코드 생성
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # QR 코드를 이미지로 만듦
    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    # 이미지를 파일로 저장
    img.save(file_path)

    # 성공 메시지 출력
    messagebox.showinfo("Success", f"QR code saved as {file_path}")

# 메인 함수 실행
if __name__ == "__main__":
    main()

