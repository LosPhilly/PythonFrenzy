import hashlib

def hash_file(file_path):
    BUF_SIZE = 65536
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as file:
        buf = file.read(BUF_SIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = file.read(BUF_SIZE)
    return hasher.hexdigest()
file_path = 'file.txt'
print(f'Hash of {file_path}: {hash_file(file_path)}')
