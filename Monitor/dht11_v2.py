# Carrega as bibliotecas
import Adafruit_DHT
import RPi.GPIO as GPIO
import json
import requests
import time
import datetime
from decimal import *

# Funcao responsavel por acionar o buzzer e o led caso os limites tenham sido ultrapassados
def definirAlarme(tempDec, umidDec):
   tempExcedida = temp >= Decimal(config["valorAlertaTemperaturaMaxima"]) or temp <= Decimal(config["valorAlertaTemperaturaMinima"])
   umidExcedida = umid >= Decimal(config["valorAlertaUmidadeMaxima"]) or umid <= Decimal(config["valorAlertaUmidadeMinima"])

   if tempExcedida or umidExcedida:
     GPIO.output(pino_sensor_buzzer, GPIO.HIGH)
     GPIO.output(pino_sensor_led, GPIO.HIGH)

     enviarNotificacao(tempExcedida, tempDec, umidExcedida, umidDec)
   else:
     GPIO.output(pino_sensor_buzzer, GPIO.LOW) 
     GPIO.output(pino_sensor_led, GPIO.LOW)

# Funcao responsavel por chamar o servico que envia a notificacao para os dispositivos com o aplicativo instalado
def enviarNotificacao(tempExcedida, tempDec, umidExcedida, umidDec):
   dados = {}
   dados["app_id"] = "11bfdd01-0741-4a4a-a105-3f2d3bfb79ad"
   dados["included_segments"] = ["All"]

   cabecalho = {}
   cabecalho["Content-Type"] = "application/json"
   cabecalho["Authorization"] = "Basic MTIwNGY4ZmUtZWU3OC00OTZmLTgzZTgtNGRhYmEwMWJkNjNk"

   if tempExcedida:
     mensagem = ("A temperatura ultrapassou o limite definido. Valor atual: {0:0.1f} C").format(tempDec)
     dados["contents"] = { "en": mensagem }

   if umidExcedida: 
     mensagem = ("A umidade ultrapassou o limite definido. Valor atual: {0:0.1f}%").format(umidDec)
     dados["contents"] = { "en": mensagem }

   response = requests.post('https://onesignal.com/api/v1/notifications', headers = cabecalho, json = dados)
   print ("Status de envio da notificacao: {0:0.1f}").format(response.status_code)


# Define o tipo de sensor
sensor = Adafruit_DHT.DHT22
 
GPIO.setmode(GPIO.BOARD)

# Define a GPIO conectada ao pino de dados do sensor
pino_sensor_buzzer = 18
pino_sensor_led = 22
pino_sensor_temp_umid = 23

GPIO.setwarnings(False)

GPIO.setup(pino_sensor_buzzer, GPIO.OUT) # porta de saida do buzzer
GPIO.setup(pino_sensor_led, GPIO.OUT) # porta de saida do led
 
# Informacoes iniciais
print ("*** Lendo os valores de temperatura e umidade \n");


while(1):
   # Efetua a leitura do sensor
   umid, temp = Adafruit_DHT.read_retry(sensor, pino_sensor_temp_umid);
   # Caso leitura esteja ok, mostra os valores na tela
   if umid is not None and temp is not None:
     dados = {}
     dados["umidade"] = umid
     dados["temperatura"] = temp
     dados["data"] = str(datetime.datetime.now()).split()[0]
     dados["hora"] = str(datetime.datetime.now()).split()[1].split('.')[0]

     response = requests.post('https://projetoiotpuc.firebaseio.com/temperaturas.json', json = dados)
     
     print ("Temperatura = {0:0.1f}  Umidade = {1:0.1f}").format(temp, umid)
     print ("Status de envio dos dados coletados: {0:0.1f}").format(response.status_code)

     config = requests.get('https://projetoiotpuc.firebaseio.com/config.json').json()
     
     definirAlarme(Decimal(temp), Decimal(umid))

     #GPIO.output(18, GPIO.LOW)
     print ("Aguarde {0} segundos para efetuar nova leitura...\n").format(config["intervaloMonitoramento"])
     time.sleep(float(config["intervaloMonitoramento"]))
   else:
     # Mensagem de erro de comunicacao com o sensor
     print("Falha ao ler dados do DHT11 !!!")
