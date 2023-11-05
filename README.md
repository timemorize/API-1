# API - 1º Semestre Fatec 🔭
## Objetivo
Desenvolver um sistema interno de gestão e acompanhamento de scores para a instituição de ensino PBLTeX, especializada em cursos práticos de ensino aplicando PBL, visando otimizar a avaliação do Fator de Ensino Evolutivo (FEE) e fortalecer sua posição no mercado de edtechs.

### Requisitos Funcionais
- O SI deve possuir um controle de Turmas;
- O SI deve possuir um controle de Grupos de Alunos;
- O SI deve permitir um controle de Alunos;
- O SI deve permitir a carga de Alunos;
- O SI deve permitir um controle dos Ciclos de Entrega;
- O SI deve permitir a carga de <i>scores</i> parciais relacionados ao Ciclo de Entrega;
- O SI deve permitir a configuração de parâmetros globais;
- O SI deve permitir a exportação de dados consolidados, computados e métricas inferidas;
- O SI deve prover visibilidades objetivas e diretas que possibilitem o acompanhamento dos cursos providos pela PBLTeX.

### Requisitos Não Funcionais
- Linguagem de programação Python e tecnologias relacionadas.
- Uso de bases de dados simples, podendo ser: Arquivo(Text, CSV, Json ou outros formatos);
- Não deve ser utilizado SGBDs SQL e NoSQL no trabalho
- Sistema de controle de versão de código (Git)
- Documentações

#### Prazos das sprints
<table border="1 px solid #343A40">
    <tr>
        <th> Sprints </th>
        <th> Início </th>
        <th> Fim </th>
    </tr>
    <tr>
        <td> 1ª sprint </td>
        <td> 04/09 </td>
        <td> 24/09 </td>
    </tr>
    <tr>
        <td> 2ª sprint </td>
        <td> 25/09 </td>
        <td> 15/10 </td>
    </tr>
    <tr>
        <td> 3ª sprint </td>
        <td> 16/10 </td>
        <td> 05/11 </td>
    </tr>
    <tr>
        <td> 4ª sprint </td>
        <td> 06/11 </td>
        <td> 26/11 </td>
    </tr>
</table>

### Fluxograma da Aplicação:
Foi elaborado um fluxograma utilizando o software Miro. Convido você a clicar no botão abaixo para conferir o resultado: <br>
<a href="https://miro.com/app/board/uXjVMmvukI4=/?share_link_id=70126474804">
    <img src="https://github.com/ElbertJean/faculdade/blob/main/AcessarFluxograma.png" width="25%"/>
</a>

### WireFrame
Foi Desenvolvido um wireframe no Figma para o projeto. Convido você a clicar no botão abaixo para visualizar o wireframe: <br>
<a href="https://www.figma.com/file/z3ULTstviHzHjpTrmdqyky/Untitled?type=design&node-id=0%3A1&mode=design&t=7X3mwSH3mpjgNpdP-1">
    <img src="https://github.com/ElbertJean/faculdade/blob/main/AcessarWireframe.png" width="25%"/>
</a>

### Backlog do projeto
| **COMO** | **EU QUERO** | **PRIORIDADE** | **SPRINT** | **STATUS** |
|-------------------------|-------------------------|---------------------|----------------|-------------------------|
| Desenvolvedor | Criar documentação do produto | Imprescindível | 1 | **Realizado** |
| Desenvolvedor | Criar fluxograma e wireframes  do produto | Imprescindível | 1 | **Realizado** |
| Diretor | Cadastrar diferentes tipos de usuários | Imprescindível | 2 | **Realizado** |
| Diretor | Conseguir editar e excluir o cadastro dos usuários |  Imprescindível | 2 | **Realizado**|
| Diretor | Criar Grupos de alunos | Imprescindível | 2 | **Realizado** |
| Diretor | Vincular alunos aos grupos existentes |  Imprescindível | 2 | **Realizado**|
| Diretor | Conseguir editar e excluir Grupos |  Imprescindível | 2 | **Realizado**|
| Diretor | Criar Turmas | Imprescindível | 2 | **Realizado** |
| Diretor | Vincular alunos e professores as turmas existentes |  Imprescindível | 2 | **Realizado**|
| Diretor | Conseguir editar e excluir Turmas |  Imprescindível | 2 | **Realizado**|
| Diretor | Campo de pesquisa nas telas de Alunos, Grupos, Turmas e Professores | Importante | 2 | **Realizado** |
| Diretor | Conseguir criar um ciclo de entrega | Imprescindível | 3 | **Realizado** |
| Diretor | Conseguir editar e excluir o ciclo de entrega |  Imprescindível | 3 | **Realizado**|
| Diretor | Saber se um ciclo de entrega está ativo ou desativado |  Importante | 3 | **Realizado**|
| Diretor | Campo de pesquisa na tela de ciclo de entrega | Importante | 3 | **Realizado** |
| Diretor | Conseguir exportar os ciclos de entrega | Importante | 3 | **Realizado** |
| Professor | Conseguir cadastrar uma atividade | Imprescindível | 3 | **Realizado** |
| Professor | Conseguir gerenciar as atividades | Imprescindível | 3 | **Realizado** |
| Professor | Conseguir editar e excluir uma atividade | Imprescindível | 3 | **Realizado** |
| Professor | Conseguir inserir as notas dos alunos | Imprescindível | 3 | **Realizado** |
| Professor | Conseguir exportar as notas dos alunos | Importante | 3 | **Realizado** |
| Usuário | Fazer login no sistema | Imprescindível | 4 | **-** |
| Aluno | Conseguir visualizar em quais turmas está cadastrado | Imprescindível | 4 | **-** |
| Aluno | Conseguir visualizar as suas notas |  Imprescindível | 4 | **-**|
| Aluno | Saber como está o seu score|  Importante | 4 | **-**|

### Backlog 1º Sprint
| **COMO** | **EU QUERO** | **PRIORIDADE** | **SPRINT** | **STATUS** |
|-------------------------|-------------------------|---------------------|----------------|-------------------------|
| Desenvolvedor | Criar documentação do produto | Imprescindível | 1 | **Realizado** |
| Desenvolvedor | Criar fluxograma e wireframes  do produto | Imprescindível | 1 | **Realizado** |

### Backlog 2º Sprint
| **COMO** | **EU QUERO** | **PRIORIDADE** | **SPRINT** | **STATUS** |
|-------------------------|-------------------------|---------------------|----------------|-------------------------|
| Diretor | Cadastrar diferentes tipos de usuários | Imprescindível | 2 | **Realizado** |
| Diretor | Conseguir editar e excluir o cadastro dos usuários |  Imprescindível | 2 | **Realizado**|
| Diretor | Criar Grupos de alunos | Imprescindível | 2 | **Realizado** |
| Diretor | Vincular alunos aos grupos existentes |  Imprescindível | 2 | **Realizado**|
| Diretor | Conseguir editar e excluir Grupos |  Imprescindível | 2 | **Realizado**|
| Diretor | Criar Turmas | Imprescindível | 2 | **Realizado** |
| Diretor | Vincular alunos e professores as turmas existentes |  Imprescindível | 2 | **Realizado**|
| Diretor | Conseguir editar e excluir Turmas |  Imprescindível | 2 | **Realizado**|
| Diretor | Campos de pesquisa | Importante | 2 | **Realizado** |

### Backlog 3º Sprint
| **COMO** | **EU QUERO** | **PRIORIDADE** | **SPRINT** | **STATUS** |
|-------------------------|-------------------------|---------------------|----------------|-------------------------|
| Diretor | Conseguir criar um ciclo de entrega | Imprescindível | 3 | **Realizado** |
| Diretor | Conseguir editar e excluir o ciclo de entrega |  Imprescindível | 3 | **Realizado**|
| Diretor | Saber se um ciclo de entrega está ativo ou desativado |  Importante | 3 | **Realizado**|
| Diretor | Campo de pesquisa na tela de ciclo de entrega | Importante | 3 | **Realizado** |
| Diretor | Conseguir exportar os ciclos de entrega | Importante | 3 | **Realizado** |
| Professor | Conseguir cadastrar uma atividade | Imprescindível | 3 | **Realizado** |
| Professor | Conseguir gerenciar as atividades | Imprescindível | 3 | **Realizado** |
| Professor | Conseguir editar e excluir uma atividade | Imprescindível | 3 | **Realizado** |
| Professor | Conseguir inserir as notas dos alunos | Imprescindível | 3 | **Realizado** |
| Professor | Conseguir exportar as notas dos alunos | Importante | 3 | **Realizado** |


## Tecnologias utilizadas e Integrantes
<img src="https://github.com/ElbertJean/faculdade/blob/main/Frame%203%20(2).jpg" width="100%"/>

## Instalação

 # Passo-a-passo para Instalação de uma Aplicação Python

### 1. Preparação do Ambiente

Certifique-se de ter o Python instalado em seu sistema. Você pode baixá-lo em [Python Official Website](https://www.python.org/). Certifique-se também de instalar o [Flask Official Website](https://pypi.org/project/Flask/) e [Pip Official Website](https://pypi.org/project/pip/)  para que o projeto possa funcionar.<br>
Além disso, é recomendável criar um ambiente virtual para isolar as dependências do projeto.

### 2. Clonar o Repositório

Clone o repositório do projeto a partir do GitHub.<br>
Para isso, abra o terminal dentro de uma pasta e:

```
git clone <URL_DO_REPOSITORIO>
cd nome-do-projeto
```

### 2. Para rodar o projeto
```
python3 app.py

Ou

flask run
```
