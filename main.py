import tkinter as tk
from tkinter import PhotoImage, scrolledtext
from tkinter import RIGHT,TOP,messagebox,Menu,filedialog,Toplevel, Label, Button
from ground import Ground
from utility import Utility
import winsound
import threading

root=tk.Tk()
ut=Utility()

header_label = tk.Label(root, text="👨‍💻", font=("Arial", 24))
header_label.pack(side=tk.TOP, fill=tk.X)
# create the message label
message_label = tk.Label(root, text="Internet not available")

def showInfo(): 
    # Create a new window 
    newwin = Toplevel(root) 
  
    # Set the new window's title 
    newwin.title("Sonic Assistant - Contact Details") 
  
    # Set the size of the window 
    newwin.geometry("900x250") 

    # Add a label to the window 
    Label(newwin, text = "We are excited to announce the launch of our new software!\n\n\n Our software is designed to help you streamline your business processes and increase efficiency. \n\n  If you would like more information about our software, please contact us at vickychhetri4@gmail.com or 919780553734. We look forward to hearing from you\n\n\n\nSincerely,\n\n Chhetri Software Productions\n\n").pack() 

     # Create a button to close the window  
    Button(newwin, text = "Close", command = newwin.destroy).pack()  

def start_thread():
    thread = threading.Thread(target=get_input)
    thread.start()
def save_file():
    content = output_container.get("1.0",'end-1c') # get content from text entry widget 

    file = filedialog.asksaveasfile(mode='w', defaultextension=".txt") # open save as file dialog

    if file is None: # if no file chosen then return 
        return

    file.write(content) # write content to the file and close it 
    file.close() 
# function to retrieve the input from the entry widget
def get_input():
    if (ut.is_internet_available()):
        user_input = entry.get("1.0",'end-1c')
        if user_input=="":
            return 
        button.config(state="disabled")
        lbl.config(text="Loading...") # change the label text to "Loading..."
        winsound.PlaySound('button_pressed.mp3', winsound.SND_FILENAME)
        # sleep(4)
        manager=Ground()
        manager.setQuery(user_input)    
        response=manager.getQuery()
        # print("User entered:", user_input)
        # append the input to the scrolled text widget
        output_container.insert(tk.END, "\n\nQUESTION: " + user_input+"\n\n")
        output_container.insert(tk.END, "REPLY: " + response.choices[0]['text'] + "\n")
        output_container.see(tk.END)
        entry.delete("1.0",'end')
        button.config(state="normal")
        lbl.config(text="")
    else:
        # hide the submit button and show the message label
        button.pack_forget()
        message_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# create a scrolled text widget
output_container = scrolledtext.ScrolledText(root, width=100, height=20)

output_container.pack(ipadx=10,ipady=10)
# create a label
label = tk.Label(root, text=" 🔔 Ask your question  :")
label.pack()
# create an entry widget
entry = tk.Text(root, width=100,height=4)
entry.pack(padx=10, pady=10)

lbl = tk.Label(root, text ="") 
lbl.pack() 
# create a button to get the input
button = tk.Button(root, text=" 👉🏻 Submit", command=start_thread)
button.pack(padx=10,pady=10)

copyright_text=tk.Label(root,text="Software Develop by Chhetri Software Productions.")
copyright_text.pack(padx=10,pady=10)
photo =PhotoImage(file="coding.png")

menu_bar= Menu(root)
file_menu=Menu(menu_bar,tearoff=0)
help_menu=Menu(menu_bar,tearoff=0)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_command(label="Exit",command=root.quit)
menu_bar.add_cascade(label="File",menu=file_menu)

help_menu.add_command(label="Support",command=showInfo)
menu_bar.add_cascade(label="Help",menu=help_menu)
root.config(menu=menu_bar)
# menu_bar.pack()
root.title("Sonic Assistant")
root.geometry("900x600")

root.iconphoto(False,photo)
root.resizable(False, False)
root.mainloop()