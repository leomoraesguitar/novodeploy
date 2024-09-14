
import flet as ft
import requests
import base64
import json
import os




class API_Github:
    def __init__(self,
                 nomeusuario = None,
                 nomerepositorio = None,
                 caminhoarquivo = None,

                 
                 
                 ):
        # Configurações do GitHub

        self._GITHUB_TOKEN = os.getenv('PERSONAL_ACCESS_TOKEN')

        self._REPO_OWNER = nomeusuario #'leomoraesguitar'
        self._REPO_NAME = nomerepositorio #'novodeploy'
        self._FILE_PATH = caminhoarquivo #'meu.json'
        self._API_URL = f'https://api.github.com/repos/{self._REPO_OWNER}/{self._REPO_NAME}/contents/{self._FILE_PATH}'

        self._headers = {
            'Authorization': f'token {self._GITHUB_TOKEN}',
            'Accept': 'application/vnd.github.v3+json'
        }




    def ExibirJson(self, nomedodicionario):
        return json.dumps(nomedodicionario, indent=4)

    def Ler_json2(self, nomedoarquivo):
        try:
            return json.loads(nomedoarquivo)
        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar JSON: {e}")
            return {}


    def update_github_file(self, new_content, sha):
        message = "Atualização do arquivo JSON via Flet"
        encoded_content = base64.b64encode(new_content.encode('utf-8')).decode('utf-8')

        data = {
            'message': message,
            'content': encoded_content,
            'sha': sha
        }

        response = requests.put(self._API_URL, json=data, headers=self._headers)
        return response.status_code
    
    # Função para obter o SHA e o conteúdo do arquivo JSON
    def get_file_content(self):
        response = requests.get(self._API_URL, headers=self._headers)
        if response.status_code == 200:
            file_info = response.json()
            file_content = base64.b64decode(file_info['content']).decode('utf-8')

            # Verificar se o conteúdo não é vazio ou inválido
            if not file_content.strip():
                return '{}', file_info['sha']  # Retorna um JSON vazio se o arquivo estiver vazio

            sha = file_info['sha']
            return file_content, sha
        return None, None


    def AtualizarJson(self,json_data,sha):
            updated_content = json.dumps(json_data, indent=4)
            # updated_content = Escrever_json2(json_data)
            
            # Atualizar o arquivo no GitHub
            status = self.update_github_file(updated_content, sha)        
            return status



# Função principal do app Flet
def main(page: ft.Page):
    new_key_field = ft.TextField(label="novo Nome", width=200)
    json_display = ft.Text("Conteúdo atual do arquivo JSON:")
    result_label = ft.Text(value="", color="green")


    Api = API_Github(
        nomeusuario = 'leomoraesguitar',
        nomerepositorio = 'novodeploy',
        caminhoarquivo = 'meu.json'
    )
    file_content, sha = Api.get_file_content()


    if file_content and sha:
        json_data = Api.Ler_json2(file_content)
    new_key_field.value = json_data[list(json_data.keys())[0]]



    # Função chamada ao clicar no botão de atualização
    def submit_content(e):
        # Obtenção do conteúdo atual e SHA do arquivo
        file_content, sha = Api.get_file_content()

        if file_content and sha:
            json_data = Api.Ler_json2(file_content)
            valor = new_key_field.value
            json_data[list(json_data.keys())[0]] = valor
            status = Api.AtualizarJson(json_data,sha)

            if status == 200:
                result_label.value = "Arquivo JSON atualizado com sucesso!"
                # Atualiza o conteúdo exibido na página
                json_display.value = f"Conteúdo atualizado:\n{Api.ExibirJson(json_data)}"
            else:
                result_label.value = f"Erro ao atualizar arquivo. Status: {status}"


        else:
            result_label.value = "Erro ao obter o conteúdo do arquivo."

        page.update()

    # Botão para enviar o novo conteúdo
    submit_button = ft.ElevatedButton(text="Atualizar arquivo JSON", 
                                      on_click=submit_content
                                      )

    # Adicionando os componentes à página
    page.add(
        ft.Text("Atualizador de arquivo JSON no GitHub", size=20, weight="bold"),
        new_key_field,
        submit_button,
        result_label,
        json_display
    )

# Executando o app Flet
ft.app(target=main)
