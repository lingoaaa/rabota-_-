def polin(pol):
    if pol[::-1]==pol:
        return True
    else:
        return False
print(polin(input('Введите слово:')))