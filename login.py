import tkinter
from tkinter import messagebox
window=tkinter.Tk()
window.title('Login page using python')
window.geometry('750x550')
window.configure(bg='#8F00FF')
def login():
    username='aswani'
    password='123456'

    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title='Login Successfull',message='Your log in Sucessfully.')
        
    else:
            messagebox.showerror(title='Error',message='Invalid login.')
frame=tkinter.Frame(bg='#8F00FF')
login_label = tkinter.Label(frame, text="Login Page Using Python",   font=("Arial", 30))
username_label = tkinter.Label(frame, text="Username", bg='#8F00FF', fg="#FFFFFF", font=("Arial", 16, 'bold'))
password_label = tkinter.Label(frame, text="Password", bg='#8F00FF', fg="#FFFFFF", font=("Arial", 16, 'bold'))

username_entry = tkinter.Entry(frame, font=("Arial", 16))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))



login_button = tkinter.Button(frame, text="Login", bg="#DC143C", fg="#FFFFFF", font=("Arial", 16), command=login)
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)
frame.pack()
window.mainloop()
