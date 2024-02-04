preço = float(input("Qual preço do produto? R$"))
desconto = preço - preço * 0.05
print(f"O produto que custava R${preço}, na promoção com desconto de 5% vai custar R${desconto:.2f}")