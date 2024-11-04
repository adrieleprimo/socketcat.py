# Changelog

Este arquivo tem o propósito de documentar as mudanças que serão realizadas neste projeto e visualizar a evolução no decorrer do tempo.

O formato será baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/).

## [1.2.0] - 2024-10-30
### Adicionado
- A implementação de logs para conexões estabelecidas e recebidas, com a diferenciação de entrada e saída.
- Registro da execução de comandos, para melhor monitoramento das atividades remotas.
- Log para upload de arquivos, além de verificação caso ocorra com sucesso ou erro ao salvar o arquivo.
- Registro das mensagens enviadas e recebidas, com nível `DEBUG`, ou seja, desde eventos de nível `DEBUG`e superiores, como `INFO`, `ẀARNING`, `ERROR` e `CRITICAL`.
- Registro de erros, para obter informações mais precisas e específicas sobre o tipo de erro e respectivamente a sua origem.

### Alterado
- Configurações de logs para que inicialmente sejam definidos a nível `DEBUG` e grave os logs em arquivos diadiários com nome `socketCat_YYYYMMDD.log`. Logo, com o nome do projeto e  respectivamente ano, mês e data.

### Melhorias
- Implementação dos controles de níveis de log ('INFO`, `DEBUG`, `ERROR`, etc) para deixar mais organizado e facilitar quanto a análise das atividades conforme a severidade expressa.

## [1.1.0] - 2024-10-22
### Adicionado 
- Implementação de uma camada de segurança SSL/TLS no `socketCat.py` gerando certificado `cert.pem`e chave privada `key.pem`.
- Instruções no README para realizar a configuração de SSL/TLS com  ferramenta OpenSSL.

### Modificado
- Atribuição do `wrap_socket` com TLS 1.2 na função `clienteSender`para aplicar a camada de segurança.
- Função `serverLoop`com implementação de contexto SSL para obter mais segurança e suporte a certificado e chave privada para autenticar o servidor.


## [v1.0.0] - 2024-10-19
### Adicionado
- Primeira versão do projeto `socketCat.py`, com as funcionalidades básicas cliente-servidor TCP.
- Funções iniciais:
    
    * `clienteSender#>` O objetivo é enviar dados ao servidor.
    * `serverLoop#>` O propósito ouvir as conexões de entrada.
    * `clientHandler#>` Neste caso, a proposta é o upload e execução de comandos.
- Implementação de comandos básicos:
    * Uma conexão TCP, de confiabilidade com execução de comandos remotos.
    * Upload de arquivos.

### Exemplos de comandos
```shell
socketCat.py -t 192.168.0.1 -p 5555 -l -c
socketCat.py -t 192.168.0.1 -p 5555 -l -e="cat /etc/passwd"
```
