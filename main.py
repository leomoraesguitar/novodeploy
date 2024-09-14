import flet as ft

def main(page: ft.Page):
    new_key_field = ft.TextField(label="novo Nome1", width=200)
    result_label = ft.Text(value="", color="green")


    def SalvarDadosLocais( nome, valor):
        page.client_storage.set(nome, valor)
        

    def LerDadosLocais( nome,  default=None):
        if page.client_storage.contains_key(nome):
            return page.client_storage.get(nome)
        else:
            return default
    def submit_content(e):
        result_label.value = "Valor salvo no LocalStorage!"
        SalvarDadosLocais('valor', new_key_field.value)
        page.update()


    # new_key_field.value = LerDadosLocais('valor')
    submit_button = ft.ElevatedButton(text="Salvar no LocalStorage", on_click=submit_content)

    page.add(
        ft.Text("Atualizador de valor no LocalStorage", size=20, weight="bold"),
        new_key_field,
        submit_button,
        result_label,

    )
if __name__ == '__main__':
    ft.app(main, view=ft.AppView.WEB_BROWSER)
