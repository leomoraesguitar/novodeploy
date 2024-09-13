import flet as ft
def main(page: ft.Page):

    def SalvarDadosLocais(nome, valor):
        page.client_storage.set(nome, valor)
        

    def LerDadosLocais( nome,  default=None):
        if page.client_storage.contains_key(nome):
            return page.client_storage.get(nome)
        else:
            return default


    def Settext(e):
        valor = e.control.value
        SalvarDadosLocais('valortexto',valor)
    
    ti = LerDadosLocais('valortexto', default='02')
    page.add(ft.TextField(value = ti, on_change=Settext,label='Digite aqui', border_width=1))


if __name__ == '__main__':  
    
    ft.app(main )