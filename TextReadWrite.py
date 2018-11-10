
with open('measurements.txt', 'r') as f:

    #for line in f:
    #    print(line, end = '')

    size_to_read = 10
    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:     
        print(f_contents, end = '')
        f_contents = f.read(size_to_read)



with open('measurements.txt' , 'a') as f1:
    f1.write('Test')
    f1.seek
