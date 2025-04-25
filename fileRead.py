
with open('file1.txt', 'r') as file1:
    # file_content = file1.read()
    # print('File content is :\n', file_content)

    # To read specific characters, you can use the read() method with an argument that specifies the number of characters to read. It reads characters starting from the current position of the file pointer.
    character = file1.read(5)  # Read the next 5 characters
    print(character)

    print('while loop begins after this line...')

    while True:
        line = file1.readline()
        if not line:
            break  # Stop when there are no more lines to read
        print(line)


file1.close()