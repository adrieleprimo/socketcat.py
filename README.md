# socketCat.py

<p align="center">
  <img align="center" width="280" src="./socketcat.gif" alt="socketCat Logo"/>
</p>

---

## Descrição

**socketCat.py** é um singelo projeto construído a partir dos estudos em conjunto com a galera do **Axé Sec**. O pilar deste projeto é compreender o funcionamento dos módulos do Python e como ocorre as conexões entre redes, atuando como cliente ou servidor, com conexões TCP. Além disso, possui outras funcionalidades, como execução remota de comandos, uploado de arquivos, noções de SSL/TLS e uma shell embrionaria que futuramente será mais intuitiva.

### Funcionalidades

- **Modo Servidor**: o socketCat.py aceita conexões dos clientes e a execução de comandos.
- **Upload de Arquivos**: Recebimento e armazenamento de arquivos enviados pelos clientes.
- **Shell de Comando**: Uma shell interativa para comunicação com o servidor.
---

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/yourusername/socketCat.git
   cd socketCat
2. Instalação das dependências necessárias:
```bash
    pip install -r requirements.txt
```
---
### Utilização
Para iniciar o servidor e escutar conexões:
```bash
sudo python3 ./src/socketCat.py -l -p [port] -c
```

Para conectar-se ao servidor:
```bash
sudo python3 ./src/socketCat.py -t [targetHost] -p [port]
```

Para mais opções e ajuda com a ferramenta:
```bash
```bash 
sudo python3 socketCat.py -h
```

## Licença
Esse projeto está licenciado sob a [Licença MIT](LICENSE)