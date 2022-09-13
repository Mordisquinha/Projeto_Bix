# Projeto_Bix
Fase teste para o processo seletivo da empresa BIX Tecnologia.
Planejado e desenvolvido por Gabriel Santiago.

A - Sobre o Projeto:

    O projeto consiste na resolução ao desafio proposto, o qual se baseia em:

        1 - Consumir dados de uma tabela de vendas do banco de dados postgresql dado pelo desafiante.

        2 - Consumir dados de uma API dada pelo desafiante, com dados de funcionários cujo o assesso é pelo ID.

        3 - Consumir dados de um arquivo .parquet através de um link dado pelo desafiante, com dados de categorias.

        4 - Criar uma pipeline para movimentar esses dados para um banco de dados pessoal onde o objetivo é no final ter
        as vendas, os funcionários e as categorias em um só lugar.

        5 - Tendo o requisito de: realizar a movimentação dos dados diariamente, pois essas fontes de dados são alimentadas periodicamente. Por isso, é necessário o uso de um orquestrador, no caso deste projeto, o Airflow.

B - Sobre a estruturação do projeto:

    O projeto é estruturado primordialmente pela divisão entra as etapas stage e relacional.

    Na etapa stage, os dados brutos de vendas, funcionário e categorias é carregado no schema stg do banco de dados mysql.

    Na etapa rel, adicionam-se as colunas de inserção base e exclusão lógica ao final da tabela, para assim garantir o melhor controle no processo de etl.

    1 - Etapa Stage:

        A etapa stage está dentro da pasta "ETAPA_STG".

        A criação do schema stg do meu banco mysql é feita através da biblioteca sqlalchemy, com programação orientada a 
        objeto.

        Sobre a criação do schema:

            1 - arquivo models.py:
                
                Nele há as classes das tabelas stages (stg.funcionarios, stg.vendas, stg.categorias).

                Definindo assim as colunas que irão pertencer a estas tabelas e o tipo de cada coluna.

                Nestas classes também definimos as chaves primárias e estrangeiras deste schema.

            2 - arquivo database.py:

                Aqui está a credencial necessária para criar a engine no sql alchemy e algumas variáveis que irão ser
                necessárias ao longo do projeto.
            
            3 - arquivo create_db.py:

                Este arquivo é o "play" para a criação de todas as tabelas do schema stage.

        Arquivo funcoes_db.py:

            Aqui foi escrita a classe "Connect_db()", onde estão todas as funções e métodos que irão ser
            usados ao longo do processo de etl, como querys e inserts nas tabelas do mysql.

        Ariquivo api.py:

            Este é reponsável pela consulta à api, cedida para o projeto, em que existe a verificação da possibilidade do aumento do número de id's nesta.

            Ela faz a consulta de id por id começando de 1 até o último valor presente na api, e insere o funcionário e
            o id do mesmo na tabela de funcionário no mysql.

        Arquivo parquet.py:

            parquet.py faz o download do arquivo .parquet, extrai os dados, insere na tabela de categorias do mysql e 
            exclui o arquivo .parquet no final do processo.
        
        Arquivo postgress.py:

            Tem a função de se conectar ao banco postgresql cedido pelo desafiante, ler e extrair os dados da tabela de
            vendas deste banco de dados e carregar os dados na tabela de vendas do banco mysql pessoal.

    2 - Etapa Rel:

        A etapa rel está dentro da pasta "ETAPA_REL".

        A criação do schema rel do meu banco mysql é feita através da biblioteca sqlalchemy, com programação orientada a 
        objeto, assim como na etapa stg, o mesmo vale para os arquivos models.py, database.py, create_db.py e 
        funcoes_db.py, pois todos estes arquivos tem o mesmo propósito nesta etapa.

        Além disso, a etapa rel é dividida em mais duas partes:

        Arquivos .sql:

            Os arquivos .sql (insert_funcionarios, insert_categorias, insert_vendas) são querys sql para a inserção das 
            tabelas relacionais. Estas querys alocam sempre os dados faltantes entre as tabelas relacionais e stages 
            através de um "left join".

        Arquivo insert_rel.py:

            Esta etapa nada mais é que a leitura dos scrips sql da etapa anterior e o processo de insert nas tabelas
            relacionais do banco pessoal mysql.

    3 - Airflow Dag:

        Como foi mencionado anteriormente, era necessário um orquestrador para os processos de carga acontecerem diariamente. Por este motivo existe uma dag do airflow neste repositório (dag.py), onde este arquivo 
        contém todas as informações necessárias para o airflow disparar este processo na ordem exata: Etapa stage e
        depois Etapa relacional.

    
C - Notas finais:

    1 - Este projeto está inteiramente na nuvem, as pastas "ETAPA_STG" e "ETAPA_REL" estão em uma máquina ec2 na aws (servidor_bix) e
    o airflow junto com o arquivo "dag.py" está hospedado em outra máquina ec2 (Airflow). Ambas se comunicam através de ssh com o operador de ssh pertencente ao airflow.

    2 - Todas as credenciais e informações sensíveis estão alocadas em variáveis de ambientes no servidor_bix e são usadas no código a partir da biblioteca "os".

    3 - Todas as tabelas stages são truncadas no início do processo de inserção e carregadas com os dados da própria fonte, somente as tabelas
    relacionais que possuem a inserção incremental, pois só recebem os dados que elas não contém. 

    4 - A aplicação Airflow no projeto foi subida através de uma imagem docker fornecida pela própria documentação do Airflow e usou docker compose para levantar todos os containers necessários para esta aplicação rodar.

D -  Tecnologias usadas: 

    1 - aws ec2:

        usada para hospedar o servidor_bix e o Airflow.
    
    2 - Airflow:

        usado para fazer a orquestração da etl.

    3 - Python:

        liguagem usada para escrever os scripts etl.

    4 - SQL:

        linguagem usada para fazer os scripts de inserção.
    
    5 - aws rds:

        usado para a criação do banco de dados mysql.

    6 - pandas:

        usado para transformar os dados brutos extraídos em data frames e então fazer a inserção no banco de dados.

    7 - sqlalchemy:

        usado para a criação das tabelas e suas conexões (chaves estrangeiras).

    8 - linux:

        sistema operacional usado nos servidores para hospedagem, conhecimento usado também para a definição das variáveis de ambiente a fim
        de ocultar as informações sensíveis ao longo do processo de etl.

    9 -  docker & docker-compose:

        usado para o upload da aplicação Airflow.

    10 - git & github:

        para o versionamento do projeto.