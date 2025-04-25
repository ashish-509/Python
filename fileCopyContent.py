# Copying contents from one file to another

with open ('fileSource.txt', 'r') as sourceFile:
    with open ('fileDestination.txt', 'w') as destinationFile:
        for line in sourceFile:
            destinationFile.write(line)
