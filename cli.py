import argparse

def get_arguments():
    parser = argparse.ArgumentParser(description="Welcome, This program is a file manager. use --help to see commands.", epilog="I hope you enjoyed using this file manager")
    parser.add_argument("--folder_adr", "-fa", help="enter the file directory that you want to work with files in it")
    parser.add_argument("--file_adr", "-fia", type=str, nargs="+", help="enter file directory like \"...\" to remove, rename, copy, move")
    parser.add_argument("--remove", "-r", help="use to remove files", action="store_true")
    parser.add_argument("--rename", "-rn", help="use to rename files", nargs="+")
    parser.add_argument("--show", "-s", help="use to show files in folder", action="store_true")
    parser.add_argument("--move", "-m", help="use to move files, enter destination in here", nargs="+")
    parser.add_argument("--copy", "-c", help="use to copy files, enter destination in here", nargs="+")
    parser.add_argument("--date", "-d", help="use to remove files from a date brfore \"YYYY-MM-DD\"")
    parser.add_argument("--format", "-f", help="use to organize files (copy, move, remove) files", choices=["jpg","jpeg","png","exe","xlsx","docx","pdf","txt","py","mp3","wav","mp4","mkv"])
    parser.add_argument("--add_folder", "-af", help="you can create new folder")
    return parser.parse_args()