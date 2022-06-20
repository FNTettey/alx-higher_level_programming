#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """returns a list of elements in list 1 divided by list 2.
    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.
    Returns:
        A new list of length list_length containing all the divisions.
    """
    new_list = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except (IndexError):
            print("out of range")
            div = 0
        except (TypeError):
            print("wrong type")
            div = 0
        except (ZeroDivisionError):
            print("division by 0")
            div = 0
        finally:
            new_list.append(div)
    return(new_list)