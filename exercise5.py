def jie_while(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

num = int(input("enter the number: "))
print(f"{num}  {jie_while(num)}")
