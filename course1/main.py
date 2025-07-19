from functools import reduce


def total(*args):
    total = 0
    for n in args:
        if type(n) != int and type(n) != float:
            continue
        total += n
    print(total)


total(3,'s',5)

def information(**kwargs):
    for key in kwargs.keys():
        print(key,":", kwargs[key])


information(name= 'elnaz', familyName= 'morad')

def finalAmount(amount, tax = 18, discount = 10): 
    discounted_amount = (amount * tax) / 100
    taxed_amount = (amount - discounted_amount) * tax / 100
    final = (amount - discounted_amount) + taxed_amount
    return final


# amount = input('please input amount')


add_ten = lambda x: x + 10
print(add_ten(10))

numbers = [1,2,3,4]
res = reduce(lambda x,y: x+y, numbers)
print(res)