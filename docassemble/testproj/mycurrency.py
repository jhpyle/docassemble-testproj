from docassemble.base.util import DAEmpty
from docassemble.base.functions import update_language_function, currency_default
from docassemble.base.util import CustomDataType

class SSN(CustomDataType):
    name = 'ssn'
    container_class = 'da-ssn-container'
    input_class = 'da-ssn'

def my_currency(*pargs, **kwargs):
  if isinstance(pargs[0], DAEmpty):
    return ''
  return currency_default(*pargs, **kwargs)

update_language_function('*', 'currency', my_currency)