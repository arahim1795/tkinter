import tkinter as tk
from PIL import ImageTk, Image


def c_prev(root, img_num):
    global imgs
    global my_label
    global status
    global b_prev
    global b_next

    my_label.grid_forget()

    my_label = tk.Label(image=imgs[img_num - 1])
    my_label.grid(row=0, column=0, columnspan=3)
    b_prev = tk.Button(root, text="<<", command=lambda: c_prev(root, img_num - 1))
    b_next = tk.Button(root, text=">>", command=lambda: c_next(root, img_num + 1))

    if img_num == 1:
        b_prev = tk.Button(root, text="<<", state=tk.DISABLED)

    b_prev.grid(row=1, column=0)
    b_next.grid(row=1, column=2)

    status = tk.Label(
        root,
        text="Img " + str(img_num) + " of " + str(len(imgs)),
        bd=1,
        relief=tk.SUNKEN,
        anchor=tk.E,
    )
    status.grid(row=2, column=0, columnspan=3, sticky=tk.W + tk.E)


def c_next(root, img_num):
    global imgs
    global my_label
    global status
    global b_prev
    global b_next

    my_label.grid_forget()
    my_label = tk.Label(image=imgs[img_num - 1])
    my_label.grid(row=0, column=0, columnspan=3)
    b_prev = tk.Button(root, text="<<", command=lambda: c_prev(root, img_num - 1))
    b_next = tk.Button(root, text=">>", command=lambda: c_next(root, img_num + 1))

    if img_num == 3:
        b_next = tk.Button(root, text=">>", state=tk.DISABLED)

    b_prev.grid(row=1, column=0)
    b_next.grid(row=1, column=2)

    status = tk.Label(
        root,
        text="Img " + str(img_num) + " of " + str(len(imgs)),
        bd=1,
        relief=tk.SUNKEN,
        anchor=tk.E,
    )
    status.grid(row=2, column=0, columnspan=3, sticky=tk.W + tk.E)


def main():
    root = tk.Tk()
    root.title("Image Viewer: Status Bar")

    global imgs
    imgs = []
    for i in range(3):
        original = Image.open("./resource/img/mountain_" + str(i) + ".jpg")
        resized = original.resize((800, 600), Image.ANTIALIAS)
        imgs.append(ImageTk.PhotoImage(resized))

    global status
    status = tk.Label(
        root, text="Img 1 of " + str(len(imgs)), bd=1, relief=tk.SUNKEN, anchor=tk.E
    )

    global my_label
    my_label = tk.Label(image=imgs[0])
    my_label.grid(row=0, column=0, columnspan=3)

    b_prev = tk.Button(
        root, text="<<", command=lambda: c_prev(root, 2), state=tk.DISABLED
    )
    b_exit = tk.Button(root, text="Exit", command=root.quit)
    b_next = tk.Button(root, text=">>", command=lambda: c_next(root, 2))

    b_prev.grid(row=1, column=0)
    b_exit.grid(row=1, column=1)
    b_next.grid(row=1, column=2, pady=10)
    status.grid(row=2, column=0, columnspan=3, sticky=tk.W + tk.E)

    root.mainloop()


if __name__ == "__main__":
    main()
