for x in reversed (range(1, 6)):
    print(x)

print("Blastoff!")


while True:
    line = input('>Goodbye World!')
    if line == 'done' :
        break
    print (line)
print ('Done!')


while True:
    line = input('>We coming back!')
    if line[0] == '#' :
        continue
    if line == 'done' :
        break
        print (line)
print('Done!')