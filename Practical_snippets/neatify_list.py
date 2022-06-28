def neatify_list(my_list: list):
    if my_list[0] != my_list[-1]:
        items_but_last = [i for i in my_list[:-1]]
        output = f"{', '.join(items_but_last)} and {my_list[-1]}"
    else:
        output = my_list[0]
    return output
