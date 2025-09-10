class Praia:
    def __init__(self, nome: str, distancia_centro: float, veranistas: int, tipo_de_acesso: str):
        """
        Inicializa uma nova instância da classe Praia.

        Args:
            nome (str): O nome da praia.
            distancia_centro (float): A distância da praia até o centro da cidade (em km).
            veranistas (int): O número estimado de veranistas na praia.
            tipo_de_acesso (str): O tipo de acesso à praia (ex: "rodoviário", "trilhas").
        """
        self.nome = nome
        self.distancia_centro = distancia_centro
        self.veranistas = veranistas
        self.tipo_de_acesso = tipo_de_acesso

# Exemplo de como criar um objeto (instância) da classe Praia
praia_copacabana = Praia("Praia de Copacabana", 3.5, 10000, "rodoviário")

# Acessando os atributos do objeto
print(f"Nome da praia: {praia_copacabana.nome}")
print(f"Veranistas: {praia_copacabana.veranistas}")