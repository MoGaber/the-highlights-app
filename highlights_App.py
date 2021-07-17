import tkinter as tk #importing tkinter to build your App
from tkinter import Tk
from tkinter import ttk

import os


class Application(tk.Tk): #building a class called Application and making it the child of tk.Tk so
                          # that it inherits all of its attributes      
    
    def __init__(self): 
        tk.Tk.__init__(self) #initializing Tkinter
        self.geometry('200x200') #setting the dimension of the App
        self.title('the_Highlights App') #title of the App
        container = tk.Frame(self)
        container.pack()
        self.frames = {}
        
        for F in (startpage, page1):
            frame = F(parent = container, controller = self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show(startpage)
    def show(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class startpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        create_button = tk.Button(self, text = "Create a New Study Session",
                                  command = lambda : controller.show(page1))
        create_button.pack(pady=6, padx=6)

        open_button = tk.Button(self, text = "Open an Existing Study Session",
                                command = lambda : controller.show(page1))
        open_button.pack(pady=6, padx=6)

        
class page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Highlight_button = tk.Button(self, text = "Highlight", command = self.highlight)
        Highlight_button.pack(pady=6, padx=6)

        generate_button = tk.Button(self, text = "Generate",
                                    command = self.generate)
        generate_button.pack(pady=6, padx=6)

    def highlight(self):
        file_object = open('store.txt', 'a')
        root = Tk()
        root.withdraw()
        content = root.clipboard_get()
        file_object.write(" "+content)
        file_object.close()


    def generate(self):
        
        os.system('cmd /c "python generator2.py > study_quizes.txt"')
        os.system('cmd /c "python generator1.py > study_concepts.txt"')
        #"""
        popup = tk.Tk()
        popup.geometry("200x200")
        popup.wm_title("!")
        label = ttk.Label(popup, text="Highlights Ready \n")
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Open Study Concepts", command = open_concepts)
        B1.pack()
        
        labe2 = ttk.Label(popup, text="\n")
        labe2.pack(side="top", fill="x", pady=10)
        
        B2 = ttk.Button(popup, text="Start a Study Quiz", command = open_quiz)
        B2.pack()
                
        labe3 = ttk.Label(popup, text="\n")
        labe3.pack(side="top", fill="x", pady=10)
        
        popup.mainloop()
        #"""
        

        
def open_concepts():
    os.startfile("study_concepts.txt")
    
def open_quiz():
    os.startfile("study_quizes.txt")
  







#starting the App:
app = Application()
app.mainloop()
