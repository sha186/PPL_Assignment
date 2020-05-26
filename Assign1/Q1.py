if __name__ == "__main__":
    string1 = input("Enter the entity u want man to take with him \n:1. tiger 2. goat 3. grass\n")
    print(string1, end="\n")
    my_list = ['goat', 'tiger', 'grass']
    my_listf = []
    if string1 == "tiger":
        print("U cant leave goat with grass")
    string1 = input("Enter again:")
    if string1 == "grass":
        print("u cant leave tiger with goat")
    string1 = input("Enter again:")
    if string1 == "goat":
        my_listf.append("goat")
        my_list.remove("goat")
        print(my_list)
        print(my_listf)

    string2 = input("Enter the second entity:\n")
    print(string2, end="\n")
    if string2 == "grass":
        print("u may lose a track")
        string2 = input("Re-enter:\n")
    if string2 == "tiger":
        my_listf.remove("goat")
        my_list.remove("tiger")
        my_listf.append("tiger")
        my_list.append("goat")
        print(my_list)
        print(my_listf)
    # if(string2 == "grass"):
    #   print("U may lose the track: ")
    # string2 = input("Re-enter:")

    string3 = input("Enter the third entity:1.grass 2.goat\n")
    print(string3, end="\n")

    if string3 == "goat":
        print("Better option available\n")
    string3 = input("Re-enter:\n")

    if string3 == "grass":
        my_list.remove("grass")
        my_listf.append("grass")
        print(my_list)
        print(my_listf)

    string4 = input("u are left with one entity :1.goat\n")
    print(string4, end="\n")

    if string4 == "goat":
        my_list.remove("goat")
        my_listf.append("goat")
        print(my_list)
        print(my_listf)
        print("Completed")

