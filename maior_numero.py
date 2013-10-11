a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

if b > c and b > a:
	print("\nO maior numero é", b)
elif c > a and c > b:
	print("\nO maior numero é", c)
else:
	print("\nO maior numero é", a)

input()
