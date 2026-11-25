# -*- coding: utf-8 -*-

def list_str(list1):
    '''
    Convert list into string comma seperated values.

    Parameters
    ----------
    list1 : LIST
        The list entered for conversion.

    Returns
    -------
    Simple String
    '''
    ans = ''
    if list1 != []:
        for index, item in enumerate(list1, start=1):
            item_str = str(item)
            if index == len(list1) - 1:
                ans += item_str + ', and '
            elif index == len(list1):
                ans += item_str
            else:
                ans += item_str + ', '
    else:
        return ""
    
    return ans
    
if __name__ == "__main__":
    spam = ["apples", "bananas", "tofu", "cats"]
    print(list_str(spam))
