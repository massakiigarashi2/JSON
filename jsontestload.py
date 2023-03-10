# -*- coding: utf-8 -*-
"""JsonTestLOAD.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10gG7awaXXuQDpfGzNqkI4uVYUhpTAwYP

Para isso, basta acessar o link base "http://transparencia.campinas.sp.gov.br/ws/[método escolhido]/[parâmetros]

https://transparencia.campinas.sp.gov.br/index.php?action=ws&mode=getDespesasTotal

https://www.powercms.in/article/how-get-json-data-remote-url-python-script

DICA JSON!
https://acervolima.com/como-ler-uma-resposta-json-de-um-link-em-python/
"""

# import urllib library
from urllib.request import urlopen
  
# import json
import json
# store the URL in url as 
# parameter for urlopen
url = "https://transparencia.campinas.sp.gov.br/index.php?action=ws&mode=getDespesasTotal"
  
# store the response of URL
response = urlopen(url)
  
# storing the JSON response 
# from url in data
data_json = json.loads(response.read())
  
# print the json response
print(data_json)

