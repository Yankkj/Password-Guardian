# Password Guardian

## ⚠️ AVISO IMPORTANTE

# Este projeto é exclusivamente para fins educacionais e de estudo.

# Não deve ser utilizado como:

1. **Fonte primária para pesquisa sobre segurança de senhas**
2. **Solução real de gerenciamento de credenciais**
3. **Base para sistemas de autenticação em produção**

# Usuários devem ter conhecimento prévio em segurança cibernética antes de testar a aplicação. O desenvolvedor não se responsabiliza por:

1. **Uso indevido das ferramentas**
2. **Danos decorrentes da aplicação em ambientes reais**
3. **Perdas por falsa sensação de segurança**

### Visão Geral

O **Password Guardian** é uma aplicação desktop desenvolvida em Python com `customtkinter` para fornecer aos usuários um conjunto de ferramentas essenciais para gerenciar e fortalecer suas credenciais online. É ideal para quem busca entender melhor a qualidade de suas senhas e como protegê-las contra ameaças comuns.

### Funcionalidades

- **Análise de Força de Senha:** Avalia a complexidade e a resistência de uma senha contra ataques de força bruta, fornecendo um score e sugestões para melhoria.
- **Verificação de Vazamento:** Consulta o banco de dados do "Have I Been Pwned?" para verificar se uma senha específica foi comprometida em violações de dados conhecidas.
- **Geração de Senhas Fortes:** Cria senhas aleatórias e personalizáveis, incluindo a opção de gerar "frases-senha" (passphrases) longas e fáceis de memorizar.
- **Dicas de Segurança:** Oferece um guia conciso com as melhores práticas para a criação, gerenciamento e proteção de senhas.
- **Interface Gráfica Intuitiva:** Desenvolvido com `customtkinter` para uma experiência de usuário moderna e agradável.

## Como Usar

### Pré-requisitos

Certifique-se de ter o [Python 3.x](https://www.python.org/downloads/) instalado em seu sistema.

### Instalação e Execução

Para iniciar o Password Guardian, siga os passos abaixo:

1.  **Clone o repositório** para o seu computador:

    ```bash
    git clone [https://github.com/Yankkj/password-guardian.git](https://github.com/Yankkj/password-guardian.git)
    cd password-guardian
    ```

2.  **Execute o script de inicialização** (Windows):
    Basta dar um duplo clique no arquivo `run_app.bat` localizado na raiz do projeto.

    **Para usuários Linux/macOS:**
    Abra o terminal na pasta raiz do projeto e execute:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python3 -m src.main
    ```

    O script `run_app.bat` (ou os comandos manuais para Linux/macOS) irá:

    - Verificar e criar um ambiente virtual (`venv`) se ele não existir.
    - Ativar o ambiente virtual.
    - Instalar todas as dependências necessárias listadas em `requirements.txt`.
    - Iniciar a aplicação Password Guardian.

### Navegação na Interface

- **Aba "Analisar Senha"**: Digite uma senha e clique em "Analisar" para ver a força e sugestões.
- **Aba "Verificar Vazamento"**: Insira uma senha para checar se ela apareceu em vazamentos de dados.
- **Aba "Gerar Senha"**: Use os controles para personalizar e gerar novas senhas ou frases-senha.
- **Aba "Dicas de Segurança"**: Leia as recomendações para manter suas senhas seguras.
- **Aba "Sobre"**: Informações sobre o projeto e o desenvolvedor.

## Testes

Para garantir a integridade do código, o projeto inclui testes unitários usando `pytest`.

1.  **Ative o ambiente virtual** (se ainda não estiver ativo):

    ```bash
    cd password-guardian
    .\venv\Scripts\activate  # Windows
    # ou
    source venv/bin/activate # Linux/macOS
    ```

2.  **Execute os testes**:

    ```bash
    pytest
    ```

    Você verá um relatório indicando quais testes passaram ou falharam.

## Contribuição

Contribuições são bem-vindas! Se você tiver ideias para melhorias, novas funcionalidades ou encontrar bugs, por favor.

Contribuições devem:

1. Manter o propósito educativo

2. Incluir avisos de segurança

3. Evitar implementações de criptografia real

## Contato

- **Criador:** yankkjj
- **GitHub:** [https://github.com/Yankkj](https://github.com/Yankkj)
- **Discord:** imundar
- **Telegram:** feicoes

## Agradeço por usar o **Password Guardian!**
