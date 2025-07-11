import os

def handle_folder_operations(arguments):
    if(arguments.add_folder and arguments.folder_adr):
        if(isinstance(arguments.add_folder, list)):
            folder_names = arguments.add_folder
        else:
            folder_names = [arguments.add_folder]
        for folder in (folder_names):
            new_folder_path = os.path.join(arguments.folder_adr, folder)
            if(os.path.exists(new_folder_path)):
                print(f"Error  ====> Folder already exists: {new_folder_path}")
            else:
                try:
                    os.mkdir(new_folder_path)
                    print(f"Folder created: {new_folder_path}")
                except Exception as e:
                    print("Error While creating folder:", e)

    if arguments.folder_adr and arguments.show:
        try:
            if os.path.isdir(arguments.folder_adr):
                files = os.listdir(arguments.folder_adr)
                print(f"Files in {arguments.folder_adr}:")
                for file in files:
                    print(file)
            else:
                print("No such file directory")
        except Exception as e:
            print("Error while accessing folder:", e)