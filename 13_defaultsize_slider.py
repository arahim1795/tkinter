import tkinter as tk


def slide(value):
    global root
    root.geometry(str(value) + "x400")


def manual_slide(slider):
    global root
    tk.Label(root, text=slider.get()).pack()
    root.geometry(str(slider.get()) + "x400")


def main():
    global root
    root = tk.Tk()
    root.title("Default Window Size, Slider")

    # default window size: horizontal by vertical
    root.geometry("400x400")

    # scale: must separate pack
    vertical = tk.Scale(root, from_=0, to=100)
    vertical.pack()

    # # command to dynamically update: though not advised for resizing windows
    # horizontal = tk.Scale(root, from_=400, to=800, orient=tk.HORIZONTAL, command=slide)
    
    horizontal = tk.Scale(root, from_=400, to=800, orient=tk.HORIZONTAL)
    horizontal.pack()

    # manual update
    tk.Button(root, text="Get Value", command=lambda: manual_slide(horizontal)).pack()

    root.mainloop()


if __name__ == "__main__":
    main()
