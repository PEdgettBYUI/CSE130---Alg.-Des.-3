def compute_tax (income):
    ''' Compute the tax burden based on income. '''
    tax = -1.0 

    assert type(income) == int or type(income) == float, "Income must be a int or float"
    assert income >= 0, "Income is negative"

 
    # 10% bracket.
    if 0 <= income < 15100:
        tax = income * 0.10
        assert 0 <= tax <= 1510, "Income not within 10% Bracket margins"
    # 15% bracket.
    elif 15100 <= income < 61300:
        tax = 1510 + 0.15 * (income - 15100)
        assert 1510 <= tax <= 8440, "Income not within 15% Bracket margins"
    # 25% bracket.
    elif 61300 <= income < 123700:
        tax = 8440 + 0.25 * (income - 61300)
        assert 8440 <= tax <= 24040, "Income not within 25% Bracket margins"
    # 28% bracket.
    elif 123700 <= income < 188450:
        tax = 24040 + 0.28 * (income - 123700)
        assert 24040 <= tax <= 42170, "Income not within 28% Bracket margins"
    #33% bracket.
    elif 188450 <= income < 336550:
        tax = 42170 + 0.33 * (income - 188450)
        assert 42170 <= tax <= 91043, "Income not within 33% Bracket margins"
    #35% bracket.
    elif income >= 336550:
        tax = 91043 + 0.35 * (income - 336550)
        assert 91043 <= tax, "Income not within 35% Bracket margins"

    assert tax != -1.0

    return tax

x = float(input("> "))
print(compute_tax(x))


def binary_search(array, search):
    ''' Return TRUE if search exists in array. '''

    # Initialize the bounding indices.
    i_first = 0
    i_last = len(array) - 1

    assert i_first(type) == type(array[i_first])
    assert i_last(type) == type(array[i_last])
    assert len(array) >= 0
    if __debug__:
        len_save = len(array)

    # Continue as long as there are elements in the range.
    while i_first <= i_last:
        i_middle = (i_first + i_last) // 2

        assert 0 <= i_first <= i_middle <= i_last < len(array)
        # assert array[0] <= array[] <= array[] <= array[]
        assert type(search) == type(array[i_middle])

        # Too high or too low.
        if array[i_middle] < search:
            i_first = i_middle + 1
        elif array[i_middle] > search:
            i_last = i_middle - 1

        # Found!
        else:
            assert len_save == len(array)
            assert array[i_middle] == search, "The value is not at this index"
            return True

    # Not found!
    assert len_save == len(array)
    assert array[i_middle] == search
    assert not search in array, "The value is not in the array"
    return False


def compute_tax(income):
    ''' Compute the tax burden based on income. '''

    brackets = [
    #    min     max       fixed  rate 
        ( 0,     15100,    0,     0.10),
        ( 15100, 61300,    1510,  0.15),
        ( 61300, 123700,   8440,  0.25),
        (123700, 188450,   24040, 0.28),
        (188450, 336500,   42170, 0.33),
        (336500, 99999999, 91043, 0.35)
    ]

    assert type(income) == float or type(income) == int
    assert 0 <= income

    for bracket in brackets:
        assert len(bracket) == 4, "Not a valid data set format"
        assert bracket[0] < bracket[1], "Max is higher than Min"
        assert 0.0 <= bracket[3] <= 1.0, "Not a valid Percentage"
        assert 0 <= bracket[2] <= bracket[1], "Fixed should not be more than Max"
        
        if bracket[0] <= income and bracket[1] >= income:
            return bracket[2] + bracket[3] * (income - bracket[0])
    
    assert False
    return 0.0

assert compute_tax(15100) == 1510
assert compute_tax(61300) == 8440
assert compute_tax(123700) == 24040
assert compute_tax(188450) == 42170
assert compute_tax(334500) == 91043
