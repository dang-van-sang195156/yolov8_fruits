from tkinter import *

import tkinter as tk

import tkinter as tk
import cv2
from tkinter import Tk, Label, Entry, Listbox, Button, Frame
from PIL import Image, ImageTk
from run_pro import *


def update_label(predicted_classes_list_var, type_fruits):
    
    cc = type_fruits[0]
    if cc == 10: 
        predicted_text = "None"
    elif cc == 0:
        predicted_text = "Apple"
    elif cc == 1:
        predicted_text = "Banana"
    elif cc == 2:
        predicted_text = "Grape"
    elif cc == 3:
        predicted_text = "Orange"
    elif cc == 4:
        predicted_text = "Pineapple"
    elif cc == 5:
        predicted_text = "Watermelon"     
    predicted_classes_list_var.set(f"Predicted Classes:\n \n {predicted_text}")
    



def start_camera():
    def update():
        ret, frame = cap.read()
        results = model(frame, show = True ,conf = 0.3, device = 'cpu')
        predicted_classes_list = []
        for result in results:
        # Lấy thông tin về lớp dự đoán
            predicted_classes = result.boxes.data[:, -1].int()
            #print(type(predicted_classes))
        # Chuyển đổi tensor thành danh sách Python và in ra
            predicted_classes_list = predicted_classes.tolist()

        if len(predicted_classes_list)>0 :
            type_fruits = predicted_classes_list
            numbers_fruits = len(predicted_classes_list)
            #print("so luong phan tu ", numbers_fruits)
        else:
            type_fruits = [10]
        #print("Phan tu ban dau ",type_fruits)

        print("--------------------------------")

        update_label(predicted_classes_list_var, type_fruits)


        root.after(1, update)


    cap = cv2.VideoCapture(0)
    model = YOLO('./best_40epoch.pt')


    update()  # Bắt đầu vòng lặp cập nhật


if __name__ == "__main__":
    root = Tk()
    root.title("Object Detection")
    root.minsize(height= 1180, width=1560)
    predicted_classes_list_var = StringVar()


    L3  = tk.Label(root, textvariable= predicted_classes_list_var, fg="red", font=("Times New Roman", 20), width = 20 )
    L3.place(x= 1100, y= 500)

    Label(root, text="Interfaces Detection", fg="red", font=("Times New Roman", 14), width=20).grid(row=0, pady=10)
    Label(root, text="Type", fg="red", font=("Times New Roman", 14), width=30).grid(row=4, column=0)

    list_box_imgs = Listbox(root, width=100, height=30)
    list_box_imgs.grid(row=1, column=0, columnspan=1, padx=10)


    Label(root, text="Chạy chương trình", fg="red", font=("Times New Roman", 14), width=20).grid(row=2, column=0, pady=35)
    Label(root, text="Dừng chương trình", fg="red", font=("Times New Roman", 14), width=20).grid(row=2, column=1, pady=35)

    # Tạo Label
    label_btl = tk.Label(root, text="Bài tập lớn cuối kì 2023.1", fg="red", font=("Times New Roman", 20), width=20)

    label_btl_2 = tk.Label(root, text="Sinh viên thực hiện:", fg="black", font=("Times New Roman", 14), width=30)
    label_btl_1 = tk.Label(root, text="GVHD: TS.Nguyễn Thành Hùng", fg="black", font=("Times New Roman", 14), width =30)


    label_btl_3 = tk.Label(root, text="Trịnh Thanh Hà: 20207759", fg="black", font=("Times New Roman", 14), width=30)
    label_btl_4 = tk.Label(root, text="Nguyễn Minh Hiếu: 20207760", fg="black", font=("Times New Roman", 14), width=30)
    label_btl_5 = tk.Label(root, text="Mã lớp: 143462", fg="black", font=("Times New Roman", 14), width=30)



    # Đặt vị trí của Label theo pixel
    label_btl.place(x= 1100, y= 100)
    label_btl_1.place(x= 1100, y= 150)
    label_btl_2.place(x= 1100, y= 200)
    label_btl_3.place(x= 1100, y= 250 )
    label_btl_4.place(x= 1100, y= 300 )
    label_btl_5.place(x= 1100, y= 350 )



    button_1 = Frame(root)
    button_2 = Frame(root)

    Button(button_1, text="start", width=20, height=8, command=lambda: start_camera(),font=("Times New Roman", 15), bg = "green").pack(side=LEFT)
    Button(button_2, text="end", width=20, height=8, command=root.quit, font=("Times New Roman", 15) ,bg = "red").pack(side=LEFT)
    button_1.grid(row=3, column=0, padx=10, pady=10)
    button_2.grid(row=3, column=1, padx=10, pady=10)


    
    # Mở ảnh

    img_1 = Image.open("1.jpg")

    # Chuyển ảnh thành đối tượng ImageTk.PhotoImage
    image1 = ImageTk.PhotoImage(img_1)

    # Tạo Label để hiển thị ảnh
    label1 = tk.Label(root, image=image1)
    label1.image = image1  # Đảm bảo giữ tham chiếu đến ảnh

    # Đặt vị trí của Label
    label1.place(x= 850, y= 100)


    root.mainloop()
