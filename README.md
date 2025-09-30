# 🌐 Tradutor de Documentos Azure

Um projeto Python para tradução automática de documentos Word (.docx) utilizando o Azure Translator Service.

## 📋 Descrição

Este projeto permite traduzir documentos Word automaticamente do inglês para português brasileiro (ou outros idiomas) usando a API do Azure Translator. O sistema processa cada parágrafo do documento, mantendo a formatação básica.

## ✨ Funcionalidades

- 📄 Tradução de documentos Word (.docx)
- 🔄 Processamento parágrafo por parágrafo
- 🌍 Suporte a múltiplos idiomas (configurável)
- 🔐 Configuração segura via variáveis de ambiente
- 📝 Preservação da estrutura do documento

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Azure Translator Service** - API de tradução
- **python-docx** - Manipulação de documentos Word
- **requests** - Requisições HTTP
- **python-dotenv** - Gerenciamento de variáveis de ambiente

## 📦 Instalação

### Pré-requisitos

- Python 3.7 ou superior
- Conta Azure com Translator Service ativo
- Chave de API e endpoint do Azure Translator

### Passos de Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/kaykesandes/translate_azure.git
   cd translate_azure
   ```

2. **Crie um ambiente virtual:**
   ```bash
   python -m venv venv
   ```

3. **Ative o ambiente virtual:**
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```
   - Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Instale as dependências:**
   ```bash
   pip install requests python-docx python-dotenv
   ```

5. **Configure as variáveis de ambiente:**
   
   Crie um arquivo `.env` na raiz do projeto:
   ```env
   subscription_key=sua_chave_do_azure_translator
   endpoint=https://api.cognitive.microsofttranslator.com
   location=sua_regiao_azure
   ```

## ⚙️ Configuração do Azure

1. **Acesse o Portal Azure** (https://portal.azure.com)
2. **Crie um recurso Translator Service**
3. **Obtenha as credenciais:**
   - Chave de assinatura (subscription_key)
   - Endpoint da API
   - Região/localização

## 🚀 Uso

### Uso Básico

1. **Coloque seu documento Word** na pasta do projeto com o nome `document.docx`

2. **Execute o script:**
   ```bash
   python init.py
   ```

3. **Resultado:** O documento traduzido será salvo como `document_pt-br.docx`

### Personalização

Para alterar o idioma de destino, modifique a variável `target_language` no arquivo `init.py`:

```python
target_language = 'pt-br'  # Português brasileiro
# target_language = 'es'   # Espanhol
# target_language = 'fr'   # Francês
# target_language = 'de'   # Alemão
```

### Idiomas Suportados

O Azure Translator suporta mais de 100 idiomas. Alguns códigos comuns:

- `pt-br` - Português (Brasil)
- `es` - Espanhol
- `fr` - Francês
- `de` - Alemão
- `it` - Italiano
- `ja` - Japonês
- `ko` - Coreano
- `zh` - Chinês

## 📁 Estrutura do Projeto

```
translate_azure/
├── init.py              # Script principal
├── document.docx        # Documento original (exemplo)
├── document_pt-br.docx  # Documento traduzido (gerado)
├── .env                 # Variáveis de ambiente
├── .gitignore          # Arquivos ignorados pelo Git
├── README.md           # Documentação
└── venv/               # Ambiente virtual
```

## 🔧 Funções Principais

### `translator_text(text, target_language)`
Traduz um texto específico usando a API do Azure Translator.

**Parâmetros:**
- `text`: Texto a ser traduzido
- `target_language`: Código do idioma de destino

**Retorna:** Texto traduzido

### `translate_document(path)`
Traduz um documento Word completo.

**Parâmetros:**
- `path`: Caminho para o arquivo .docx

**Retorna:** Caminho do arquivo traduzido

## 🔒 Segurança

- ✅ Credenciais armazenadas em variáveis de ambiente
- ✅ Arquivo `.env` incluído no `.gitignore`
- ✅ Headers de segurança nas requisições à API

## 🤝 Contribuições

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📝 Melhorias Futuras

- [ ] Interface gráfica (GUI)
- [ ] Suporte a múltiplos formatos (PDF, TXT)
- [ ] Tradução em lote
- [ ] Preservação avançada de formatação
- [ ] Cache de traduções
- [ ] Logs detalhados
- [ ] Testes unitários

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👤 Autor

- **Kayke Sandes** - [@kaykesandes](https://github.com/kaykesandes)

## 🙏 Agradecimentos

- Microsoft Azure pela API de tradução
- Comunidade Python pelas bibliotecas utilizadas
- DIO (Digital Innovation One) pela inspiração do projeto

## 📞 Suporte

Se você encontrar algum problema ou tiver dúvidas:

1. Verifique a documentação do Azure Translator
2. Confira se as variáveis de ambiente estão corretas
3. Abra uma issue no GitHub

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!