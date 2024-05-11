from tkinter import *  #Import tkinter library
from tkinter.filedialog import askopenfilename, asksaveasfilename  #Import file dialog functions

def create_new_file():  #Define function to create new file
    content = text_widget.get(1.0, END)  #Get content from text box
    if not content:  #If text box is empty, then return
        return
    save_file()  #Call function to save file

def open_existing_file():  #Define function to open existing file
    file_path = askopenfilename(title='Open Document', filetypes=[('Text Document', "*.txt"), ("py file", "*.py")])  #Open file dialog
    print(file_path)  #Print file path
    if not file_path:  #If file path is empty, then return
        return
    content = open(file_path).read()  #Read file content
    text_widget.insert("1.0", content)  #Insert file content into text box
    root.title("%s - Notepad" % file_path.split('/')[-1])  #Set window title as file name

def save_file():  #Define function to save file
    file_path = asksaveasfilename(title='Save As', initialfile='Untitled.txt', filetypes=[("Text Document", "*.txt")], defaultextension='.txt')  #Open save file dialog
    print(file_path)  #Print file path
    if not file_path:  #If file path is empty, then return
        return
    with open(file_path, 'w') as file:  #Open file in write mode
        file.write(text_widget.get(1.0, END))  #Write text box content to file
    text_widget.delete(1.0, END)  #Clear text box
    root.title("%s - Notepad" % file_path.split("/")[-1])  #Set window title as file name

def save_as_other_file():  #Define function to save as other file
    pass

def add_expense_record():  #Define function to add expense record
    record_window = Toplevel(root)  #Create a top-level window
    record_window.title("Expense Record")  #Set window title

    def save_record():  #Define function to save record
        date = date_entry.get()  #Get content from date entry box
        amount = amount_entry.get()  #Get content from amount entry box
        record_data = f"Date: {date}, Amount: {amount}\n"  #Format record data
        text_widget.insert(END, record_data)  #Insert record data into text box

    date_label = Label(record_window, text="Date:")  #Create date label
    date_label.grid(row=0, column=0, padx=5, pady=5)  #Set date label position
    date_entry = Entry(record_window)  # Create date entry box
    date_entry.grid(row=0, column=1, padx=5, pady=5)  # Set date entry box position

    amount_label = Label(record_window, text="Amount:")  # Create amount label
    amount_label.grid(row=1, column=0, padx=5, pady=5)  # Set amount label position
    amount_entry = Entry(record_window)  #Create amount entry box
    amount_entry.grid(row=1, column=1, padx=5, pady=5)  #Set amount entry box position

    save_button = Button(record_window, text="Save", command=save_record)  #Create save button
    save_button.grid(row=2, columnspan=2, pady=10)  #Set save button position

def open_help():  #Define function to open help
    help_window = Toplevel(root)  #Create a top-level window
    help_window.title("HELP")  #Set window title
    help_text = "The application is a simple memo application built using Python's Tkinter library. It provides a user-friendly interface for creating, opening and saving text files. It also includes functionality to record income and expenses. "  #Help text
    help_label = Label(help_window, text=help_text)  #Create help label
    help_label.pack()  #Display help label

def open_about():
    about_window = Toplevel(root)
    about_window.title("About Us")
    about_text = "This is a memo application. You can enter memos in the text box. This application also includes tools for recording income and expenses."
    about_label = Label(about_window, text=about_text)
    about_label.pack()

root = Tk()  #Create a window
root.title("Untitled - Notepad")  #Set window title
root.geometry("300x200+1000+300")  #Set window size and position
root.configure(bg='sky blue')  #Set background color to sky blue

menu_bar = Menu(root, bg='violet')  #Create menu bar, set background color to violet
root.config(menu=menu_bar)  #Set window menu bar

file_menu = Menu(menu_bar, tearoff=0, bg='violet')  #Create file menu, set background color to violet
file_menu.add_command(label="New", accelerator='Ctrl + N', command=create_new_file)  #Add new menu item
file_menu.add_command(label="Open", accelerator="Ctrl + O", command=open_existing_file)  #Add open menu item
file_menu.add_command(label="Save", accelerator="Ctrl + S", command=save_file)  #Add save menu item
file_menu.add_command(label="Save As", accelerator="Ctrl + S", command=save_as_other_file)  #Add save as menu item
file_menu.add_separator()  #Add separator
file_menu.add_command(label="Exit", command=root.quit)  #Add exit menu item
menu_bar.add_cascade(label="File", menu=file_menu)  #Add file menu to menu bar

#Add table menu
table_menu = Menu(menu_bar, tearoff=0, bg='violet') #Create help menu, set background color to violet
table_menu.add_command(label="Add Table", command=add_expense_record)  #Add add table menu item
table_menu.add_separator()  #Add separator
menu_bar.add_cascade(label="Table", menu=table_menu)  #Add help menu to menu bar

#Add help menu
help_menu = Menu(menu_bar, tearoff=0, bg='violet')  #Create help menu, set background color to violet
help_menu.add_command(label="User Manual", command=open_help)  #Add user manual menu item
help_menu.add_command(label="About App", command=open_about)
menu_bar.add_cascade(label="Help", menu=help_menu)  #Add help menu to menu bar

text_widget = Text(root, bg='sky blue')  #Create text box, set background color to sky blue
text_widget.pack(expand=YES, fill=BOTH)  #Display text box

root.mainloop()  #Enter message loop


