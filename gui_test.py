import tkinter as Tk
import numpy as np

class Begueradj(Tk.Frame):
   def __init__(self,parent):
      Tk.Frame.__init__(self, parent)
      self.parent = parent
      self.initialize()

   def initialize(self):
      '''
      Draw the GUI
      '''
      self.parent.title("RUN ON START TEST")       
      self.parent.grid_rowconfigure(1,weight=1)
      self.parent.grid_columnconfigure(1,weight=1)

      self.frame = Tk.Frame(self.parent)  
      self.frame.pack(fill=Tk.X, padx=5, pady=5)

      # Create a 6x7 array of zeros as the one you used
      self.a = np.zeros((6,7))
      for i in range(0,self.a.shape[0]):
          for j in range(0,self.a.shape[1]):
               self.b = Tk.Button(self.frame, text = 'Hello')
               self.b.grid(row=i,  column= j)

# Start the main program here               
if __name__ == "__main__": 
   root=Tk.Tk()
   app = Begueradj(root)   
   root.mainloop()