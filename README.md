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
<a href="https://miro.com/welcomeonboard/YlRPSEFoVjhnZGoxempKd2k4aW5EQmpFZ0JOVVVYRU02Mk1OY1VmNlQ3Wm9qc002TlFCeWxzR2FoYzB1cjFMS3wzNDU4NzY0NTYzNTMzMTc5OTk2fDI=?share_link_id=665929022673">
    <img src="https://github.com/ElbertJean/faculdade/blob/main/AcessarFluxograma.png" width="20%"/>
</a>

### WireFrame
Foi Desenvolvido um wireframe no Figma para o projeto. Convido você a clicar no botão abaixo para visualizar o wireframe: <br>
<a href="https://www.figma.com/file/z3ULTstviHzHjpTrmdqyky/Untitled?type=design&node-id=0%3A1&mode=design&t=7X3mwSH3mpjgNpdP-1">
    <img src="https://github.com/ElbertJean/faculdade/blob/main/AcessarWireframe.png" width="20%"/>
</a>

### Backlog do projeto
| **COMO UM** |  **EU QUERO**  | **PARA** | **PRIORIDADE** | **SPRINT** | **STATUS** |
|-----------------------|-------------------------|-------------------------|---------------------|----------------|-------------------------|
| Desenvolvedor | Criar documentação do produto | Organização | Imprescindível | 1 | **Realizado** |
| Desenvolvedor | Criar fluxograma e wireframes  do produto | Organização | Imprescindível | 1 | **Realizado** |
| Desenvolvedor | Criar Backlog do produto | Organização | Imprescindível | 1 | **Realizado** |
| Desenvolvedor | Criar conta no Jira e gerenciar as tasks realizadas durante as sprints | Organização | Imprescindível | 1 | **Realizado** |
| Desenvolvedor | Desenvolver as telas do diretor com as funcionalidades| Desenvolvimento | Imprescindível | 2 | **Realizado** |
| Diretor | Cadastrar usuários | Acessar o sistema | Imprescindível | 2 | **Realizado**|
| Diretor | Cadastrar turmas e grupo de alunos | Organização | Imprescindível | 2 | **Realizado** |
| Usuário | Login/Log-off| Acessar o sistema | Imprescindível | 3 | **-** |
| Professor | Visualizar desempenho individual do aluno | Visualizar notas do aluno | Importante | 3 | **-** |
| Professor | Visualizar grupo de alunos | Visualizar alunos de um grupo específico | Importante | 3 | **-** |
| Desenvolvedor | Aplicar restrições e hierarquias dos usuários | Organização | Imprescindível | 3 | **-** |
| Desenvolvedor | Desenvolver as telas do aluno com as funcionalidades| Desenvolvimento | Imprescindível | 3 | **-** |
| Desenvolvedor | Desenvolver as telas do professor com as funcionalidades| Desenvolvimento | Imprescindível | 3 | **-** |
| Desenvolvedor | Realizar a conexão das telas com o backend | Desenvolvimento | Imprescindível | 3 | **-** |
| Diretor | Editar e excluir contas, grupos de alunos e turmas| Corrigir erros e fazer alterações | Importante | 4 | **-** |
| Professor | Inserir nota no ciclo de entrega | Nota individual para o aluno | Importante | 4 | **-** |
| Aluno | Ver as médias das minhas notas | Noção de performance  | Importante | 4 | **-** |

### Backlog 1º Sprint
| **COMO UM** |  **EU QUERO**  | **PARA** | **PRIORIDADE** | **SPRINT** | **STATUS** |
|-----------------------|-------------------------|-------------------------|---------------------|----------------|-------------------------|
| Desenvolvedor | Criar documentação do produto | Organização | Imprescindível | 1 | **Realizado** |
| Desenvolvedor | Criar fluxograma e wireframes  do produto | Organização | Imprescindível | 1 | **Realizado** |
| Desenvolvedor | Criar Backlog do produto | Organização | Imprescindível | 1 | **Realizado** |
| Desenvolvedor | Criar conta no Jira e gerenciar as tasks realizadas durante as sprints | Organização | Imprescindível | 1 | **Realizado** |

### Backlog 2º Sprint
| **COMO UM** |  **EU QUERO**  | **PARA** | **PRIORIDADE** | **SPRINT** | **STATUS** |
|-----------------------|-------------------------|-------------------------|---------------------|----------------|-------------------------|
| Desenvolvedor | Desenvolver as telas do diretor com as funcionalidades| Desenvolvimento | Imprescindível | 2 | **Realizado** |
| Diretor | Cadastrar usuários | Acessar o sistema | Imprescindível | 2 | **Realizado** |
| Diretor | Cadastrar turmas e grupo de alunos | Organização | Imprescindível | 2 | **Realizado** |


## Tecnologias utilizadas e Integrantes
<img src="https://github.com/ElbertJean/faculdade/blob/main/Frame%203%20(2).jpg" width="100%"/>

## Instalação

 # Passo-a-passo para Instalação de uma Aplicação Python

### 1. Preparação do Ambiente

Certifique-se de ter o Python instalado em seu sistema. Você pode baixá-lo em [Python Official Website](https://www.python.org/). Além disso, é recomendável criar um ambiente virtual para isolar as dependências do projeto.

### 2. Clonar o Repositório

Clone o repositório do projeto a partir do GitHub.

bash <br>
git clone <URL_DO_REPOSITORIO> <br>
cd nome-do-projeto <br>


### 3. Criar o primeiro usuário Diretor
bash
python firstUsr.py
