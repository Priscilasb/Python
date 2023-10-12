#Dissecando uma variavel
a = input("Digite algo: ")
print("O tipo primitivo desse valor é ", type(a))
print("Só tem espaço? ", a.isspace())
print("É um numero? ", a.isnumeric())
print("É alfabetico? ", a.isalpha())
print("É alfanumerico? ", a.isalnum())
print("Esta em maisuculas? ", a.isupper())
print("Esta em minusculas? ", a.islower())
print("Esta capitalizada?", a.istitle()) #maiusculo com minisculo
