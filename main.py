def elso_beado(beker):
    #### mondat bekerese
    beker = beker.lower()
    #### betük gyakorisaganak megszamolasa
    def betu_gyak(beker):
        thisdict = {}
        for x in beker:
            thisdict[x] = beker.count(x)
        return thisdict

    print("Betűk gyakorisága: ", betu_gyak(beker))

    ################# Fordítas
    fordit = beker[::-1]
    print("Fordítva: ", fordit)

    ################ Lista
    thislist = []
    thislist.insert(1, beker.split(" "))
    print("Listába rendezve szavanként: ", thislist)
    #Dupla []-be rakja és nem tudom miért...

if __name__ == '__main__':
    print("Adjon meg egy mondatot:")
    beker = input()
    elso_beado(beker)
