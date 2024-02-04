# Name: Saphal Pant
# Date: 1/31/2024
#Description: The Reckoner

from tkinter import *
from button_data import button_data


WIDTH = 450
HEIGHT = 650

class MainGUI(Frame):
    
    def __init__(self,parent):
        Frame.__init__(self, parent, bg='white')
        # parent.attributes("-fullscreen", True)
        self.setupGUI()
        
        
    def setupGUI(self):
        self.display = Label(
            self,
            text="",
            anchor=E,
            bg="white",
            fg="black",  #text
            height=1,
            font = ("TexGyreAdventor", 40)
        )
        
        self.display.grid(
            row=0,
            column=0,
            columnspan=4,
            sticky=NSEW
        )
        
        for row in range(6):
            Grid.rowconfigure(self, row, weight=1)
        
        for col in range(6):
            Grid.columnconfigure(self, col, weight=1)
            
        for button in button_data:
            self.make_button(button["row"], button["column"], button['columnspan'], button["value"])
            
        self.pack(fill=BOTH, expand=1)
    
    def make_button(self, row, col, columnspan, value):
        bg_color = "#dddddd"
        
        if value=="=":
            bg_color = "light blue"
            
        if value in ["(", ")", "AC", "**", "/", "*", "+", "-","%", "del"]:
            bg_color="#999999"
            
            
        button = Button(
            self,
            font=("TexGyreAdventor", 30),
            text=value,
            fg="black",
            bg=bg_color,
            highlightbackground=bg_color,
            borderwidth=0.5,
            highlightthickness=0,
            width=5,
            command=lambda: self.process(value)
        )
        
        button.grid(row=row, column=col, columnspan=columnspan, sticky=NSEW)
        
    def clear_display(self):
        self.display["text"] = ""
    
    def set_display(self,value):
        if(len(value)>14):
            self.display["text"] = value[0:11]+"..."
        else:
            self.display["text"]=value
            

    
    def append_display(self, value):
        if(len(self.display["text"])<14):
            self.display["text"] +=value

    
    def evaluate(self):
        pass
    
    def process(self, button):
        if (button=="AC"):
            self.clear_display()
        elif(button=="del"):
            if (self.display["text"]!="ERROR"):
                self.display["text"] = self.display["text"][0:-1]
            else:
                self.clear_display()
        elif (button=="="):
            expr = self.display["text"]
            try:
                result = eval(expr)
                self.set_display(str(result))
            except:
                self.display['text'] = "ERROR"
        else:
            if (self.display['text']=="ERROR"):
                self.set_display(button)
            else:
                self.append_display(button)
##MAIN

window = Tk()
window.title("The Reckoner")
window.geometry(f"{WIDTH}x{HEIGHT}")
p = MainGUI(window)
window.mainloop()
    
    