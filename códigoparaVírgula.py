def formatar_lista(lista):
    if len(lista) == 0:
        return ""
    elif len(lista) == 1:
        return lista[0]
    else:
        # Use join para combinar todos os itens, exceto o último, separados por ", "
        # e adicione "and" antes do último item
        return ', '.join(lista[:-1]) + ' and ' + lista[-1]

# Exemplo de uso com a lista "spam"
spam = ['apples', 'bananas', 'tofu', 'cats']
resultado = formatar_lista(spam)
print(resultado)
