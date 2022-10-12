from models.product import Product


def main():
    with open('./produtos.txt', 'r') as f:
        file_text = f.readlines()

    products = []
    for index, line in enumerate(file_text):
        if index == 0:
            continue

        products.append(Product(*line.split("|")))

    products.sort(key=lambda x:(-x.stock_price, -x.unit_price, x.description))

    total = 0.0
    with open('./estoque.txt', 'w') as f:
        f.write(f"    id|descricao                               |preco_estoque  \n")

        for p in products:
            total += round(p.stock_price, 2)
            f.write(f"{p.id:0>6}|{p.description:<40}|{p.stock_price:0>15.2f}\n")

        f.write(f"      |TOTAL                                   |{total:0>15.2f}")

if __name__ == "__main__":
    main()