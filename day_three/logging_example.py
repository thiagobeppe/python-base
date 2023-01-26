#!/usr/bin/env python
import logging
from logging import handlers
#Instancia customizada de log
log = logging.Logger("loggin.py", logging.DEBUG)

#level - https://docs.python.org/3/library/logging.html#logging-levels
# ch = logging.StreamHandler() -> Console
fh = handlers.RotatingFileHandler(
    "meu_log_personalizado.log",
    maxBytes=10**6,
    backupCount=10)

fh.setLevel(logging.DEBUG)

# Formating

fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
fh.setFormatter(fmt)
#Destino
log.addHandler(fh)

log.debug("testing_debug")
log.info("testing_info")
log.critical("testing_critical")
log.warning("testing_warning")
log.error("testing_error")
