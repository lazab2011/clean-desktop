import os
import shutil

#define the function to move the files and folders

def move_desktop_files_to_documents():
    desktop_path = r"C:\Users\path\to\Desktop"

    documents_path = os.path.join(os.path.expanduser('~'), "Documents") 

    #ensure the documents folder exists
    # if the documents folder does not exist, one will be made
    
    if not os.path.exists(documents_path):
        os.makedirs(documents_path)
    
    #List all files and directories on the desktop
    desktop_contents = os.listdir(desktop_path)

    #move each file from the desktop to the Documents

    for item in desktop_contents:
        item_path = os.path.join(desktop_path, item)
        if os.path.isfile(item_path):
            shutil.move(item_path, documents_path)
            print(f"Moved file:{item}")
        elif os.path.isdir(item_path):
            shutil.move(item_path, documents_path)
            print(f"Moved folder: {item}")
    print("All files and folders have been moved from the Desktop to the Documents folder")

if __name__ == "__main__":
    move_desktop_files_to_documents()
