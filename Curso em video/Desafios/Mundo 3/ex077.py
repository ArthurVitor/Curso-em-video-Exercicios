palavras = ('aprender', 'Rcaaranar', 'linguagen', 'python',
            'curso', 'gratis', 'estudar', 'Rcaticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

for p in palavras:
    print(f'\n Na palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')