# Some file operations

# User input
f_path = input("Please enter file-path: ")

f_name, f_ext = f_path.split(".")

with open(f_path, "rb") as rf:
    with open("{}_copy.{}".format(f_name, f_ext), "wb") as wf:
        for line in rf:
            #some operation...
            wf.write(line)


# for i in range(5):
#     with open("Test_{}.txt".format(i), "wb") as wf:
#         pass