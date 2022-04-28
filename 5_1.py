
file_name = "./infile.txt"
infile = open(file_name, "r")
names = [line.rstrip() for line in infile]

# infile.close()

# def main():
#     display_with_forloop(file_name)
#     print()


# def display_with_forloop(file_name):
#     infile = open_file(file_name, "r")
#     for line in infile:
#         print(line, end="")
#     infile.close()

# def display_with_list_comprehension(file_name):
#     infile = open_file(file_name, "r")
#     items = [line.rstrip() for line in infile]
#     print("items: ", items)
#     infile.close()

# def open_file(file_name, mode):
#     return open(file_name, mode)
# main()


# Create a file object in write mode

# def main():
#     save_to_outfile("./outfile.txt")


# def open_file(file_name, mode):
#     return open(file_name, mode)


# def save_to_outfile(file_name):
#     outfile = open_file(file_name, "w")
#     for name in names:
#         if "Doe" not in name:
#             print("Name to be presisted: ", name)
#             outfile.write(name + "\n")
#         else:
#             print("Names to be exluded: ", name)


# main()
