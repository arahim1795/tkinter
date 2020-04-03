import tkinter as tk


def main():
    root = tk.Tk()

    # create a label widget
    myLabel = tk.Label(root, text="Hello World!")
    # put to screen as is
    myLabel.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
