# Loja de Roupas

Mini projeto de gerenciamento de produtos desenvolvido com Django. A aplicação permite cadastrar, listar, editar e excluir produtos, relacionando cada produto a uma marca e a uma ou mais categorias.

## Funcionalidades

- Listagem de produtos com preço, marca, país de origem, categorias e disponibilidade em estoque.
- Cadastro, edição e exclusão de produtos.
- Relacionamento de cada produto com uma marca.
- Relacionamento de cada produto com várias categorias.
- Gerenciamento de marcas e categorias pela área administrativa do Django.
- Banco de dados SQLite para desenvolvimento local.

## Tecnologias

- Python 3.14
- Django 6.1.2
- SQLite
- HTML e templates Django

## Requisitos

- Python instalado.
- Git, caso queira clonar o repositório.

## Como executar localmente

No PowerShell, na pasta do projeto:

```powershell
python -m venv env
.\env\Scripts\Activate.ps1
python -m pip install Django==6.1.2
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Acesse a aplicação em:

- Lista de produtos: <http://127.0.0.1:8000/store/produto/>
- Administração: <http://127.0.0.1:8000/admin/>

No admin, cadastre marcas e categorias antes de criar produtos, pois o produto precisa de uma marca. Depois, use a página de produtos para cadastrar e gerenciar os produtos.

## Rotas principais

| Método | Caminho | Descrição |
| --- | --- | --- |
| GET | `/store/produto/` | Lista os produtos |
| GET | `/store/adicionar/` | Exibe o formulário de cadastro |
| POST | `/store/adicionar/` | Cadastra um produto |
| GET | `/store/editar/<produto_id>/` | Exibe o formulário de edição preenchido |
| POST | `/store/editar/<produto_id>/` | Salva as alterações do produto |
| POST | `/store/apagar/<produto_id>/` | Exclui um produto |

## Modelos

- **Categoria**: nome com até 50 caracteres.
- **Marca**: nome com até 80 caracteres e país de origem com até 50 caracteres.
- **Produto**: nome com até 150 caracteres, marca, várias categorias, preço decimal e indicador de estoque.

## Testes

Para executar os testes do app:

```powershell
python manage.py test loja
```

Ainda não há testes automatizados implementados no projeto.

## Observação de segurança

As configurações atuais são destinadas ao desenvolvimento local. Antes de publicar ou hospedar a aplicação, configure uma `SECRET_KEY` segura fora do código e desative `DEBUG`.
