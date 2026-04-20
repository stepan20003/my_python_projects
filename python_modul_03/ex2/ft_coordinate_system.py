import math
def get_player_pos():
    while True:
        try:
            x=[float(x) for x in input("Enter new coordinates as floats in format 'x,y,z':")]
            break
        except ValueError:
            print("Invalid syntax")
    print ("ok")
get_player_pos()
