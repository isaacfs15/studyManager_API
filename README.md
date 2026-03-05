# 🎓 StudyManager API

Uma API RESTful robusta e escalável desenvolvida com **FastAPI** e **Python** para o gerenciamento de alunos, cursos e matrículas. 

Este projeto foi construído com foco em boas práticas de engenharia de software, separação rigorosa de responsabilidades e validação de dados, garantindo alta performance e confiabilidade nas regras de negócio.

## 🚀 Tecnologias Utilizadas

* **Framework Web:** FastAPI
* **Linguagem:** Python 3.10+
* **ORM & Banco de Dados:** SQLAlchemy + MySQL (`mysql-connector-python`)
* **Validação de Dados:** Pydantic V2
* **Servidor ASGI:** Uvicorn

## 📂 Arquitetura do Projeto

```text
studymanager_api/
├── app/
│   ├── main.py                     # Ponto de entrada, CORS e tratamento global de erros
│   ├── config/
│   │   └── database.py             # Configuração da string de conexão MySQL (localhost)
│   ├── models/                     # Entidades do SQLAlchemy (Mapeamento Objeto-Relacional)
│   │   ├── __init__.py           
│   │   ├── usuario_modelo.py
│   │   ├── curso_modelo.py
│   │   └── matricula_modelo.py
│   ├── schemas/                    # DTOs do Pydantic (Validação de entrada e serialização de saída)
│   │   ├── resposta_schema.py    
│   │   ├── usuario_schema.py
│   │   ├── curso_schema.py
│   │   └── matricula_schema.py
│   ├── repositories/               # Isolamento exclusivo para consultas e persistência no banco
│   │   ├── usuario_repository.py
│   │   ├── curso_repository.py
│   │   └── matricula_repository.py
│   ├── services/                   # Encapsulamento estrito das regras de negócio
│   │   ├── usuario_service.py
│   │   ├── curso_service.py
│   │   └── matricula_service.py
│   └── controllers/                # Roteamento HTTP (Endpoints)
│       ├── usuario_controller.py
│       ├── curso_controller.py
│       └── matricula_controller.py
```
## 🏛️ Justificativa da Arquitetura
  A estrutura do projeto foi desenhada baseando-se nos princípios da Arquitetura Limpa (Clean Architecture) e SOLID, visando a máxima separação de responsabilidades. Dividindo a aplicação em camadas isoladas — onde os Controllers gerenciam apenas as requisições HTTP, os Services aplicam as regras de negócio rigorosas (como a validação de matrículas duplicadas), os Repositories abstraem as queries do banco de dados e os Schemas/Models definem os contratos de dados —. Essa modularização em múltiplos arquivos independentes evita o acoplamento excessivo, facilita a navegação no código e permite que tecnologias subjacentes (como o banco de dados) sejam trocadas no futuro com impacto estrutural quase nulo.

## ⚙️ Funcionalidades e Regras de Negócio
A API padroniza todas as respostas em um formato JSON previsível: {"success": bool, "message": str, "data": object}.


```Usuários (/usuarios): Criação, listagem, busca, atualização e deleção. Garantia de unicidade de e-mail.```

 ```Cursos (/cursos): Gerenciamento completo do catálogo de cursos e suas cargas horárias.```

Matrículas (/enrollments):

```Validação rigorosa: Verifica se o usuário e o curso existem na base de dados (Retorna HTTP 404 caso não existam).```

```Prevenção de duplicidade: Impede que um aluno se matricule duas vezes no mesmo curso (Retorna HTTP 400).```


## 🛠️ Como executar o projeto localmente

1. Clone o repositório:

```text
  git clone [https://github.com/SEU_USUARIO/studymanager-api.git](https://github.com/SEU_USUARIO/studymanager-api.git)
cd studymanager-api
```

2. Crie e ative um ambiente virtual (Recomendado):

```text
  python -m venv venv
```
  # No Windows:
   ```text
    .\venv\Scripts\activate
   ```
  # No Linux/Mac:
  ```text
    source venv/bin/activate
  ```
3. Instale as dependências:

  ```text
    pip install fastapi "uvicorn[standard]" sqlalchemy mysql-connector-python "pydantic[email]"
  ```
4. Prepare o Banco de Dados:

  * Certifique-se de que o MySQL está rodando na sua máquina (localhost porta 3306).

  * Crie o banco de dados base (o SQLAlchemy criará as tabelas automaticamente):
    ```text
    CREATE DATABASE studymanager_db;
    ```
5. Execute a aplicação:

   ```text
    uvicorn app.main:app --reload
   ```
6. Acesse a documentação interativa:

   * Swagger UI: http://127.0.0.1:8000/docs
