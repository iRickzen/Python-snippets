# File name
import os

# User input
f_path = input("Please enter file-path: ")
if not f_path: f_path = os.getcwd()

os.chdir(f_path)

for f in os.listdir():
    #for each file in directory
    f_name, f_ext = os.path.splitext(f)

    try:
        f_name1, f_num = f_name.split("_")
        f_name1 = f_name1.strip()
        f_num = f_num.strip().zfill(2)

        f_name_new = "{}-{}{}".format(f_num,f_name1,f_ext)
        print(f_name_new)

        os.rename(f, f_name_new)
    except:
        pass