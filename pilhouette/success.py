import tkinter as tk
from tkinter import ttk

class Success(tk.Frame):
    def __init__(self, master, controller, address):
        tk.Frame.__init__(self, master)
        self.master = master
        self.controller = controller
        self.address = address
        self.create_widgets()
    def create_widgets(self):
        self.label_thankyou = ttk.Label(self, text="Thank you for using Pilhouette!")
        self.label_thankyou.grid(row=0,column=0, columnspan=2, sticky="news")

        self.label_success = ttk.Label(self, text="Email sent successfully to {}".format(self.address))
        self.label_success.grid(row=1, column=0, sticky="news")

        self.button_toggle = ttk.Button(self)
        self.button_toggle.grid(row=1,column=1, sticky="news")
        self.address_toggle(False)

        self.label_spam = ttk.Label(self, text="If you don't see our email, be sure to check your spam folder in case it was incorrectly caught by a spam filter.")
        self.label_spam.grid(row=2, column=0, columnspan=2, sticky="news")

        self.label_timer = ttk.Label(self, text="Restarting in 10 seconds...")
        self.label_timer.grid(row=3, column=0, columnspan=2, sticky="news")
        self.countdown(10)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        #self.row_configure(0, weight=1)
    def address_toggle(self, visible): # boolean, true if currently visible
        if visible: # hide the address
            self.label_success.config(text="Email sent successfully")
            self.button_toggle.config(text="Show address", command=lambda:self.address_toggle(not visible)) # not visible == False
        else: # show the address
            self.label_success.config(text="Email sent successfully to {}".format(self.address))
            self.button_toggle.config(text="Hide address", command=lambda:self.address_toggle(not visible)) # not visible == True
    def countdown(self, seconds):
        if seconds > 0:
            self.label_timer.config(text="Restarting in {} seconds...".format(seconds))
            self.master.after(1000, lambda:self.countdown(seconds-1))
        else:
            self.controller.home()

