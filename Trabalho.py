import csv

class OrcamentoAluguel():
    def __init__(self):
        # Preços bases e adicionais
        self.preco_apartamento_1Q = 700.00
        self.preco_casa_1Q = 900.00
        self.preco_studio = 1200.00
        
        self.quarto_adicional_apartamento = 200.00
        self.quarto_adicional_casa = 250.00
        self.garagem_adicional = 300.00
        
        self.vaga_padrao_studio = 250.00  # 2 vagas padrões
        self.vaga_adicional_studio = 60.00  # Por vaga adicional
        
        self.valor_contrato = 2000.00
        
    def calcular_apartamento(self, quartos, tem_garagem, tem_criancas):
        total = self.preco_apartamento_1Q
        
        # Calculo apartamento com dois quartos
        if quartos == 2:
            total += self.quarto_adicional_apartamento
            
    
        if tem_garagem:
            total += self.garagem_adicional
            
        # Desconto de 5% se não tiver crianças
        if not tem_criancas:
            desconto = total * 0.05
            total -= desconto
            
        return total

    def calcular_casa(self, quartos, tem_garagem):
        total = self.preco_casa_1Q
        
        # Calculo casa com dois quartos
        if quartos == 2:
            total += self.quarto_adicional_casa
            
        
        if tem_garagem:
            total += self.garagem_adicional
            
        return total

    def calcular_studio(self, incluir_vagas, vagas_extras=0):
        total = self.preco_studio
        
        # Regra F: Vagas de estacionamento
        if incluir_vagas:
            total += self.vaga_padrao_studio  # Inclui 2 vagas
            if vagas_extras > 0:
                total += (vagas_extras * self.vaga_adicional_studio)
                
        return total

    def gerar_parcelas_contrato(self):
        parcelas = []
        for i in range(1, 6):
            valor = self.valor_contrato / i
            parcelas.append(f"{i}x de R$ {valor:.2f}")
        return parcelas

    def gerar_csv(self, nome_cliente, tipo_imovel, valor_mensal, contrato_parcelado):
        filename = f"orcamento_{nome_cliente.replace(' ', '_').lower()}.csv"
        
        # Gera o arquivo CSV com 12 parcelas do orçamento
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Mês', 'Valor Aluguel', 'Descrição'])
            
            # Escreve 12 meses
            for mes in range(1, 13):
                writer.writerow([f'Mês {mes}', f'R$ {valor_mensal:.2f}', f'Aluguel {tipo_imovel}'])
                
            writer.writerow([])
            writer.writerow(['CONTRATO', 'R$ 2.000,00', 'Pode ser parcelado em até 5x'])
            
        return filename

# Abre o menu inicial
def menu():
    sistema = OrcamentoAluguel()
    
    print("=== SISTEMA DE ORÇAMENTO R.M IMOBILIÁRIA ===")
    print("===Seja bem vindo!===")
    nome = input("Nome do cliente: ")
    
    print("\nTipos de Imóvel:")
    print("1 - Apartamento")
    print("2 - Casa")
    print("3 - Studio")
    imovel = input("Escolha o tipo (1/2/3): ")
    
    valor_final = 0.0
    descricao_imovel = ""
    
    if imovel == '1':
        descricao_imovel = "Apartamento"
        quartos = int(input("Número de quartos (1 ou 2): "))
        garagem = input("Deseja vaga de garagem? (S/N): ").upper() == 'S'
        criancas = input("Possui crianças? (S/N): ").upper() == 'S'
        valor_final = sistema.calcular_apartamento(quartos, garagem, criancas)
        
    elif imovel == '2':
        descricao_imovel = "Casa"
        quartos = int(input("Número de quartos (1 ou 2): "))
        garagem = input("Deseja vaga de garagem? (S/N): ").upper() == 'S'
        valor_final = sistema.calcular_casa(quartos, garagem)
        
    elif imovel == '3':
        descricao_imovel = "Studio"
        vagas = input("Deseja pacote de vagas (2 vagas por R$ 250)? (S/N): ").upper() == 'S'
        extras = 0
        if vagas:
            tem_extras = input("Deseja vagas extras além das 2? (S/N): ").upper() == 'S'
            if tem_extras:
                extras = int(input("Quantas vagas extras?: "))
        valor_final = sistema.calcular_studio(vagas, extras)
    
    print("\n" + "="*40)
    print(f"Orçamento para o cliente: {nome}")
    print(f"Imóvel escolhido : {descricao_imovel}")
    print(f"Valor Mensal do Aluguel: R$ {valor_final:.2f}")
    print("\nOpções de Pagamento do Contrato (Total R$ 2.000,00):")
    for opcao in sistema.gerar_parcelas_contrato():
        print(opcao)
        
    gerar_arquivo = input("\nDeseja gerar o arquivo CSV? (S/N): ").upper() == 'S'
    if gerar_arquivo:
        arquivo = sistema.gerar_csv(nome, descricao_imovel, valor_final, sistema.gerar_parcelas_contrato())
        print(f"Arquivo gerado com sucesso: {arquivo}")


if __name__ == "__main__":
    menu()
