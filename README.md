# Mongatron Discord Bot

Mongatron é um bot de Discord que interage como um personagem de IA, utilizando a API do ChatGPT. Ele responde às mensagens prefixadas com "mongatron" e também pode responder aleatoriamente às mensagens no servidor.

### Clone o repositorio
```sh
git clone https://github.com/seu-usuario/discord-bot.git
cd discord-bot
```

### Configurar Variáveis de Ambiente
- Crie um arquivo .env na raiz do projeto e adicione as seguintes variáveis de ambiente:
```ini
DISCORD_TOKEN=seu-token-aqui
DISCORD_GUILD_ID=id-do-servidor-aqui
DISCORD_CHANNEL_ID=id-do-canal-aqui
OPENAI_API_KEY=sua-api-key-do-openai-aqui
```

### Instalar Dependências
- Instale as dependências necessárias:
```bash
pip install -r requirements.txt
```

### Execução
- Para rodar o bot localmente, use:
```bash
python bot.py
```
