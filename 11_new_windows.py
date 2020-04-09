import tkinter as tk
from PIL import Image, ImageTk


def open(root):
    global resized  # possibly due to some garbage collection
    top = tk.Toplevel()
    top.title("Top")
    img = Image.open("./resource/img/mountain_0.jpg")
    resized = ImageTk.PhotoImage(img.resize((800, 600), Image.ANTIALIAS))
    tk.Label(top, image=resized).pack()

    tk.Button(top, text="Close Window", command=top.destroy).pack()


def main():
    root = tk.Tk()
    root.title("New Windows")

    btn = tk.Button(root, text="Open Top", command=lambda: open(root))
    btn.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
