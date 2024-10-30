import logging
from datetime import datetime

logging.basicConfig(
    filename=f'socketCat_{datetime.now().strftime("%Y%m%d")}.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def logConnection(clientAddress, port, direction='inbound'):
    if direction == 'inbound':
        logging.info(f'Connection received from {clientAddress}:{port}')
    else:
        logging.info(f'Connection established to {clientAddress}:{port}')

def logCommandExecution(command):
    logging.info(f'Command executed {command}')  

def logFileUpload(destination, status):
    if status:
        logging.info(f'File upload successfully saved in {destination}')
    else:
        logging.error(f'Failed to save the file: {destination}')

def logMessageSent(message):
    logging.debug(f'Message sent: {message}')

def logMessageReceived(message):
    logging.debug(f'Message received: {message}')

def logError(errorMessage):
    logging.error(f'Error: {errorMessage}')