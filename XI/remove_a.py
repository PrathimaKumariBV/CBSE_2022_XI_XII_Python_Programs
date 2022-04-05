#Remove all the lines that contain the character 'a' in a file and write it to another file
import os

with open("sample_file.txt",'r+') as file_obj_read:
    file_content=file_obj_read.readlines()
    file_obj_read.truncate()

with open("temp_file.txt",'w') as file_obj_write:

    for line in file_content:
        if 'a' in line:
            file_obj_write.write(line)
            
with open ("sample_file.txt",'w') as file_update:

    for line in file_content:
        if 'a' in line:
            line=""

        file_update.write(line)
   



        