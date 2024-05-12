import tkinter as tk 
from tkinter.filedialog import askopenfilename,asksaveasfilename

def open_file(window,text_editor):
    
    file_path=askopenfilename(filetypes=[("Text Files","*.txt")]) 
    
    if not file_path : 
        return
    text_editor.delete(1.0,tk.END) #clearing the text editor starting from(1,0)-1st line and 0th character to END
    with open(file_path, "r") as f:
        content=f.read()
        text_editor.insert(tk.END,content)
    window.title(f"File :{file_path}")

def save_file(window,text_editor):
    file_path=asksaveasfilename(filetypes=[("Text Files","*.txt")])

    if not file_path:
        return
    with open(file_path,"w") as f:
        content=text_editor.get(1.0,tk.END)
        f.write(content)
    window.title(f"Saved file:{file_path}")
    
def close_window(window): #to close the window
    window.destroy()
    




def main() :
    
    #creating a window and frame
    
    window=tk.Tk() 
    window.title("DRText Editor")

    window.rowconfigure(0,minsize=400) 
    window.columnconfigure(1,minsize=400)

    text_editor=tk.Text(window,font="Helvetica 18") #widget for text editor
    text_editor.grid(row=0,column=1) 

    frame=tk.Frame(window,relief=tk.RAISED,bd=2) 

    #Buttons creation

    save_button=tk.Button(frame,text="Save",command=lambda:save_file(window,text_editor)) 
    open_button=tk.Button(frame,text="Open",command=lambda:open_file(window,text_editor)) 
    save_button.grid(row=0,column=0,padx=5,pady=5,sticky="ew") 
    open_button.grid(row=1,column=0,padx=5,sticky="ew") 
    frame.grid(row=0,column=0,sticky="ns") #

    #Applying key bindings
   
    window.bind("<Control-s>",lambda x:save_file(window,text_editor)) 
    window.bind("<Control-o>",lambda x:open_file(window,text_editor)) 
    window.bind("<Control-q>",lambda x:close_window(window)) 
    
   
    window.mainloop() #keep it alive the window until we click the x

main()