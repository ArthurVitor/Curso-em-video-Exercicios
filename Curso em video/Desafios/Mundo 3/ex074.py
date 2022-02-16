import random as rd

nums = rd.randint(1,10), rd.randint(1,10), rd.randint(1,10), rd.randint(1,10), rd.randint(1,10)
print(f'Listagem da tupla {nums} \n'
      f'O maior valor na tupla foi de {max(nums)} \n'
      f'E o menor foi {min(nums)}')