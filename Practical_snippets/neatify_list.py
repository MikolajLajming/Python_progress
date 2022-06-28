def neatify_list(my_list: list):
    """Changes string into a list separated by commas, last item is separated by 'and'"""
    items_but_last = []
    if my_list[0] != my_list[-1]:
        for i in my_list[:-1]:
            items_but_last.append(i)
        output = f"{', '.join(items_but_last)} and {my_list[-1]}"
    else:
        output = my_list[0]
    return output
