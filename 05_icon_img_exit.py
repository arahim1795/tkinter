import tkinter as tk
from PIL import ImageTk, Image


def main():
    root = tk.Tk()
    root.title("Icons, Images and Exit Button")

    # favicon
    root.iconbitmap("./resource/favicon.ico")

    # image
    my_img = ImageTk.PhotoImage(Image.open("./resource/mountain.png"))
    my_label = tk.Label(image=my_img)
    my_label.pack()

    # exit program
    button_quit = tk.Button(root, text="Exit", command=root.quit)
    button_quit.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
