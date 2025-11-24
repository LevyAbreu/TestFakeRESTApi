# Projeto de Testes de API

Este repositório contém uma suíte de testes de integração e ponta a ponta para uma API, desenvolvida em Python utilizando a biblioteca `pytest` e `requests`. Os testes estão organizados por módulos que parecem corresponder a diferentes endpoints da API.

## Estrutura do Projeto

O projeto está estruturado em módulos, onde cada diretório representa um conjunto de testes focado em uma funcionalidade ou recurso específico da API.

```
/home/ubuntu/project_root/testes
TestFakeRESTApi
├──Tests
│  ├── Activities/ (Mike)
│  │   ├── config.py
│  │   ├── test_activities_delete.py
│  │   ├── test_activities_get.py
│  │   ├── test_activities_get_id.py
│  │   ├── test_activities_post.py
│  │   └── test_activities_put.py
│  ├── Authors/ (Eric)
│  │   ├── config.py
│  │   ├── test_authors_delete.py
│  │   ├── test_authors_get.py
│  │   ├── test_authors_get_id.py
│  │   ├── test_authors_post.py
│  │   └── test_authors_put.py
│  ├── Books/ (Levy)
│  │   ├── config.py
│  │   ├── test_books_delete.py
│  │   ├── test_books_get.py
│  │   ├── test_books_get_id.py
│  │   ├── test_books_post.py
│  │   └── test_books_put.py
│  ├── Cover_photo/ (Leo)
│  │   ├── config.py
│  │   ├── test_Cover_photo_delete.py
│  │   ├── test_Cover_photo_get.py
│  │   ├── test_Cover_photo_get_id.py
│  │   ├── test_Cover_photo_post.py
│  │   └── test_Cover_photo_put.py
│  └── Users/ (Rian)
│      ├── config.py
│      ├── test_users_delete.py
│      ├── test_users_get.py
│      ├── test_users_get_id.py
│      ├── test_users_post.py
│      └── test_users_put.py
└── ReadMe.md
```

### Módulos de Teste

| Módulo   | Endpoint/Recurso Testado | Arquivos de Exemplo                                          |
| :---     | :---                     | :---                                                         |
| **Eric** | `Authors`                | `test_authors_get.py`, `test_authors_post.py`, etc.          |
| **Levy** | `Books`                  | `test_books_get.py`, `test_books_post.py`, etc.              |
| **Mike** | `Activities`             | `test_activities_get.py`, `test_activities_post.py`, etc.    |
| **Rian** | `Users`                  | `test_users_get.py`, `test_users_post.py`, etc.              |
| **Leo**  | `Cover_photo`            | `test_Cover_photo_get.py`, `test_Cover_photo_post.py`, etc.  |

## Tecnologias Utilizadas

*   **Python**: Linguagem de programação principal.
*   **Pytest**: Framework de testes para execução e organização dos casos de teste.
*   **Requests**: Biblioteca HTTP para realizar as chamadas à API.

## Configuração e Instalação

Para executar os testes, você precisará ter o Python instalado e as dependências do projeto.

### Pré-requisitos

*   Python 3.x

### Instalação de Dependências

Recomenda-se criar um ambiente virtual antes de instalar as dependências.

```bash
# Crie um ambiente virtual (opcional, mas recomendado)
python3 -m venv venv
source venv/bin/activate  # No Linux/macOS
# venv\Scripts\activate   # No Windows

# Instale as dependências (assumindo que requests e pytest são as principais)
pip install pytest requests
```

## Executando os Testes

Os testes podem ser executados usando o comando `pytest` na raiz do diretório `tests`.

### Executar Todos os Testes

```bash
pytest /home/ubuntu/project_root/tests
```

### Executar Testes de um Módulo Específico

Para executar apenas os testes relacionados a Livros (módulo Levy):

```bash
pytest /home/ubuntu/project_root/tests/Levy
```

### Executar um Caso de Teste Específico

Você pode executar um teste específico usando o caminho do arquivo e o nome da função de teste:

```bash
pytest /home/ubuntu/project_root/tests/Books-Levy/test_books_get.py::test_tc12_get_book_by_id_success
```

## Configuração de Endpoints

Os endpoints base da API são definidos nos arquivos `config.py` dentro de cada módulo. Certifique-se de que a variável de ambiente ou a constante `BOOKS_ENDPOINT`, `AUTHORS_ENDPOINT`, etc., esteja configurada corretamente para apontar para a URL da sua API.

Exemplo de `config.py`:

```python
# Exemplo de conteúdo em config.py
BASE_URL = "http://api.exemplo.com/v1"
BOOKS_ENDPOINT = f"{BASE_URL}/Books"
# ... outros endpoints
```