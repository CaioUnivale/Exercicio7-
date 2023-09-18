class Documento:
    def __init__(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo
    
    def exibir(self):
        return f"Título: {self.titulo}, Conteúdo: {self.conteudo}"

class Email(Documento):
    def __init__(self, titulo, conteudo, remetente, destinatario):
        super().__init__(titulo, conteudo)
        self.remetente = remetente
        self.destinatario = destinatario
    
    def exibir(self):
        base_info = super().exibir()
        return f"{base_info}, Remetente: {self.remetente}, Destinatário: {self.destinatario}"

class Relatorio(Documento):
    def __init__(self, titulo, conteudo, data):
        super().__init__(titulo, conteudo)
        self.data = data
    
    def exibir(self):
        base_info = super().exibir()
        return f"{base_info}, Data: {self.data}"


documento = Documento("Documento Genérico", "Este é um documento qualquer.")
print(documento.exibir())

email = Email("Convite para Reunião", "Por favor, participe da reunião na próxima segunda-feira.", "joao@email.com", "maria@email.com")
print(email.exibir())

relatorio = Relatorio("Relatório Mensal", "Análise das vendas do mês de julho.", "01/08/2023")
print(relatorio.exibir())