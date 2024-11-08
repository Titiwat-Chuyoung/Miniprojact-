from tkinter import*
import tkinter as tk
from tkinter import ttk
import time
from PIL import Image, ImageTk

window = Tk()
window.geometry("880x800+250+100")
window.title("โปรแกรมคำนวณอย่างง่าย") #ชื่อโปรแกรม
window.configure(background="#00FF99") #สีพื้นหลัง
bg=PhotoImage(file="C:/Users/AUN/OneDrive/Documents/มินิโปรเจ็ค/pngtree-blue-minimalistic-tech-computer-banner-poster-background-picture-image_1083507.png") #ใส่รูปพื้นหลัง
label = Label(window,image=bg ,width = 880 ,height = 200)
label.pack()
bg2=PhotoImage(file="C:/Users/AUN/OneDrive/Documents/มินิโปรเจ็ค/cyber-background-2wcmfxgeg4gnhx7n.png") #ใส่รูปพื้นหลัง
label1 = Label(window,image=bg2)
label1.pack()


def menuInfo():
    windowInfo = Toplevel(window)
    windowInfo.geometry("500x500+250+100")
    windowInfo.title("ผู้จัดทำ")
    windowInfo.configure(background="#FFD000")
    bg1=PhotoImage(file="C:/Users/AUN/OneDrive/Documents/มินิโปรเจ็ค/g5RhES.png") #ใส่รูปพื้นหลัง
    label = Label(windowInfo,image=bg1)
    label.pack()

    label1 = Label(windowInfo,text="ผู้จัดทำ",font=26,fg="blue",bg="#FFD000")
    label1.place(x=250 , y=0)
    label2 = Label(windowInfo,text="1.นายภูฟ้า เเดงเเสละ 654234010",font=26,fg="blue",bg="#FFD000")
    label2.place(x=125 , y=50)
    label2 = Label(windowInfo,text="2.นายณัฐวุฒิ ง๊ะสมัน 654234005",font=26,fg="blue",bg="#FFD000")
    label2.place(x=125 , y=100)
    label2 = Label(windowInfo,text="3.นายฐิติวัสส์  ชูยัง 654234004",font=26,fg="blue",bg="#FFD000")
    label2.place(x=125 , y=150)
    label2 = Label(windowInfo,text="4.นายญามาลุดดีน สุทธิประภา 654234019",font=26,fg="blue",bg="#FFD000")
    label2.place(x=125 , y=200)
    label2 = Label(windowInfo,text="5.นายอับบาส หลีหนุด 654234021",font=26,fg="blue",bg="#FFD000")
    label2.place(x=125 , y=250)
    label2 = Label(windowInfo,text="6.นายพีรพล สรรพกิจผล 654234033",font=26,fg="blue",bg="#FFD000")
    label2.place(x=125 , y=300)
    windowInfo.mainloop()

def menuNext():
    windowNext = Toplevel(window)
    windowNext.title("Sorting Algorithm Visualization")
    scrollbar = ttk.Scrollbar(windowNext, orient="vertical")
    scrollbar.pack(side="right", fill="y")

    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j][1] > arr[j+1][1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    update_display(arr, j, j+1)
                    windowNext.update()
                    time.sleep(1)

    def insertion_sort(arr):
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and key[1] < arr[j][1]:
                arr[j + 1] = arr[j]
                update_display(arr, j, j + 1)
                windowNext.update()
                time.sleep(1)
                j -= 1
            arr[j + 1] = key
            update_display(arr, i, j + 1)
            windowNext.update()
            time.sleep(1)

    def selection_sort(arr):
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j][1] < arr[min_idx][1]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            update_display(arr, i, min_idx)
            windowNext.update()
            time.sleep(1)

    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            merge_sort(left_half)
            merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i][1] < right_half[j][1]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

            update_display(arr, -1, -1)
            windowNext.update()
            time.sleep(1)

    def update_display(arr, idx1, idx2):
        # คำนวณความสูงสูงสุดที่กราฟต้องมี
        max_height = canvas_height - 20

        # คำนวณความสูงของกราฟสำหรับแต่ละรูปภาพ
        max_val = max(arr, key=lambda x: x[1])[1]
        bar_heights = [(val / max_val) * max_height for _, val in arr]

        canvas.delete("all")

        for i, (img, val) in enumerate(arr):
            fill_color = "blue" if i not in [idx1, idx2] else "red"
            
            # คำนวณพิกัด x และ y สำหรับกราฟและรูปภาพ
            x = i * bar_width + 10
            y_bar = canvas_height - bar_heights[i]
            y_text = y_bar - 10
            y_image = canvas_height - int(canvas_height / 4)

            # สร้างกราฟและรูปภาพ
            canvas.create_rectangle(
                x, canvas_height,
                x + bar_width, y_bar,
                fill=fill_color
            )
            canvas.create_text(
                x + bar_width / 2, y_text,
                text=str(val),
                fill="black" if i not in [idx1, idx2] else "black"
            )
            canvas.create_image(
                x + bar_width / 2, y_image,
                image=img
            )

    gifImage = "text.gif"
    openImage = Image.open(gifImage)
    frames = openImage.n_frames
    imageObject = [PhotoImage(file=gifImage, format=f"gif -index {i}") for i in range(frames)]
    count = 0
    showAnimation = None

    def animation(count):
        global showAnimation
        newImage = imageObject[count]

        gif_Label.configure(image=newImage)
        count += 1
        if count == frames:
            count = 0
        
        showAnimation = windowNext.after(50, lambda: animation(count))



    gif_Label = tk.Button(windowNext, image="")
    gif_Label.place(x=155, y=20, width=450, height=500)

    animation(count)

    def sort_data():
        input_data = entry.get()
        sort_algorithm = sort_option.get()

        try:
            input_list = input_data.split()
            if len(input_list) != len(images):
                raise ValueError("Number of numbers must match the number of images")

            data = [(images[i], int(val)) for i, val in enumerate(input_list)]

            if sort_algorithm == "Bubble Sort":
                bubble_sort(data)
            elif sort_algorithm == "Insertion Sort":
                insertion_sort(data)
            elif sort_algorithm == "Selection Sort":
                selection_sort(data)
            elif sort_algorithm == "Merge Sort":
                merge_sort(data)

            result_label.config(text=f"Sorted Data: {[val[1] for val in data]}")
        except ValueError as e:
            result_label.config(text=str(e))
        except Exception:
            result_label.config(text="An error occurred. Please check your input.")

    

    label = tk.Label(windowNext, text="Enter space-separated numbers to sort (must match the number of images):")
    label.pack(pady=10)

    entry = tk.Entry(windowNext)
    entry.pack(pady=5)

    sort_option = tk.StringVar()
    sort_option.set("Bubble Sort")  # เริ่มต้นเลือก Bubble Sort

    sort_label = tk.Label(windowNext, text="Select Sorting Algorithm:")
    sort_label.pack(pady=10)

    sort_dropdown = tk.OptionMenu(windowNext, sort_option, "Bubble Sort", "Insertion Sort", "Selection Sort", "Merge Sort")
    sort_dropdown.pack(pady=5)

    
    gif_Label = tk.Button(windowNext, image="",command=sort_data)
    gif_Label.place(x=450, y=40, width=100, height=100)

    
    result_label = tk.Label(windowNext, text="")
    result_label.pack(pady=10)

    canvas_width = 600
    canvas_height = 400

    canvas = tk.Canvas(windowNext, width=canvas_width, height=canvas_height)
    canvas.pack(pady=10)

    bar_width = 100
    im1 = "C:/Users/AUN/OneDrive/Documents/มินิโปรเจ็ค/png-clipart-laptop-gaming-computer-video-game-desktop-computers-intel-laptop-television-game-thumbnail5.png"
    image_paths = [im1, "C:/Users/AUN/OneDrive/Documents/มินิโปรเจ็ค/png-clipart-laptop-dell-computer-keyboard-computer-monitors-laptop-computer-netbook-computer-keyboard4.png", "C:/Users/AUN/OneDrive/Documents/มินิโปรเจ็ค/png-clipart-black-flat-screen-tv-showing-purple-background-computer-computer-monitor-desktop-computer-lcd-tv-14-computer-violet-ring-purple-television2.png"]  # แทนที่ด้วยที่อยู่และชื่อไฟล์ของรูปภาพของคุณ

    images = [ImageTk.PhotoImage(Image.open(img_path)) for img_path in image_paths]
    
    
    
    windowNext.mainloop()
    
    

        

myMenu = Menu() #เมนูหลัก

myMenu.add_cascade(label="จัดเรียง",command=menuNext)
myMenu.add_cascade(label="ผู้จัดทำ",command=menuInfo)
window.config(menu=myMenu)

image = PhotoImage(file="C:/Users/AUN/OneDrive/Documents/มินิโปรเจ็ค/png-clipart-laptop-gaming-computer-video-game-desktop-computers-intel-laptop-television-game-thumbnail5.png")  # เปลี่ยนเป็นตำแหน่งของรูปภาพของคุณ
image_button = Button(window, image=image,width = 100,height = 50, command=menuNext)
image_button.place(x=10 , y=100)
image1 = PhotoImage(file="C:/Users/AUN/OneDrive/Documents/มินิโปรเจ็ค/png-clipart-laptop-dell-computer-keyboard-computer-monitors-laptop-computer-netbook-computer-keyboard4.png")  # เปลี่ยนเป็นตำแหน่งของรูปภาพของคุณ
image_button1 = Button(window, image=image1,width = 100,height = 50, command=menuNext)
image_button1.place(x=160 , y=100)
image2 = PhotoImage(file="C:/Users/AUN/OneDrive/Documents/มินิโปรเจ็ค/png-clipart-black-flat-screen-tv-showing-purple-background-computer-computer-monitor-desktop-computer-lcd-tv-14-computer-violet-ring-purple-television2.png")  # เปลี่ยนเป็นตำแหน่งของรูปภาพของคุณ
image_button2 = Button(window, image=image2,width = 100,height = 50, command=menuNext)
image_button2.place(x=310 , y=100)
image3 = PhotoImage(file="C:/Users/AUN/OneDrive/Documents/มินิโปรเจ็ค/Light-Keyboard-And-Mouse-PNG-Pic2.png")  # เปลี่ยนเป็นตำแหน่งของรูปภาพของคุณ
image_button3 = Button(window, image=image3,width = 100,height = 50, command=menuNext)
image_button3.place(x=460 , y=100)
image4 = PhotoImage(file="C:/Users/AUN/OneDrive/Documents/มินิโปรเจ็ค/png-clipart-hewlett-packard-dell-all-in-one-desktop-computers-hp-pavilion-hewlett-packard-electronics-computer2.png")  # เปลี่ยนเป็นตำแหน่งของรูปภาพของคุณ
image_button4 = Button(window, image=image4,width = 100,height = 50, command=menuNext)
image_button4.place(x=610 , y=100)
image5 = PhotoImage(file="C:/Users/AUN/OneDrive/Documents/มินิโปรเจ็ค/png-clipart-computer-cases-housings-design-computer-electronic-device2.png")  # เปลี่ยนเป็นตำแหน่งของรูปภาพของคุณ
image_button5 = Button(window, image=image5,width = 100,height = 50, command=menuNext)
image_button5.place(x=760 , y=100)

window.mainloop()
