import logging
import datetime

logging.basicConfig(
    filename=f'socketCat_{datetime.now().strftime('%Y%m%d')}.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
