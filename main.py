from cli import get_arguments
from file_ops import handle_file_operations
from folder_ops import handle_folder_operations

def main():
    args = get_arguments()
    handle_file_operations(args)
    handle_folder_operations(args)

if __name__ == "__main__":
    main()