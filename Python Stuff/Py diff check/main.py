file1 = open("Python Stuff\Py diff check\input1.txt","r")
modslist1 = file1.readlines()
file1.close()

file2 = open("Python Stuff\Py diff check\input2.txt","r")
modslist2 = file2.readlines()
file2.close()


notInm2 = []
notInm1 = []


for i in range(2):
    for m1 in modslist1:
        isInOther = False
        for m2 in modslist2:
            if m2 == m1:
                isInOther = True
        if not isInOther:
            if i == 1:
                notInm2.append(m1)
            else:
                notInm1.append(m1)

output = open("Python Stuff\Py diff check\output.txt","w")
output.write("Mods found in input 1 but not 2")
for mod in notInm2:
    output.write(mod)

output.write("\n")
output.write("Mods found in input 2 but not 1")
for mod in notInm1:
    output.write(mod)
output.close()