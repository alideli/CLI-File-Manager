import os
import shutil
import datetime
from utils import is_supported_formats

def handle_file_operations(arguments):
    if arguments.date and arguments.folder_adr:
        try:
            user_date = datetime.datetime.strptime(arguments.date, "%Y-%m-%d").date()
            if arguments.remove:
                for file in os.listdir(arguments.folder_adr):
                    file_path = os.path.join(arguments.folder_adr, file)
                    if os.path.isfile(file_path):
                        file_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path)).date()
                        if file_modified_time <= user_date:
                            os.remove(file_path)
                            print(f"File removed: {file_path}")
            if arguments.copy:
                for file in os.listdir(arguments.folder_adr):
                    file_path = os.path.join(arguments.folder_adr, file)
                    if os.path.isfile(file_path):
                        file_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path)).date()
                        if file_modified_time <= user_date:
                            for dest in arguments.copy:
                                dest_path = os.path.join(dest, file) if os.path.isdir(dest) else dest
                                shutil.copy2(file_path, dest_path)
                                print(f"File copied: {file_path} -> {dest_path}")
            if arguments.move:
                for file in os.listdir(arguments.folder_adr):
                    file_path = os.path.join(arguments.folder_adr, file)
                    if os.path.isfile(file_path):
                        file_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path)).date()
                        if file_modified_time <= user_date:
                            for dest in arguments.move:
                                dest_path = os.path.join(dest, file) if os.path.isdir(dest) else dest
                                shutil.move(file_path, dest_path)
                                print(f"File moved: {file_path} -> {dest_path}")
        except Exception as e:
            print("Date parsing failed:", e)

    elif arguments.remove:
        if arguments.file_adr and not arguments.date:
            for f in arguments.file_adr:
                if os.path.isfile(f):
                    os.remove(f)
                    print(f"File removed: {f}")

    if arguments.rename:
        if len(arguments.file_adr) != len(arguments.rename):
            print("Number of old files and new names must be equals")
        else:
            for old_path_r, new_name_r in zip(arguments.file_adr, arguments.rename):
                without_name = os.path.dirname(old_path_r)
                new_path = os.path.join(without_name, new_name_r)
                if os.path.isfile(old_path_r):
                    os.rename(old_path_r, new_path)
                    print(f"File renamed: {old_path_r} -> {new_path}")

    if arguments.move and arguments.file_adr and not arguments.format and not arguments.date:
        if len(arguments.file_adr) != len(arguments.move):
            print("Number of source files and move destinations must be equal")
        else:
            for old_path_m, new_path_m in zip(arguments.file_adr, arguments.move):
                if os.path.isdir(new_path_m):
                    new_path_m = os.path.join(new_path_m, os.path.basename(old_path_m))
                if os.path.isfile(old_path_m):
                    shutil.move(old_path_m, new_path_m)
                    print(f"File moved: {old_path_m} -> {new_path_m}")

    if arguments.copy and arguments.file_adr and not arguments.format and not arguments.date:
        if len(arguments.file_adr) != len(arguments.copy):
            print("Number of source files and copy destinations must be equal")
        else:
            for old_path_c, new_path_c in zip(arguments.file_adr, arguments.copy):
                if os.path.isdir(new_path_c):
                    new_path_c = os.path.join(new_path_c, os.path.basename(old_path_c))
                if os.path.isfile(old_path_c):
                    shutil.copy2(old_path_c, new_path_c)
                    print(f"File copied: {old_path_c} -> {new_path_c}")

    if arguments.format and arguments.folder_adr:
        if arguments.remove:
            for file in os.listdir(arguments.folder_adr):
                if is_supported_formats(file, arguments.format):
                    file_path = os.path.join(arguments.folder_adr, file)
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                        print(f"File removed: {file_path}")
        if arguments.move:
            for file in os.listdir(arguments.folder_adr):
                if is_supported_formats(file, arguments.format):
                    old_p = os.path.join(arguments.folder_adr, file)
                    for dest in arguments.move:
                        if os.path.isdir(dest):
                            new_p = os.path.join(dest, file)
                        else:
                            new_p = dest
                        if os.path.isfile(old_p):
                            shutil.move(old_p, new_p)
                            print(f"File moved: {old_p} -> {new_p}")
        if arguments.copy:
            for file in os.listdir(arguments.folder_adr):
                if is_supported_formats(file, arguments.format):
                    old_p = os.path.join(arguments.folder_adr, file)
                    for dest in arguments.copy:
                        if os.path.isdir(dest):
                            new_p = os.path.join(dest, file)
                        else:
                            new_p = dest
                        if os.path.isfile(old_p):
                            shutil.copy2(old_p, new_p)
                            print(f"File copied: {old_p} -> {new_p}")