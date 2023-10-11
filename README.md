# MorizeApp 🔭

Ola, o Morize App é uma aplicação web, que permite o gerenciamento de um instituição de ensino, permitindo que usuários e professores consigam interagir, mantendo e acompanhando um ciclo de entregas que relaciona atividades diretamente de alunos interfaceado por grupos de alunos e turmas.

## Recursos:

### Autenticação e Nível de Usuário:
O sistema tem a autenticação baseado em usuário e senha, o mesmo também permite o acesso distinto aos três tipos de usuário.
#### Diretor:
O usuário do tipo diretor, pode cadastrar, alunos, professores, turmas, grupos de aluno e outros diretores. Este usuário também pode relacionar essas entidades, ou seja atribuir alunos a grupos de alunos ou turmas e atribuir professores a turmas de aluno.

#### Professor:
O Professor é responsável por grande parte da concepção do Ciclo de Entregas, ou seja define as datas do mesmo, como também a descrição das atividades. Também é responsabilidade do professor atribuir as devidas notas aos alunos por atividade.

#### Aluno:
O Aluno tem ações somente a nível mais passivo, uma vez que o mesmo apenas acompanha o Ciclo de Entregas, como seu score parcial e final referentes ao próprio ciclo de entregas.

### Gerenciamento de Turmas
As turmas permitem um agrupamento de alunos, por característica comum, no caso relacionam os alunos a um ciclo de entregas comum definido pelo professor.

### Gerenciamento de Grupos de Aluno
Grupos de aluno são uma abstração de alunos pertencentes a mesma turma, servido para especificar os usuários dentro de um conjunto já especifico que é a turma.


### Ciclo de Entregas:
O Ciclo de entrega, relaciona todas as entidades do sistema, salvo os diretores, uma vez que através de datas define seu ciclo de vida, um ciclo de entregas permite ao professor atribuir notas as atividades, gerando assim um score que os alunos podem acompanhar de desde sua parcialidade.

### Fluxograma da Aplicação:
Acesse o fluxograma da aplicação através do Miro, clicando no link que segue: <br>
<a href="https://miro.com/welcomeonboard/YlRPSEFoVjhnZGoxempKd2k4aW5EQmpFZ0JOVVVYRU02Mk1OY1VmNlQ3Wm9qc002TlFCeWxzR2FoYzB1cjFMS3wzNDU4NzY0NTYzNTMzMTc5OTk2fDI=?share_link_id=665929022673">Ir para o Miro</a>
### WireFrame
Acesse o wire frame da aplicação através do Figma, clicando no link que segue:<br>
<a href="https://www.figma.com/file/z3ULTstviHzHjpTrmdqyky/Untitled?type=design&node-id=0%3A1&mode=design&t=7X3mwSH3mpjgNpdP-1">Ir para o Figma</a>

### Backlog
| **COMO UM** |  **EU QUERO**  | **PARA** | **PRIORIDADE** | **SPRINT** | **STATUS** |
|-----------------------|-------------------------|-------------------------|---------------------|----------------|-------------------------|
| Usuário | Login/Log-off| Acessar o sistema | Imprescindível | 3 | **-** |
| Diretor | Cadastrar usuários | Acessar o sistema | Imprescindível | 3 | **-** |
| Diretor | Cadastrar turmas e grupo de alunos | Organização | Imprescindível | 3 | **-** |
| Diretor | Editar e excluir contas, grupos de alunos e turmas| Corrigir erros e fazer alterações | Importante | 4 | **-** |
| Professor | Visualizar desempenho individual do aluno | Visualizar notas do aluno | Importante | 3 | **-** |
| Professor | Visualizar grupo de alunos | Visualizar alunos de um grupo específico | Importante | 3 | **-** |
| Professor | Inserir nota no ciclo de entrega | Nota individual para o aluno | Importante | 4 | **-** |
| Aluno | Ver as médias das minhas notas | Noção de performance  | Importante | 3 | **-** |
| Desenvolvedor | Criar documentação do produto | Organização | Imprescindível | 1 | **Realizado** |
| Desenvolvedor | Criar fluxograma e wireframes  do produto | Organização | Imprescindível | 1 | **Realizado** |
| Desenvolvedor | Criar Backlog do produto | Organização | Imprescindível | 1 | **Realizado** |
| Desenvolvedor | Criar conta no Jira e gerenciar as tasks realizadas durante as sprints | Organização | Imprescindível | 1 | **Realizado** |
| Desenvolvedor | Aplicar restrições e hierarquias e usuários | Organização | Imprescindível | 2 | **-** |
| Desenvolvedor | Desenvolver as telas do produto sem funcionalidades| Desenvolvimento | Imprescindível | 2 | **-** |
| Desenvolvedor | Realizar a conexão das telas com o backend | Desenvolvimento | Imprescindível | 3 | **-** |

## Tecnologias usadas
### Backend:
 - Python 🐍 : Framework Flask
### Frontend:
 - Bootstrap: Framework Frontend

#### Membros da Equipe:
<img src="https://github.com/ElbertJean/faculdade/blob/fee37ec7da5f4662fc041bd241c0d3203e499728/Frame%202.png" width="100%"/>

## Instalação

 # Passo-a-passo para Instalação de uma Aplicação Python

### 1. Preparação do Ambiente

Certifique-se de ter o Python instalado em seu sistema. Você pode baixá-lo em [Python Official Website](https://www.python.org/). Além disso, é recomendável criar um ambiente virtual para isolar as dependências do projeto.

### 2. Clonar o Repositório

Clone o repositório do projeto a partir do GitHub.

bash
git clone <URL_DO_REPOSITORIO>
cd nome-do-projeto


### 3. Criar o primeiro usuário Diretor
bash
python firstUsr.py


