from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("IMAGE VIEWER")
root.iconbitmap("C:/Users/Bilal Atiq/PycharmProjects/imageViewerGUI/image_viewer.ico")

img1 = ImageTk.PhotoImage(Image.open("C:/Users/Bilal Atiq/PycharmProjects/imageViewerGUI/images/1.jpg"))
img2 = ImageTk.PhotoImage(Image.open("C:/Users/Bilal Atiq/PycharmProjects/imageViewerGUI/images/2.jpg"))
img3 = ImageTk.PhotoImage(Image.open("C:/Users/Bilal Atiq/PycharmProjects/imageViewerGUI/images/3.jpg"))
img4 = ImageTk.PhotoImage(Image.open("C:/Users/Bilal Atiq/PycharmProjects/imageViewerGUI/images/4.jpg"))
img5 = ImageTk.PhotoImage(Image.open("C:/Users/Bilal Atiq/PycharmProjects/imageViewerGUI/images/5.jpg"))

image_list = [img1, img2, img3, img4, img5]

my_label = Label(image=img3)
my_label.grid(row=0, column=0, columnspan=3)


def imageBack(img_next):

    global my_label
    global next_Btn
    global back_Btn

    my_label.grid_forget()
    my_label = Label(image=image_list[img_next - 1])
    my_label.grid(row=0, column=0, columnspan=3)
    next_Btn = Button(root, text="Next", command=lambda: imageNext(img_next + 1))
    back_Btn = Button(root, text="Back", command=lambda: imageBack(img_next - 1))

    if img_next == 1:
        next_Btn = Button(root, text="Next", state=DISABLED)

    back_Btn.grid(row=1, column=0)
    next_Btn.grid(row=1, column=2)


def imageNext(img_next):

    global my_label
    global next_Btn
    global back_Btn

    my_label.grid_forget()
    my_label = Label(image=image_list[img_next - 1])
    my_label.grid(row=0, column=0, columnspan=3)
    next_Btn = Button(root, text="Next", command=lambda: imageNext(img_next + 1))
    back_Btn = Button(root, text="Back", command=lambda: imageBack(img_next - 1))

    if img_next == 5:
        next_Btn = Button(root, text="Next", state=DISABLED)

    back_Btn.grid(row=1, column=0)
    next_Btn.grid(row=1, column=2)


next_Btn = Button(root, text="Next", command=lambda : imageNext(1))
exit_Btn = Button(root, text="Exit Viewer", command=root.quit)
back_Btn = Button(root, text="Back", command=imageBack, state=DISABLED)

back_Btn.grid(row=1, column=0)
exit_Btn.grid(row=1, column=1)
next_Btn.grid(row=1, column=2)



root.mainloop()
