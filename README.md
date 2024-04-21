# (PT) Tradutor de Termos de Sistema

## Descrição do Projeto
Este projeto foi desenvolvido para facilitar a localização de softwares, traduzindo termos de sistemas do inglês para o português de forma automatizada. Utilizando a poderosa API da OpenAI, com o modelo GPT-3.5-turbo-0125, o sistema garante traduções precisas e adaptadas ao contexto de uso, o que é fundamental para a usabilidade e compreensão em ambientes multilíngues.

## Estrutura do Arquivo
O arquivo CSV necessário para o processo deve seguir um formato específico com duas colunas: `INDEX` e `English`. A coluna `INDEX` representa o identificador único de cada termo no sistema, enquanto `English` contém o texto original em inglês que será traduzido.

## Fluxo de Trabalho Detalhado
1. **Inicialização**: O usuário ativa o sistema e faz o upload do arquivo CSV.
2. **Carregamento de Dados**: O arquivo é carregado e preparado para processamento.
3. **Conexão com a API**: O sistema estabelece uma conexão segura com a API da OpenAI.
4. **Processamento de Tradução**: Cada linha do arquivo é processada individualmente, traduzindo o termo do inglês para o português.
5. **Geração de Saída**: As traduções são inseridas numa nova coluna denominada `Portuguese`.
6. **Exportação**: O arquivo CSV é atualizado com as traduções e pronto para ser exportado.

## Benefícios da Utilização de IA
A utilização de inteligência artificial através do modelo GPT-3.5-turbo-0125 permite não apenas traduções rápidas, mas também altamente contextuais, considerando nuances culturais e técnicas, o que é essencial para a precisão terminológica em diferentes domínios de aplicação.

## Considerações Finais
Este sistema é ideal para desenvolvedores de software, gestores de produto e equipes de localização que buscam agilizar o processo de adaptação de seus sistemas para o mercado brasileiro, garantindo assim uma maior acessibilidade e satisfação do usuário final.


--------


# (EN) System Terms Translator

## Project Description
This project is designed to facilitate software localization by automatically translating system terms from English to Portuguese. Leveraging the powerful OpenAI API with the GPT-3.5-turbo-0125 model, the system ensures precise translations that are contextually adapted, which is crucial for usability and understanding in multilingual environments.

## File Structure
The necessary CSV file for the process should follow a specific format with two columns: `INDEX` and `English`. The `INDEX` column represents the unique identifier for each term in the system, while `English` contains the original English text to be translated.

## Detailed Workflow
1. **Initialization**: The user activates the system and uploads the CSV file.
2. **Data Loading**: The file is loaded and prepared for processing.
3. **API Connection**: The system establishes a secure connection with the OpenAI API.
4. **Translation Processing**: Each line of the file is individually processed, translating the term from English to Portuguese.
5. **Output Generation**: Translations are inserted into a new column named `Portuguese`.
6. **Exportation**: The CSV file is updated with the translations and ready to be exported.

## Benefits of Using AI
Using artificial intelligence through the GPT-3.5-turbo-0125 model not only allows for quick translations but also highly contextual ones, considering cultural and technical nuances, which is essential for terminological accuracy across different application domains.

## Final Considerations
This system is ideal for software developers, product managers, and localization teams looking to streamline the process of adapting their systems to the Brazilian market, thereby ensuring greater accessibility and end-user satisfaction.
