# Análise da Relação entre Dieta e Expectativa de Vida

## Descrição
Este repositório contém um projeto de análise de dados que investiga a relação entre os tipos de dieta das diferentes espécies de primatas e sua expectativa média de vida. O objetivo é desenvolver habilidades em manipulação de dados, visualização de dados e análise estatística utilizando Python.

## Estrutura do Repositório
```plaintext
.
├── data
│ ├── raw
│ │ └── primates_dataset.csv # Dataset bruto
│ │
│ ├── processed
│ │ └── primates_dataset_clean.csv # Dataset limpo
│ │
│ └── logs
│   └── analysis.log
│
├── scripts
│ ├── dieta_expectativa_vida.py # Script Python para análise
│ ├── pyproject.toml # Arquivo de configuração do Poetry
│ └── poetry.lock # Arquivo de lock do Poetry
│
├── reports
│ └── dieta_expectativa_vida.pdf # Relatório final em PDF
│
└── README.md # Descrição do repositório e instruções
```



## Configuração do Ambiente

### Requisitos
- Python 3.11 ou superior
- Poetry (para gerenciamento de dependências)

### Instalação do Poetry
Caso não tenha o Poetry instalado, siga as instruções em [Poetry](https://python-poetry.org/docs/#installation).

### Instalação das Dependências
1. Navegue até o diretório do projeto:
    ```bash
    cd analysis-diet-life-expectancy\scripts
    ```
2. Instale as dependências utilizando o Poetry:
    ```bash
    poetry install
    ```

## Como Executar

### Usando Script Python
1. Ative o ambiente virtual do Poetry:
    ```bash
    poetry shell
    ```
2. Execute o script Python:
    ```bash
    python ./dieta_expectativa_vida.py
    ```

## Estruturação de Script

### Preparação dos Dados
- Carregar e limpar os dados do dataset `primates_dataset.csv`.
- Filtrar as colunas relevantes: `species_name`, `diet`, `avg_lifespan`.
- Verificar e tratar valores ausentes e inconsistências.

### Análise Exploratória dos Dados (EDA)
- Visualizar a distribuição dos tipos de dieta entre as diferentes espécies de primatas.
- Usar gráficos de barra para mostrar a distribuição das dietas.
- Visualizar a expectativa de vida média para cada tipo de dieta usando boxplots ou gráficos de violino.

### Visualização dos Resultados
- Criar gráficos que mostrem a relação entre dieta e expectativa de vida.
- Destacar diferenças significativas encontradas na análise estatística.

## Estruturação de Report

### Conclusões e Insights
- Resumir os principais achados da análise.
- Discutir correlações ou padrões interessantes entre dieta e expectativa de vida.
- Sugerir possíveis explicações para os resultados observados.

## Contribuições
Contribuições são bem-vindas! Por favor, abra um pull request com suas melhorias.

---

© 2024 PrimaType Brazil. Todos os direitos reservados.
