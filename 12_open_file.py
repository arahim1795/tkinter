import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


def open(root):
    global resized
    root.filename = filedialog.askopenfilename(
        initialdir="./resource/img",
        title="Select File(s)",
        filetypes=(("JPG", "*.jpg"), ("JPEG", "*.jpg *.jfif"), ("All types", "*.*"),),
    )

    tk.Label(root, text=root.filename).pack()
    img = Image.open(root.filename)
    resized = ImageTk.PhotoImage(img.resize((800, 600), Image.ANTIALIAS))
    tk.Label(root, image=resized).pack()


def main():
    root = tk.Tk()
    root.title("Open File Dialog Box")

    tk.Button(root, text="Open Image", command=lambda: open(root)).pack()

    root.mainloop()


if __name__ == "__main__":
    main()
