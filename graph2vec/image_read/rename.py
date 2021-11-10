import os
dir = "/home/pei/Documents/yi_liu/graph2vec/image_read/40_nm/Done"
all_file = []
for filename in os.listdir(dir):
    all_file.append(filename)
#    if filename.endswith(".asm") or filename.endswith(".py"): 
#         # print(os.path.join(directory, filename))
#        continue
#    else:
#        continue
# print(all_file)

for file in all_file:
    if " " in file:
        os.rename(file, file.replace(" ", "_"))
        print(file)