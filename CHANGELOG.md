# Changelog

Este arquivo tem o propósito de documentar às mudanças que serão realizadas neste projeto e visualizar a evolução no decorrer do tempo.

O formato será baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/)

---

## [v1.0.0] - 2024-09-19
### Adicionado
- Primeira versão do projeto `sokcetCat.py`, com as funcionalidades básicas cliente-servidor TCP.
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
