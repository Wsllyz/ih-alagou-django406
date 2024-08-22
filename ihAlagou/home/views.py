from datetime import datetime, timedelta
from django.shortcuts import render
from django.http import JsonResponse
from home.models import leitura
import requests

# classe de sensores. (implementação futura para múltiplos sensores no sistema)
class Sensor:
    def __init__(self, url, endereco, tamanho):
        self.url: str = url
        self.endereco: str = endereco
        self.tamanho: int = tamanho

#sensor1 = Sensor('https://api.thingspeak.com/channels/2602561/feeds.json?api_key=4OW0Z91BKJ5U61ZT&results=2')

# Função responsável por consumir a api do thingspeak e retornar dinamicamente a distância identificada pelo sensor
def distancia_view(request):
    response = requests.get('https://api.thingspeak.com/channels/2602561/feeds.json?api_key=4OW0Z91BKJ5U61ZT&results=2')
    if response.status_code == 200:
        distancia = abs(int(float(response.json()['feeds'][0]['field2'])) - 300)
        insert_distancia(distancia)
        return JsonResponse({'distancia':distancia})
    return

# Função responsável por renderizar o arquivo index.html inicialmente
def home_view(request):
    return render(request, 'index.html')

# Função responsável por inserir os registros no banco
def insert_distancia(distancia):
    novoRegistro = leitura(distancia=distancia, temperatura=0, statusBateria=100, timestamp=datetime.now().replace(microsecond=0))
    novoRegistro.save()

# Função responsável por pegar as leituras das últimas 12 horas
def select_lista_leituras_view(request):
    listaLeituras = []
    hora = datetime.now()
    for x in range(0, 12):
        distancia = leitura.objects.filter(timestamp__icontains=hora.strftime("%H")).values_list('distancia', flat=True).first()
        if distancia is not None:
            listaLeituras.append(int(distancia))
            hora = hora - timedelta(hours=1)
        else:
            listaLeituras.append(0)
    return JsonResponse({'listaLeituras':listaLeituras})

# Função responsável por excluir todos os registros da tabela leitura (implementação futura de rotina de limpeza)
def limpar_tabela_leitura():
    leitura.objects.all().delete()