#!/usr/bin/python3i
def delete_at(my_list=[], idx=0):
    for i in range(len(my_list)):
        if i != idx:
            new_list.append(my_list[i])
    my_list[:] = new_list
    return my_list
    if idx < 0 or idx >= len(my_list):
        return my_list
