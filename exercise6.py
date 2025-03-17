def jie_for(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

num = int(input("enter the number: "))
print(f"{jie_for(num)}")
