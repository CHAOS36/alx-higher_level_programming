#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n_list = []
    for i in range(list_length):
        try:
            pipox = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            pipox = 0
        except ZeroDivisionError:
            print("division by 0")
            pipox = 0
        except IndexError:
            print("out of range")
            pipox = 0
        finally:
            n_list.append(pipox)
    return n_list
