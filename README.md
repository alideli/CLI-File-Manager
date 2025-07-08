# File Manager CLI

A simple and flexible command-line tool for managing files and folders. Perform operations like delete, rename, move, copy, list folder contents, and create new folders—all from your terminal.

---

## ✨ Features

- Delete files (by name, date, or format)
- Rename files (batch support)
- Move or copy files (single or multiple)
- Work with files by format (e.g., files with `.jpg`, `.txt`, etc.)
- List contents of a folder
- Create new folders

---

## 🚀 Getting Started

1. **Prerequisites:**  
   Make sure you have **Python 3** installed.

2. **Run the tool:**  
   Open your terminal, navigate to the project directory, and run:
   ```sh
   python main.py [OPTIONS]
   ```

---

## 🛠️ Command-Line Options

| Option / Short         | Description                                                                 | Example                                         |
|------------------------|-----------------------------------------------------------------------------|-------------------------------------------------|
| `--folder_adr`, `-fa`  | Path to the target folder                                                   | `--folder_adr "/path/to/your/folder"`           |
| `--file_adr`, `-fia`   | Path(s) to target file(s)                                                   | `--file_adr "file1.txt" "file2.txt"`            |
| `--remove`, `-r`       | Delete specified files or files by date/format                              | `--remove`                                      |
| `--rename`, `-rn`      | Rename files (provide new names in order)                                   | `--rename "new1.txt" "new2.txt"`                |
| `--show`, `-s`         | List files in a folder                                                      | `--show`                                        |
| `--move`, `-m`         | Move files (provide destination paths in order, or use with date/format)    | `--move "/path/to/dest1" "/path/to/dest2"`      |
| `--copy`, `-c`         | Copy files (provide destination paths in order, or use with date/format)    | `--copy "/path/to/dest1" "/path/to/dest2"`      |
| `--date`, `-d`         | Select files older than or equal to a date (YYYY-MM-DD) for remove/copy/move| `--date 2024-01-01`                             |
| `--format`, `-f`       | Work with files with a specific format (e.g., `jpg`, `txt`, etc.)           | `--format jpg`                                  |
| `--add_folder`, `-af`  | Create a new folder (use with `--folder_adr` to specify parent directory)   | `--add_folder "new_folder"`                     |

---

## 📚 Usage Examples

- **Show all files in a folder:**
  ```sh
  python main.py --folder_adr "/path/to/your/folder" --show
  ```

- **Delete multiple files:**
  ```sh
  python main.py --file_adr "file1.txt" "file2.txt" --remove
  ```

- **Rename files:**
  ```sh
  python main.py --file_adr "old1.txt" "old2.txt" --rename "new1.txt" "new2.txt"
  ```

- **Move files to other folders:**
  ```sh
  python main.py --file_adr "a.txt" "b.txt" --move "/path/to/dest1" "/path/to/dest2"
  ```

- **Delete all files with a specific format in a folder:**
  ```sh
  python main.py --folder_adr "/path/to/your/folder" --remove --format txt
  ```

- **Remove files older than a specific date:**
  ```sh
  python main.py --folder_adr "/path/to/your/folder" --remove --date 2024-01-01
  ```

- **Copy files older than a specific date to another folder:**
  ```sh
  python main.py --folder_adr "/path/to/your/folder" --copy "/path/to/dest" --date 2024-01-01
  ```

- **Move files older than a specific date to another folder:**
  ```sh
  python main.py --folder_adr "/path/to/your/folder" --move "/path/to/dest" --date 2024-01-01
  ```

- **Create a new folder inside a directory:**
  ```sh
  python main.py --folder_adr "/path/to/your/folder" --add_folder "new_folder"
  ```

---

## 💡 Tips

- You can combine `--date` with `--remove`, `--copy`, or `--move` to process files by their last modified date.
- Use `--format` with `--remove`, `--copy`, or `--move` to process files of a specific type.
- For help and all available options:
  ```sh
  python main.py --help
  ```