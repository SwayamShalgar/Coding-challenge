def swap_case(s):
    res = ""
    for i in s:
        if i.upper()==i:
           res = res+i.lower()
        else:
            res = res+i.upper()
    return res
