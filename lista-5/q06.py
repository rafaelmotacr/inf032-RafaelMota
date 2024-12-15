# 6.entrar com 3 números e imprimi-los em ordem crescente

maxNumber = int()

nums = list()
nums.append(int(input("> Enter the first number: ")))
nums.append(int(input("> Enter the second number: ")))
nums.append(int(input("> Enter the third number: ")))
nums.sort()

print(f"> Ordered List: {nums}.")
