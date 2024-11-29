import os
import shutil
import send2trash
import zipfile

# 1. Copying Files and Directories
shutil.copy('source.txt', 'destination.txt')  # Copy file
shutil.copytree('source_folder', 'destination_folder')  # Copy entire directory

# 2. Moving Files/Directories
shutil.move('source.txt', 'new_location.txt')  # Move or rename file

# 3. Deleting Files and Directories
os.unlink('file.txt')  # Delete a file
os.rmdir('empty_folder')  # Delete empty folder
shutil.rmtree('non_empty_folder')  # Delete folder with contents

# 4. Safely Deleting Files
send2trash.send2trash('important_file.txt')  # Send to recycle bin

# 5. Traversing Directory Trees
for foldername, subfolders, filenames in os.walk('start_folder'):
    print(f"Folder: {foldername}")
    print(f"Subfolders: {subfolders}")
    print(f"Files: {filenames}")

# 6. File Metadata and Renaming
print(os.path.getsize('file.txt'))  # Get file size
print(os.listdir('folder'))  # List contents of directory
os.rename('old_name.txt', 'new_name.txt')  # Rename a file

# 7. Zipping Files
# Create a ZIP file and add files
with zipfile.ZipFile('example.zip', 'w') as zipf:
    zipf.write('file.txt', compress_type=zipfile.ZIP_DEFLATED)

# Extract files from a ZIP archive
with zipfile.ZipFile('example.zip', 'r') as zipf:
    zipf.extractall('destination_folder')

# Create ZIP archive of a directory
shutil.make_archive('archive_name', 'zip', 'source_folder')

# Unpack ZIP archive to a directory
shutil.unpack_archive('archive_name.zip', 'destination_folder')
