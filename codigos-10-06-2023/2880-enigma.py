def comparaPalavras(palavra1, palavra2):
    for i in range(len(palavra1)):
        if palavra1[i] == palavra2[i]:
            return 0
    return 1

cript = input()
crib = input()
chok = 0

for i in range(len(cript)-len(crib)):
    if(len(cript[i:i+len(crib)])<len(crib)):
        break
    chok += comparaPalavras(cript[i:i+len(crib)], crib)
    
print(chok)
