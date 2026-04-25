import sys


def main() -> None:
    argv = sys.argv[1:]
    my_dict = {}
    for i in argv:
        try:
            if ":" in i:
                key = ""
                value = ""
                first = 0
                for x in i:
                    if x != ":" and first == 0:
                        key += x
                    elif first == 1 or x == ":":
                        first = 1
                        if x == ":":
                            continue
                        value += x
                if key not in my_dict:
                    my_dict[key] = int(value)
                else:
                    print(f"Redundant item {key} - discarding")
            else:
                print(f"Error - invalid parameter {i}")
        except Exception as e:
            print(f"Quantity error for {key}:{e}")
    print(f"Got inventory: {my_dict}")
    lst1 = list(dict.keys(my_dict))
    lst2 = list(dict.values(my_dict))
    print(f"Item list: {list(dict.keys(my_dict))}")
    print(f"Total quantity of the {len(lst1)} items: {sum(lst2)}")
    for i in lst1:
        print(f"Item {i} represents"
              f"{round((my_dict[i] / sum(lst2) * 100), 1)}%")
    max = my_dict[lst1[0]]
    for i in lst1:
        if my_dict[i] >= max:
            max = my_dict[i]
            name = i
    print(f"Item most abundant: {name} with quantity {max}")
    min = my_dict[lst1[0]]
    for i in lst1:
        if my_dict[i] <= min:
            min = my_dict[i]
            name = i
    print(f"Item least abundant: {name} with quantity {min}")
    my_dict.update({'magic_item': 1})
    print(f"Updated inventory: {my_dict}")


if __name__ == "__main__":
    main()
