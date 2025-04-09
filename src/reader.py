"""
Aaron Perkel
reader.py script
"""

import os

def read_crns(file_path):
    """Reads CRNs from a text file, ignoring empty and '#' lines."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, file_path)
    
    with open(file_path, 'r') as file:
        # Remove whitespace, ignore blank lines, and skip lines starting with '#'
        return [line.strip() for line in file if line.strip() and not line.strip().startswith('#')]

def main():
    # Use the directory of this script to form the path to crns.txt
    CRNS = read_crns('./crns.txt')
    print(CRNS)
        
if __name__ == '__main__':
    main()