ascii0 = """\
*****
*   *
*   *
*   *
*****\
"""
ascii1 = """\
    *
    *
    *
    *
    *\
"""
ascii2 = """\
*****
    *
*****
*
*****\
"""

ascii3 = """\
*****
    *
*****
    *
*****\
"""


ascii4 = """\
*   *
*   *
*****
    *
    *\
"""

ascii5 = """\
*****
*
*****
    *
*****\
"""
ascii6 = """\
*
*
*****
*   *
*****\
"""

ascii7 = """\
*****
    *
    *
    *
    *\
"""

ascii8 = """\
*****
*   *
*****
*   *
*****\
"""

ascii9 = """\
*****
*   *
*****
    *
*****\
"""

num = int(input())

if num == 0:
    print(ascii0)
elif num == 1:
    print(ascii1)
elif num == 2:
    print(ascii2)
elif num == 3:
    print(ascii3)
elif num == 4:
    print(ascii4)
elif num == 5:
    print(ascii5)
elif num == 6:
    print(ascii6)
elif num == 7:
    print(ascii7)
elif num == 8:
    print(ascii8)
elif num == 9:
    print(ascii9)


