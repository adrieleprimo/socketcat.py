# socketCat.py

<p align="center">
  <img align="center" width="280" src="./icon/socketcat.gif" alt="socketCat Logo"/>
</p>

 ![Python](https://img.shields.io/badge/python-3.9-blue)  ![License](https://img.shields.io/badge/license-MIT-green) 



## Descrição
**socketCat.py** é um singelo projeto construído a partir dos estudos em conjunto com a galera do **Axé Sec**. O pilar deste projeto é compreender o funcionamento dos módulos do Python e como ocorre as conexões entre redes, atuando como cliente ou servidor, com conexões TCP. Além disso, possui outras funcionalidades, como execução remota de comandos, uploado de arquivos, noções de SSL/TLS e uma shell embrionaria que futuramente será mais intuitiva.

## Funcionalidades
- **Modo Servidor**: o socketCat.py aceita conexões dos clientes e a execução de comandos.
- **Upload de Arquivos**: Recebimento e armazenamento de arquivos enviados pelos clientes.
- **Shell de Comando**: Uma shell interativa para comunicação com o servidor.


## Tecnologias 
- ![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python&logoColor=white)
- ![Socket](https://img.shields.io/badge/Socket%20Programming-using%20Python-green)
- ![SSL](https://img.shields.io/badge/SSL-using%20Python-purple)
- ![Threading](https://img.shields.io/badge/Threading-using%20Python-orange)
- ![Getopt](https://img.shields.io/badge/Getopt-using%20Python-yellow)
- ![Subprocess](https://img.shields.io/badge/Subprocess-using%20Python-red)
- ![Sys](https://img.shields.io/badge/Sys-using%20Python-lightgrey)
- ![Bcrypt](https://img.shields.io/badge/Bcrypt-using_Python-blue)
- ![Getpass](https://img.shields.io/badge/Getpass-using_Python-white)
- ![Logging](https://img.shields.io/badge/Logging-using_Python-black)




## Instalação
1. Clone o repositório:
```bash
git clone https://github.com/yourusername/socketCat.git
cd socketCat
```
2. Instalação das dependências necessárias:
```bash
    pip install -r requirements.txt
```

## Configuração do SSL/TLS
Para que você consiga utilizar esse projeto, será necessário gerar uma certificação com o seguinte comando:
```bash
openssl req -new -x509 -keyout key.pem -out cert.pem -days 365 -nodes
```
O comando utilizando o openssl é apenas para gerar uma chave privada e certificado válido, com duração de 1 ano. A ideia é apenas para testar conexões SSL/TSL, para assim entender de maneira bem básica sobre protocolos de seguranças que são usados para criptografar a comunicação entre clientes e servidores pela Internet.

* O key.pem é o arquivo da sua chave privada gerada. O nome pode ser trocado
* o cert.pem é o certificado. O nome pode ser trocado.

Após isso, em **context**, localizado na função **serverLoop** deverá atualizar com o diretório onde foi gerada a certificação e a chave privada:
```python
context.load_cert_chain(certfile='./DIRETORIO-DA-SUA-CERTIFICAÇAO', keyfile='./DIRETORIO-DA-SUA-CHAVE-PRIVADA')
```
* O key.pem é o arquivo da sua chave privada gerada.
* o cert.pem é o certificado.

## Utilização
Para iniciar o servidor e escutar conexões:
```bash
sudo python3 socketCat.py -l -p [port] -c
```

Para conectar-se ao servidor:
```bash
sudo python3 socketCat.py -t [targetHost] -p [port]
```

Para mais opções e ajuda com a ferramenta:
```bash 
sudo python3 socketCat.py -h
```

## Licença
Esse projeto está licenciado sob a [Licença MIT](LICENSE)