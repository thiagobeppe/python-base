#!/usr/bin/env python
import logging

#Instancia customizada de log
log = logging.Logger("loggin.py", logging.DEBUG)

#level - https://docs.python.org/3/library/logging.html#logging-levels
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# Formating

fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
#Destino
log.addHandler(ch)

log.debug("testing_debug")
log.info("testing_info")
log.critical("testing_critical")
log.warning("testing_warning")
log.error("testing_error")
