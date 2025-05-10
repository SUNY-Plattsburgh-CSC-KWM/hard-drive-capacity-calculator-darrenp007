#Darren Pelletier
#hd capacity calc

def main():
    platters = int(input("Enter the number of platters: "))
    surfaces = int(input("Enter the number of surfaces per platter: "))
    tracks = int(input("Enter the number of tracks per surface: "))
    sectors = int(input("Enter the number of sectors per track: "))
    bytes_per_sector = int(input("Enter the number of bytes per sector: "))

    total_bytes = platters * surfaces
    total_bytes = total_bytes * tracks
    total_bytes = total_bytes * sectors
    total_bytes = total_bytes * bytes_per_sector

    kb = total_bytes / 1024

    if kb > 1.0:
        print("Drive size: {:.1f} KB".format(kb))

    mb = kb / 1024
    if mb > 1.0:
        print("Drive size: {:.1f} MB".format(mb))

    gb = mb / 1024
    if gb > 1.0:
        print("Drive size: {:.1f} GB".format(gb))

    tb = gb / 1024
    if tb > 1.0:
        print("Drive size: {:.1f} TB".format(tb))
        return


main()

#starts by reading inputs
#calculates bytes with multiplication
#conerts to kb,mb,gb, and tb if needed then prints
