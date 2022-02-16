nums = []

esl = int(input('Quantos numeros você deseja adicionar? '))
for c in range(0, esl):
    num = int(input(f'Digite o {c+1}º numero: '))
    if num not in nums:
        nums.append(num)
print(f'Numeros em ordem crescente {sorted(nums)}')