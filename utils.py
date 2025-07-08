def is_supported_formats(filename, user_format):
    return filename.lower().endswith(f".{user_format.lower()}")