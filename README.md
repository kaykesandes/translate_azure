# 🌐 Tradutor Inteligente Azure

Um sistema Python avançado para tradução de documentos Word e artigos web usando duas poderosas APIs da Azure: **Azure Translator Service** e **Azure OpenAI GPT-4**.

## 📋 Descrição

Este projeto combina duas abordagens de tradução:
1. **Tradução Tradicional**: Azure Translator para documentos Word (.docx)
2. **Tradução Inteligente**: Azure OpenAI GPT-4 para artigos web com contexto e formatação Markdown

O sistema extrai texto de URLs, processa documentos locais e oferece traduções de alta qualidade mantendo contexto e formatação.

## ✨ Funcionalidades

- 📄 **Tradução de documentos Word** (.docx) - processamento parágrafo por parágrafo
- � **Extração e tradução de artigos web** - de qualquer URL
- 🤖 **IA contextual** - usando GPT-4 para traduções mais naturais
- 🔄 **Dual API** - Azure Translator + Azure OpenAI
- �🌍 **Suporte a múltiplos idiomas** (configurável)
- 🔐 **Configuração segura** via variáveis de ambiente
- 📝 **Preservação de formatação** - Markdown para artigos web
- 🧹 **Limpeza de conteúdo** - remove scripts e estilos desnecessários

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Azure Translator Service** - API de tradução tradicional
- **Azure OpenAI GPT-4** - IA para tradução contextual
- **LangChain** - Framework para integração com LLMs
- **BeautifulSoup4** - Extração de texto de páginas web
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
   # Azure Translator Service
   subscription_key=sua_chave_do_azure_translator
   endpoint=https://api.cognitive.microsofttranslator.com/
   location=sua_regiao_azure
   
   # Azure OpenAI Service
   azure_endpoint=https://seu-recurso.openai.azure.com/
   api_version_azure=2024-12-01-preview
   api_key_azure=sua_chave_do_azure_openai
   deployment_name=gpt-4o-mini
   ```

## ⚙️ Configuração do Azure

### Azure Translator Service
1. **Acesse o Portal Azure** (https://portal.azure.com)
2. **Crie um recurso "Translator"**
3. **Obtenha as credenciais:**
   - Chave de assinatura (subscription_key)
   - Endpoint da API
   - Região/localização

### Azure OpenAI Service
1. **Crie um recurso "Azure OpenAI"**
2. **Deploy um modelo GPT-4** (recomendado: gpt-4o-mini)
3. **Obtenha as credenciais:**
   - Endpoint do Azure OpenAI
   - Chave da API
   - Nome do deployment
   - Versão da API

## 🚀 Uso

### Modo Atual: Tradução de Artigos Web

O script está configurado para extrair e traduzir artigos de URLs da web:

```bash
python init.py
```

**O que acontece:**
1. 🌐 Extrai o texto da URL configurada (Dev.to article)
2. 🧹 Remove scripts, estilos e elementos desnecessários 
3. 🤖 Traduz usando GPT-4 com contexto inteligente
4. 📝 Retorna o resultado em formato Markdown
5. 🖨️ Exibe a tradução no terminal

### Modo Alternativo: Tradução de Documentos Word

Para traduzir documentos Word, modifique o final do `init.py`:

```python
# Comente as linhas de tradução web:
# url = "https://dev.to/kenakamu/azure-open-ai-in-vnet-3alo"
# text = extract_text_from_url(url)
# article = translate_article(text, target_language)

# Descomente para traduzir documentos:
input_file = 'document.docx'
translate_document(input_file)
```

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
├── init.py              # 🐍 Script principal com toda a lógica
├── document.docx        # 📄 Documento original (opcional)
├── document_pt-br.docx  # 📄 Documento traduzido (gerado)
├── .env                 # 🔐 Variáveis de ambiente (Azure keys)
├── .gitignore          # 🚫 Arquivos ignorados pelo Git
├── README.md           # 📖 Documentação completa
└── venv/               # 🐍 Ambiente virtual Python
```

## 🔄 Fluxo de Execução

### Para Artigos Web (Modo Atual):
```
1. 🌐 URL → extract_text_from_url()
   ├── Requisição HTTP
   ├── Parse HTML com BeautifulSoup
   ├── Remoção de scripts/estilos
   └── Texto limpo extraído

2. 📝 Texto → translate_article()
   ├── Configuração LangChain + GPT-4
   ├── Prompt contextual para tradução
   ├── Processamento IA com contexto
   └── Resposta em Markdown

3. 🖨️ Saída → Terminal + Arquivo
```

### Para Documentos Word:
```
1. 📖 .docx → translate_document()
   ├── Abertura com python-docx
   ├── Iteração por parágrafos
   └── Lista de textos

2. 🌐 Cada parágrafo → translator_text()
   ├── Azure Translator API
   ├── Configuração headers/params
   └── Tradução individual

3. 📝 Reconstrução → Novo documento
   ├── Criação documento vazio
   ├── Adição de parágrafos traduzidos
   └── Salvamento com sufixo idioma
```

## 🧠 Lógica do Sistema

### Arquitetura de Duas Camadas

O projeto utiliza **duas APIs complementares** do Azure:

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Entrada       │    │   Processamento  │    │     Saída       │
│                 │    │                  │    │                 │
│ • URLs Web      │────│ • Azure Trans.   │────│ • Texto PT-BR   │
│ • Docs Word     │    │ • Azure OpenAI   │    │ • Formato MD    │
│                 │    │ • BeautifulSoup  │    │ • Docs Word     │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

### 🔧 Funções Principais

#### `extract_text_from_url(url)`
**Lógica:** Extração inteligente de conteúdo web
- 🌐 Faz requisição HTTP para a URL
- 🧹 Remove elementos `<script>` e `<style>` com BeautifulSoup
- 📄 Extrai texto limpo separado por espaços
- 🔄 Processa linha por linha, removendo espaços vazios
- ✅ Retorna texto estruturado e limpo

#### `translator_text(text, target_language)`
**Lógica:** Tradução tradicional via Azure Translator
- 🔑 Configura headers com chaves de autenticação
- 📡 Envia requisição POST para API do Azure Translator
- 🌍 Especifica idioma origem (EN) e destino (PT-BR)
- 📊 Processa resposta JSON e extrai tradução
- ✅ Retorna texto traduzido

#### `translate_article(text, target_language)`
**Lógica:** Tradução inteligente via GPT-4
- 🤖 Cria cliente Azure OpenAI com LangChain
- 💬 Configura mensagens: System (papel) + User (tarefa)
- 🧠 GPT-4 traduz com contexto e conhecimento linguístico
- 📝 Formata resposta em Markdown automaticamente
- ✅ Retorna tradução contextualizada

#### `translate_document(path)`
**Lógica:** Processamento de documentos Word
- 📖 Abre documento Word com python-docx
- 🔄 Itera parágrafo por parágrafo
- 🌐 Traduz cada parágrafo via Azure Translator
- 📝 Reconstrói documento mantendo estrutura
- 💾 Salva como novo arquivo com sufixo do idioma

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

## 🎯 Diferenças entre as APIs

| Característica | Azure Translator | Azure OpenAI GPT-4 |
|----------------|------------------|---------------------|
| **Velocidade** | ⚡ Muito rápida | 🐌 Mais lenta (IA) |
| **Custo** | � Baixo | 💰💰 Maior |
| **Precisão** | 📊 Literal | 🧠 Contextual |
| **Formatação** | ❌ Perde formato | ✅ Mantém Markdown |
| **Contexto** | ❌ Palavra-palavra | ✅ Entende contexto |
| **Criatividade** | ❌ Mecânica | ✅ Natural e fluida |

## �📝 Melhorias Futuras

- [ ] **Interface gráfica** (Streamlit/Tkinter)
- [ ] **Suporte a múltiplos formatos** (PDF, TXT, HTML)
- [ ] **Tradução híbrida** (combinar ambas APIs)
- [ ] **Cache inteligente** de traduções
- [ ] **Processamento em lote** de múltiplos arquivos
- [ ] **API REST** para integração externa
- [ ] **Logs detalhados** e métricas
- [ ] **Testes unitários** automatizados
- [ ] **Deploy na nuvem** (Azure Functions)
- [ ] **Interface web** responsiva

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