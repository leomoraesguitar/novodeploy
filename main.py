import flet as ft

def main(page: ft.Page):
    new_key_field = ft.TextField(label="novo Nome", width=200)
    json_display = ft.Text("Conteúdo atual do arquivo salvo no LocalStorage:")
    result_label = ft.Text(value="", color="green")

    def submit_content(e):
        # Função para salvar o valor no LocalStorage via JavaScript
        page.eval(f"localStorage.setItem('key', '{new_key_field.value}');")
        result_label.value = "Valor salvo no LocalStorage!"
        page.update()

    def carregar_valor_salvo():
        # Função para carregar o valor do LocalStorage via JavaScript e exibir no Flet
        page.eval("""
        const savedValue = localStorage.getItem('key');
        if (savedValue) {
            return savedValue;
        }
        return null;
        """, 
        lambda result: json_display.update(f"Valor salvo: {result}" if result else "Nenhum valor salvo no LocalStorage.")
        )

    submit_button = ft.ElevatedButton(text="Salvar no LocalStorage", on_click=submit_content)

    # Adicionando os componentes à página
    page.add(
        ft.Text("Atualizador de valor no LocalStorage", size=20, weight="bold"),
        new_key_field,
        submit_button,
        result_label,
        json_display
    )

    # Carregar valor salvo no LocalStorage quando a página for carregada
    carregar_valor_salvo()

# Executando o app Flet
ft.app(target=main)
