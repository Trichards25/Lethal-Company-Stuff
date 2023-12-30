def main():
    filename = "mods.txt"
    writename = "dependencies.txt"
    ignorelist = ["TacoTank-TommyFun","FreeCammer","GameMaster"]
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
            fd.write("\"" + mod.strip() + "\"" + ",")
            fd.write("\n")
    print("Done!")
    
main()