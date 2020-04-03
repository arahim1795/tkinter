import tkinter as tk


def my_click(root, entry):
    display_text = "Diplaying: " + entry.get()
    myLabel = tk.Label(root, text=display_text)
    myLabel.pack()


def main():
    root = tk.Tk()

    # # basic
    # e = tk.Entry(root)

    e = tk.Entry(root, width=50, bg="#ffffff")
    e.pack()
    # - input default text
    e.insert(0, "Input Text")

    button_0 = tk.Button(root, text="Display Text", command=lambda: my_click(root, e))
    button_0.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
