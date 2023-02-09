import os
def batch_rename(path, old_extension, new_extension):
    for filename in os.listdir(path):
        # get the file extension
        split_file = os.path.splitext(filename)
        file_extension = split_file[1]
        # only rename files with the specified extension
        if old_extension == file_extension:
            newfile = split_file[0] + new_extension
            os.rename(
                os.path.join(path, filename),
                os.path.join(path, newfile)
            )
batch_rename('/path/to/files', '.old_extension', '.new_extension')
