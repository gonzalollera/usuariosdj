from django.core.exceptions import ImproperlyConfigured
import json
from unipath import Path

print('--------')
print (Path(__file__))
archivos=Path().listdir

for archivo in archivos:
    print(archivo)
