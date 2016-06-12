# -*- coding: utf-8 -*-

from urllib.parse import quote

p = ('남양주시')
quote(p)
print(p)

code = input("당신이 URL 인코딩할 구문을 삽입하시오...\n: ")

for encode in code:
    hexnum = hex(ord(encode))
    new_hexnum = str(hexnum)
    new_hexnum = new_hexnum[2] + new_hexnum[3]
    print("%", end="")
    print(new_hexnum, end="")