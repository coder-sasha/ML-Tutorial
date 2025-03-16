"""
When dealing with very large files, you want to avoid loading the entire file into memory. 
A function designed as a generator can yield one file record at a time.
"""

def read_large_file_gen(file_path: str)->str:
    """
    Lazily reads a large file line by line.
    yield: Each line of the file.
    """
    with open(file_path, 'r') as f:
        for line in f:
            yield line

# usage:
if __name__ == '__main__':
    file_path = 'big_file.txt'
    for line in read_large_file_gen(file_path):
        # process each line; for example, print or analyze it.
        print(line.strip())
		
		