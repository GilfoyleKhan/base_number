result=[]
def base10_to_other_base(n,base):#n must be in decimal number(base 10)
    while n!=0:
        current_n=n
        n=n//base
        balance=(n*base)-current_n
        result.append(abs(balance))
    return result[::-1]
print(base10_to_other_base(29,8))
# ---------------------------------
"""not finished yet
def other_to_base10(n,base):
    new_n=str(n);numbers_n=[]
    for i in str(new_n):
        numbers_n.append(int(i))
    print(numbers_n)
print(other_to_base10(37,10))
"""