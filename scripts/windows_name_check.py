import os
import sys

# Windows Reserved Characters
RESERVED_CHARS = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']

def check_names(directory):
    for root, dirs, files in os.walk(directory):
        for name in dirs + files:
            if any(char in name for char in RESERVED_CHARS):
                print(f"Found: {os.path.join(root, name)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <dir>")
        sys.exit(1)
    check_names(sys.argv[1])