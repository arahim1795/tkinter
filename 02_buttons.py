import tkinter as tk


def my_click(root):
    myLabel = tk.Label(root, text="Look! A Clicked Button")
    myLabel.pack()


def main():
    root = tk.Tk()

    # # basic
    # button_0 = tk.Button(root, text="Click Me!")\

    # function
    button_0 = tk.Button(root, text="Click Me!", command=lambda: my_click(root))

    # # parameter
    # # - padx: add padding to left and right
    # # - pady: add padding to top and bottom
    # # - fg: change text colour
    # # - bg: change button colour (accepts hex colour)
    # button_0 = tk.Button(root, text="Click Me!", padx=50)

    # # disabled button
    # button_0 = tk.Button(root, text="Click Me!", state=tk.DISABLED)

    button_0.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
