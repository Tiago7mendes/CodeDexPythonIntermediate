import csv

# Caminho do arquivo CSV
csv_file_path = 'Bestseller - Sheet1.csv'

best_selling_book = None
max_sales = 0.0

# Task 1: Lendo o arquivo CSV
with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Pular o cabeçalho
    next(csv_reader)
    
    for row in csv_reader:
        # Verifica se a linha não está vazia e tem colunas suficientes
        if len(row) > 4:
            try:
                # Troca vírgula por ponto se necessário
                current_sales = float(row[4].replace(',', '.'))
                
                if current_sales > max_sales:
                    max_sales = current_sales
                    best_selling_book = row
            except ValueError:
                # Caso a célula de vendas não seja número válido
                continue

# Task 2: Criando novo arquivo com o livro mais vendido
if best_selling_book:
    output_file_path = 'bestseller_info.csv'
    with open(output_file_path, 'w', newline='', encoding='utf-8') as output_file:
        csv_writer = csv.writer(output_file)
        
        # Escreve cabeçalho
        csv_writer.writerow(['Book', 'Author', 'Sales in Millions'])
        
        # Escreve info do livro mais vendido
        csv_writer.writerow([best_selling_book[0], best_selling_book[1], best_selling_book[4]])

    # Mensagem de confirmação
    print(f'O livro mais vendido foi "{best_selling_book[0]}" de {best_selling_book[1]} com {best_selling_book[4]} milhões de cópias.')
    print('As informações foram salvas em', output_file_path)
else:
    print("Não foi possível encontrar um livro válido no arquivo CSV.")
