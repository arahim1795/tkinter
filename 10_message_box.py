import tkinter as tk
from tkinter import messagebox


def popup(root):
    # showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

    response = messagebox.showinfo("Popup: Title", "Hello World!")  # return string, "ok"
    # response = messagebox.showwarning("Popup: Title", "Hello World!")  # return string, "ok"
    # response = messagebox.showerror("Popup: Title", "Hello World!")  # return string, "ok"
    # response = messagebox.askquestion("Popup: Title", "Hello World!")  # return string, "yes": yes, return "no": no
    # response = messagebox.askokcancel("Popup: Title", "Hello World!")  # return bool, 1: ok, 0: cancel
    # response = messagebox.askyesno("Popup: Title", "Hello World!")  # return bool, 1: yes, 0: no
    tk.Label(root, text=response).pack()
    print(type(response))
    # if response:
    #     tk.Label(root, text="You clicked Yes").pack()
    # else:
    #     tk.Label(root, text="You clicked No").pack()


def main():
    root = tk.Tk()
    root.title("Message Box")

    tk.Button(root, text="Popup", command=lambda: popup(root)).pack()

    root.mainloop()


if __name__ == "__main__":
    main()
