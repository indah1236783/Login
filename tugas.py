import tkinter as tk
from tkinter import messagebox

master = tk.Tk()
master.title("Program Login Mahasiswa")

tk.Label(master, text="Username").grid(row=0, column=0)
tk.Label(master, text="Password").grid(row=1, column=0)
e1 = tk.Entry(master)
e2 = tk.Entry(master, show="*")

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
def login():
    try:
        username = e1.get()
        password = e2.get()
        if username.isdigit():
            messagebox.showwarning("Peringatan", "username harus berupa huruf!")
            return
        if not password.isdigit():
            messagebox.showwarning("Peringatan", "password harus berupa angka!")
            return
        if username == "indah" and password == "12345678":
            messagebox.showinfo("Info","Login Berhasil")
        else:
            messagebox.showerror("Info","Login Gagal")
    except Exception as e:
        messagebox.showerror("Error",f"Terjadi Kesalahan : {e}")
bt_login = tk.Button(master, text="Login", command=login)
bt_login.grid(row=2, column=0, columnspan=2, pady=10)
tk.mainloop()