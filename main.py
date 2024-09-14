import flet as ft

def main(page: ft.Page):
    new_key_field = ft.TextField(label="novo Nome5", width=200)
    result_label = ft.Text(value="", color="green")


    # def SalvarDadosLocais( nome, valor):
    #     page.client_storage.set(nome, valor)
        

    # async  def LerDadosLocais(nome,  default=None):
    #     # if page.client_storage.contains_key(nome):
    #     try:
    #         r = await page.client_storage.get_async(nome)
    #         return r
    #     except:
    #         return default
        

    async def submit_content(e):
        # SalvarDadosLocais('valor', new_key_field.value)
        v = new_key_field.value
        await page.client_storage.set_async('valor',v)

        try:
            r = await page.client_storage.get_async('valor')
            
        except:
            r = None
        result_label.value = f"Valor salvo no LocalStorage: {r}"
        page.update()

    # SalvarDadosLocais('valor', 'meu ovo5')
    # new_key_field.value = LerDadosLocais('valor', 'meu ovo')
    submit_button = ft.ElevatedButton(text="Salvar no LocalStorage", on_click=submit_content)

    page.add(
        ft.Text("Atualizador de valor no LocalStorage", size=20, weight="bold"),
        new_key_field,
        submit_button,
        result_label,

    )
    page.update()
if __name__ == '__main__':
    ft.app(main, view=ft.AppView.WEB_BROWSER)
