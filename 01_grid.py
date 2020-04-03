import tkinter as tk


def main():
    root = tk.Tk()

    # flow 1
    label_0 = tk.Label(root, text="1!")
    label_1 = tk.Label(root, text=" ")
    label_2 = tk.Label(root, text="2!")

    # - grid
    # -- relative to one another
    # -- ignore empty rows/columns (must be filled with placeholder text to force unignore)
    label_0.grid(row=0, column=0)
    label_1.grid(row=1, column=1)
    label_2.grid(row=1, column=2)

    # # flow 2
    # label_0 = tk.Label(root, text="1!").grid(row=0, column=0)

    root.mainloop()


if __name__ == "__main__":
    main()
