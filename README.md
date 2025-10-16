🧮 Sistema de Cadastro e Relatórios de Alunos

Este projeto é uma aplicação desktop desenvolvida em Python com Tkinter e Pandas, que permite cadastrar alunos, visualizar em tabela, filtrar por nota, e gerar relatórios em CSV. O sistema é ideal para 
gerenciamento simples de dados escolares, com interface gráfica intuitiva e funcional.

🚀 Funcionalidades:

📋 Cadastro de Alunos: Adiciona novos alunos com nome, idade, curso e nota final.

📊 Tabela Dinâmica: Visualização automática dos alunos cadastrados em uma tabela interativa.

🔍 Filtragem: Filtra os alunos com nota acima de uma média informada.

💾 Salvar e Carregar CSV: Permite salvar os dados em um arquivo .csv e carregar novamente quando necessário.

📈 Exportar Relatórios Filtrados: Gera um arquivo .csv apenas com os alunos que têm nota acima da média digitada.

⚠️ Mensagens Interativas: Exibe alertas e confirmações com messagebox para facilitar a interação do usuário.

🧠 Tecnologias Utilizadas

Python 3.10+

Tkinter – Interface gráfica

Pandas – Manipulação de dados em tabelas

ttk.Treeview – Exibição dos dados em formato de tabela

messagebox e filedialog – Alertas e janelas de salvar/abrir arquivos

os – Manipulação de caminhos de arquivos

🗂️ Estrutura do Código

├── sistema_alunos.py → Código principal com toda a lógica do sistema
├── alunos.csv (opcional) → Arquivo gerado após salvar/exportar
└── README.md → Documento explicativo

⚙️ Como Executar o Projeto

1️⃣ Instalar dependências:
Certifique-se de ter o Python instalado e execute no terminal:
pip install pandas

2️⃣ Executar o programa:
No terminal (ou prompt de comando), execute:
python sistema_alunos.py

A janela do sistema será aberta automaticamente.

🖥️ Interface do Sistema
A aplicação é dividida em três seções principais:

Cadastro de Aluno: Campos para inserir nome, idade, curso e nota → Clique em Cadastrar para adicionar à tabela.

Tabela de Alunos: Exibe todos os registros cadastrados → Atualiza automaticamente após cada cadastro.

Funções Extras:

Digite uma média e clique em Filtrar para mostrar apenas notas acima.

Exportar Filtrado: Salva somente os registros filtrados.

Salvar CSV: Grava todos os dados em um arquivo .csv.

Carregar CSV: Reabre um arquivo salvo anteriormente.

📄 Exemplo de Uso
1️⃣ Preencha os campos:

Nome: Maria Silva

Idade: 20

Curso: Engenharia

Nota Final: 8.5
2️⃣ Clique em Cadastrar — o aluno será adicionado à tabela.
3️⃣ Para gerar um relatório de notas acima de 7, digite 7 e clique em Filtrar.
4️⃣ Exporte os resultados com Exportar Filtrado ou salve todos os dados com Salvar CSV.

📦 Arquivo CSV Gerado
Exemplo de arquivo .csv gerado pelo sistema:
Nome,Idade,Curso,Nota Final
Maria Silva,20,Engenharia,8.5
João Souza,22,Direito,7.8
Ana Lima,19,Medicina,9.1

🧰 Estrutura Lógica (Resumo das Funções)
Função	Descrição
cadastrar()	Cadastra novo aluno e atualiza a tabela
atualizar_tabela()	Atualiza o conteúdo visual da tabela (Treeview)
limpar_campos()	Limpa os campos de entrada após o cadastro
filtrar_notas()	Mostra apenas alunos com nota acima da média informada
salvar_csv()	Salva todos os dados em arquivo .csv
carregar_csv()	Carrega arquivo .csv existente para o sistema
exportar_filtrado()	Gera relatório apenas dos alunos filtrados
