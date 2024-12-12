import os 
def files_in_folders(folder):
   try:
     files = os.listdir(folder)
     return files,None
   except FileNotFoundError:
      return None,"File Not Found"
   except PermissionError:
      return None,"Permission Denied"
      

def main():
    folders = input(f"Enter the folder names with space: ").split()
    for folder in folders:
        files,error_message = files_in_folders(folder)
        if files:
         for file in files:
            print(f"files in folder {folder} are: " + file)
        else:
           print(f"{error_message} found when trying to find files in {folder} folder")
     

if __name__ == "__main__":
  main()
           