def main():
    filename = "Python Stuff\Py Auto Depend\mods.txt"
    writename = "Python Stuff\Py Auto Depend\dependencies.txt"
    ignorelist = ["TacoTank-TommyFun","FreeCammer","GameMaster"]

    isFirst = True

    fd = open(filename,"r")
    mods = fd.readlines()
    fd.close()
    fd = open(writename,"w")
    for mod in mods:
        ignore = False
        for name in ignorelist:
            if mod.find(name) != -1:
                ignore = True
                break
        if not ignore:
            if isFirst:
                fd.write(f"\"{mod.strip()}\"")
                isFirst = False
            else:
                fd.write(f",\n")
                fd.write(f"\"{mod.strip()}\"")
    print("Done!")
    
main()