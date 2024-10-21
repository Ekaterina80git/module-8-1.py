

def add_everything_ap(a,b):
    try:
        x = round(a + b,3)
        return x
    except TypeError:
        return f'{a}{b}'


print(add_everything_ap(123.456 ,'строка'))
print(add_everything_ap('яблоко' ,4215))
print(add_everything_ap(123.456,7))