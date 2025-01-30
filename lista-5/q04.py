# 4.Entrar com 2 números e imprimir o maior número

nums = list()
nums.append(int(input("> Enter the first number: ")))
nums.append(int(input("> Enter the second number: ")))
print(f"> Max value: {nums[0] if nums[0] > nums[1] else nums[1]}.")
