import flet as ft


class ClassName(ft.Column):
    def __init__(self,page):
        super().__init__()
        self.page = page
    # Campo de entrada para o nome do usuário
        self.name_input = ft.TextField(label="Digite seu nome")

        # Botões para salvar e carregar os dados
        self.save_button = ft.ElevatedButton(text="Salvar Nome", on_click=self.save_data)
        self.load_button = ft.ElevatedButton(text="Carregar Nome", on_click=self.load_data)
        self.saida = ft.Text()


        self.controls = [self.name_input, self.save_button, self.load_button,self.saida ]

    def save_data(self, e):
        # Salvando a entrada de texto no armazenamento local
        nome = "user_name"
        dic = {'nome':self.name_input.value}
        self.page.client_storage.set(nome, dic)
        self.saida.value = f"Nome '{self.name_input.value}' salvo!"
        self.update()

    # Função para recuperar o valor salvo no client storage
    def load_data(self, e):
        # Carregando o valor do armazenamento local
        nome = "user_name"
        stored_name = self.page.client_storage.get(nome)
        if stored_name:
            self.saida.value = f"Nome carregado: {stored_name['nome']}"
        else:
            self.saida.value = "Nenhum nome encontrado no armazenamento local."
        self.update()

def main(page: ft.Page):
    # Função para salvar um valor no client storage

    # Adicionando os elementos à página
    page.add(ClassName(page))

ft.app(target=main)
