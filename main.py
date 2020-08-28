from list_core import List

"""
• Construir um algoritmo que contenha 3 listas:

      • Nomes de produtos

      • Preços de cada produto

      • Quantidades de cada produto

• Construir uma função para imprimir um dos produtos da lista e uma função para retirar um dos produtos das listas
"""
product_list = List()
price_list = List()
quantity_list = List()

product_list.insert('Gift Card')
product_list.insert('Fita Crepe')
product_list.insert('Palheta')
product_list.insert('Relógio de Pulso')
product_list.insert('Máscara')
product_list.insert('Álcool em Gel')
product_list.insert('Capotraste')
print()

print('Product List')
print(f'{product_list.search("Máscara")}')
product_list.delete("Máscara")
product_list.get_items()

price_list.insert(30.0)
price_list.insert(0.05)
price_list.insert(2.0)
price_list.insert(137.5)
price_list.insert(7.0)
price_list.insert(10.0)
price_list.insert(25.0)
print()

print('\nPrice List')
print(f'{price_list.search(7.0)}')
price_list.delete(7.0)
price_list.get_items()

quantity_list.insert(5)
quantity_list.insert(50)
quantity_list.insert(30)
quantity_list.insert(15)
quantity_list.insert(200)
quantity_list.insert(100)
quantity_list.insert(20)
print()

print('\nQuantity List')
print(f'{quantity_list.search(200)}')
quantity_list.delete(200)
quantity_list.get_items()