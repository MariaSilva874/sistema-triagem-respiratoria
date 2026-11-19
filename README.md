# Sistema Especialista para Triagem Inicial de Sintomas Respiratórios

Protótipo acadêmico desenvolvido em Python e Streamlit. O sistema recebe respostas sobre sintomas, verifica sinais de alerta e aplica regras IF–THEN para apresentar possíveis padrões de associação.

## Aviso importante
Este projeto é exclusivamente um protótipo acadêmico. Não diagnostica, não prescreve tratamento e não substitui avaliação profissional. As regras são ilustrativas e precisam ser revisadas e validadas por profissional de saúde e pelo orientador antes de qualquer uso fora de testes acadêmicos. Não use o resultado para decidir se deve ou não procurar atendimento.

## Arquivos
- `app.py`: interface e formulário.
- `regras.py`: base de conhecimento e motor de inferência.
- `testes.py`: testes automatizados simples.
- `requirements.txt`: dependências.

## Como executar no macOS usando o VS Code

### 1. Instalar o necessário
1. Instale o Python 3, se ainda não tiver: https://www.python.org/downloads/macos/
2. Instale o Visual Studio Code: https://code.visualstudio.com/
3. Abra o VS Code e instale a extensão **Python**, da Microsoft.

### 2. Abrir o projeto
1. Descompacte o arquivo ZIP.
2. No VS Code, vá em **File > Open Folder...**.
3. Selecione a pasta `sistema_triagem_respiratoria`.

### 3. Abrir o terminal integrado
No VS Code, escolha **Terminal > New Terminal**. O terminal normalmente abrirá na pasta do projeto.

### 4. Criar um ambiente virtual
No terminal, execute:

```bash
python3 -m venv .venv
```

Ative o ambiente virtual:

```bash
source .venv/bin/activate
```

Quando estiver ativo, normalmente aparecerá `(.venv)` no início da linha do terminal.

### 5. Instalar o Streamlit
Execute:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 6. Executar o sistema
Execute:

```bash
python -m streamlit run app.py
```

O Streamlit deverá abrir o sistema no navegador. Se não abrir automaticamente, copie o endereço local exibido no terminal (normalmente `http://localhost:8501`) e cole no navegador.

### 7. Encerrar
Para parar o sistema, volte ao terminal do VS Code e pressione:

```text
Control + C
```

### 8. Executar os testes
Com o ambiente virtual ativado, execute:

```bash
python -m unittest testes.py
```

Se os testes passarem, o terminal mostrará `OK`.

## Se o comando `python3` não funcionar
Confira a instalação com:

```bash
python3 --version
```

Se o comando não for reconhecido, instale o Python para macOS pelo site oficial indicado acima e reinicie o VS Code.

## Observações de desenvolvimento
- O formulário foi limitado a adultos (18 anos ou mais), conforme o escopo inicial proposto.
- A saturação pode ser informada, mas não é interpretada pelo motor de regras nesta versão.
- O texto livre é exibido apenas como campo de observação e não é processado.
- Nenhum dado é salvo em banco de dados.
- As regras de alerta e as associações são exemplos para demonstrar a arquitetura. Os critérios clínicos, termos e encaminhamentos precisam de validação profissional.
