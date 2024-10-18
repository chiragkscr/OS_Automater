import os

folder_path = r"C:\Users\Chirag S\Desktop\images"

#List all files in the specified folder
files = os.listdir(folder_path) 

#Filters the filees to include only images/jpg images or any mentioned folder extensions
image_files = [f for f in files if f.endswith(('.jpg'))]


image_files.sort()

#iterate through each image and rename it
for index, filename in enumerate(image_files, start=1):
    #get the full path 
    src = os.path.join(folder_path, filename)

    #Generate a new name
    file_extension = os.path.splitext(filename)[1] #Extract file extension
    new_filename = f"{index}{file_extension}"

    #Generate destination path
    dst = os.path.join(folder_path, new_filename)

    #rename the file
    os.rename(src, dst)
    

