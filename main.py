import os
import requests
import base64
import json

class API_Github:
    def __init__(self):
        self._GITHUB_TOKEN = os.getenv('PERSONAL_ACCESS_TOKEN')
        self._REPO_OWNER = 'leomoraesguitar'
        self._REPO_NAME = 'novodeploy'
        self._FILE_PATH = 'meu.json'
        self._API_URL = f'https://api.github.com/repos/{self._REPO_OWNER}/{self._REPO_NAME}/contents/{self._FILE_PATH}'
        self._headers = {
            'Authorization': f'token {self._GITHUB_TOKEN}',
            'Accept': 'application/vnd.github.v3+json'
        }

    def get_file_content(self):
        response = requests.get(self._API_URL, headers=self._headers)
        if response.status_code == 200:
            file_info = response.json()
            file_content = base64.b64decode(file_info['content']).decode('utf-8')
            return file_content, file_info['sha']
        return None, None

    def update_github_file(self, new_content, sha):
        message = "Atualização do arquivo JSON"
        encoded_content = base64.b64encode(new_content.encode('utf-8')).decode('utf-8')
        data = {
            'message': message,
            'content': encoded_content,
            'sha': sha
        }
        response = requests.put(self._API_URL, json=data, headers=self._headers)
        return response.status_code

def main():
    api = API_Github()
    file_content, sha = api.get_file_content()
    if file_content and sha:
        json_data = json.loads(file_content)
        json_data['new_key'] = 'new_value'
        status = api.update_github_file(json.dumps(json_data, indent=4), sha)
        print('Status Code:', status)
        print('Response:', 'File updated successfully' if status == 200 else 'Failed to update file')
    else:
        print('Failed to get file content')

if __name__ == "__main__":
    main()
