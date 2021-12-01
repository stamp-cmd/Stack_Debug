# Import Library
from os import path
from sys import argv
from webbrowser import open_new_tab
from tkinter import messagebox

# Set Messagebox title
Title = "Stack Debug"

def trystack (file):
    # Read script of file
    with open(file, 'r') as script:
        content = script.read()
    try:
        print("Executing Code...")
        exec(content)
        print("Executing Successfull.")
        messagebox.showinfo(Title, "Code runs successfully")
    except Exception as err:
        print("Error Found.")
        messagebox.showwarning(Title, f"Error found: {err}")
        print("Redirecting to stackoverflow...")
        # Redirect to stackoverflow with error
        open_new_tab(f"https://stackoverflow.com/search?q={err}")
        print("Redirected.")

def main():
    print("===Stack Debug===Debug Using Stackoverflow===")
    try:
        # Get drop file
        drop_file = argv[1]
        print("File Dropped.")
        file_path = drop_file.replace("\\", "/")
        extension = path.splitext(drop_file)[1]
        # Check file extension
        if extension == ".py":
            trystack(file_path)
        else:
            messagebox.showerror(Title, "File extension not support")
    except IndexError:
        print("No File Found")
        messagebox.showerror(Title, "No file dropped")

if __name__ == "__main__":
    main()
