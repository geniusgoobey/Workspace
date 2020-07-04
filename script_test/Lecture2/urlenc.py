def urlenc(text):
    result = ""
    for c in text:
        result += hex(ord(c)).replace('0x', '%')
    return result
print(urlenc("test"))


def func(number):
    if number > 10:
        return "That's a big number"
    return "That's a small number"

print(func(3))
print(func(13))