# DAY 1:
def func(arr, num):
    for i in range(0, len(arr) - 1):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == num:
                return True

    return False

# DAY 2:


def likes(names):
    if len(names) < 1:
        return 'no one likes this'
    elif len(names) == 1:
        return names[0] + ' likes this'
    elif len(names) == 2:
        return names[0] + ' and ' + names[1] + ' like this'
    elif len(names) == 3:
        return names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this'
    else:
        return names[0] + ', ' + names[1] + ' and ' + str(len(names) - 2) + ' others like this'

# DAY 3:


def camel(s):
    
    chars = s.replace('-', ' ').replace('_', ' ').split(' ')
    res = ''

    for i, c in enumerate(chars):
        if i > 0:
            res += c.capitalize()
        else:
            res += c

    return(res)
