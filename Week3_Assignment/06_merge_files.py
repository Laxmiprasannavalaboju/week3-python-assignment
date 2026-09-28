with open("practice2_file1.txt", "r") as file1:
    content1 = file1.read()

with open("practice2_file2.txt", "r") as file2:
    content2 = file2.read()

with open("merged.txt", "w") as output:
    output.write(content1)
    output.write("\n")
    output.write(content2)

print("Files merged successfully!")