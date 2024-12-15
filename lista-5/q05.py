# 5.Entrar com 3 números, e imprimir o maior número

maxNumber = int()

nums = []
nums.append(int(input("> Enter the first number: ")))
nums.append(int(input("> Enter the second number: ")))
nums.append(int(input("> Enter the third number: ")))

if nums[0] > nums[1] and nums[0] > nums[2]:
    maxNumber = nums[0]
elif nums[1] > nums[0] and nums[1] > nums[2]:
    maxNumber = nums[1]
else:
    maxNumber = nums[2]

print(f"> Max value: {maxNumber}.")
