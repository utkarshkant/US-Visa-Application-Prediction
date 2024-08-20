# test logging
from us_visa.logger import logging

logging.info("Welcome to our custom log")

# test exception
from us_visa.exception import USVisaException

try:
    a = 2/0
except Exception as e:
    raise USVisaException(e, sys)