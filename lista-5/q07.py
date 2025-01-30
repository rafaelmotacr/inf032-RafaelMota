# 7.entrar com 3 números e armazená-los em três variáveis diferentes:
# maior, menor e intermediário
maxNumber = int()

nums = list()
nums.append(int(input("> Enter the first number: ")))
nums.append(int(input("> Enter the second number: ")))
nums.append(int(input("> Enter the third number: ")))
nums.sort()

max = nums[2]  
min = nums[0]
avg = nums[1]

print(f"> Max number: {max}.")
print(f"> Avg number: {avg}.")
print(f"> Min number: {min}.")
