# Comida di Buteco 2022 - WebScraper

O script foi criado apenas para diversão - eu queria a lista completa dos participantes do Comida di Buteco 2022 no Rio de Janeiro, podendo organizar por bairro, ordem alfabética, marcar se já fui, nota, etc. Para exercitar as habilidades com Selenium, criei esse robô raspador.

O robô gera dois arquivos:

    - links.csv, com os links de todas as páginas de restaurantes participantes
    - restaurantes.csv, os dados de cada um dos restaurantes

O arquivo atual de restaurantes não é o mesmo originado pelo Robô. O arquivo atual foi tratado para ser disponibilizado de forma mais aprazível [aqui, no Google Spreadsheets](https://docs.google.com/spreadsheets/d/1A6rT4zr8Y0CsUGly5cnyt38IF6Sx-bc4bWNRa8RBiUA/)

Qualquer melhoria, sugestão ou crítica é bem-vinda. Há muito o que fazer, como:

[ ] Lista de cidades

[ ] Verificar se a página é de um restaurante ou não (ao invés de remover os links raspados, como no script)

[ ] Fazer o processo de manipulação (feito externamente) no próprio script, criando a variável de bairro, limpando endereço e telefone, corrigindo horários, etc

[ ] Fazer rodar headless.

Um dia tudo isso será feito por mim (mas se quiser fazer, pode dar um pull request!). Estou um pouco ocupado visitando os restaurantes ;)

Dados retirados de: [Comida di Buteco](http://www.comidadibuteco.com.br/)