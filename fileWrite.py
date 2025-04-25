
with open ('file2.txt', 'w') as file2:
    file2.write('this is line A\n')
    file2.write('this is line B\n')
    # file1 is automatically closed when the 'with' block exits


# Writing multiple lines with while loop : 
lines = ['Line1', 'Line2', 'Line3']
with open ('file3.txt', 'w') as file3:
    for line in lines:
        file3.write(line + '\n')


# Appending data to an existing file:
with open ('file3.txt', 'a') as file3:
    file3.write('This is the appended line.\n')

