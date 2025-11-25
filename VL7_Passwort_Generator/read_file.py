def load_lines_from_file(file_path):
    with open(file_path) as f:
        lines = f.readlines()
        cleaned_lines = [line.rstrip() for line in lines]
    
    return cleaned_lines

# absolute path
# On Windows: \\ instead of /
path = "/Path/to/file/nomen.txt"
lines = load_lines_from_file(path)
print(lines)

    