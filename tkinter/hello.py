import tkinter as tk

class window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hello Tkinter")
        #creating label widget and setting its position using pack method        
        self.label =tk.Label(self,text ="Choose One")
        self.label.pack(fill=tk.BOTH, expand=1,padx=100,pady=30)

        #creating button widget,setting position using pack method,calling function using command
        home_button = tk.Button(self,text="Say Hello",command=self.say_hello)
        home_button.pack(side=tk.LEFT,padx=(20,0),pady=(0,20))

        goodbye_button = tk.Button(self,text=("say Goodbye"),command=self.say_goodbye)
        goodbye_button.pack(side=tk.RIGHT,padx=(0,20),pady=(0,20))

    #defing our functions
    def say_hello(self):
        self.label.configure(text="hello World!")
    def say_goodbye(self):
        self.label.configure(text="Goodbye! \n (Closing in 2 seconds)")
        self.after(2000,self.destroy)
if __name__ == "__main__":
    window =window()
    window.mainloop()