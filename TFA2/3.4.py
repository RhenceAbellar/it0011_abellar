f=open('TFA2/students.txt', 'r')
print ('Reading Student Information:\n')
while True:
    try:
        line=next(f)
        print(line)
    except StopIteration:
        break
f.close ()
