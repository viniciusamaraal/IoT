# Carrega as bibliotecas
import Adafruit_DHT
import RPi.GPIO as GPIO
import json
import requests
import time
import datetime
from decimal import *

def definirAlarme(umidDec, tempDec):
   tempExcedida = temp >= Decimal(config["valorAlertaTemperaturaMaxima"]) or temp <= Decimal(config["valorAlertaTemperaturaMinima"])
   umidExcedida = umid >= Decimal(config["valorAlertaUmidadeMaxima"]) or umid <= Decimal(config["valorAlertaUmidadeMinima"])

   if tempExcedida or umidExcedida:
     GPIO.output(pino_sensor_buzzer, GPIO.HIGH)
     GPIO.output(pino_sensor_led, GPIO.HIGH)
   else:
     GPIO.output(pino_sensor_buzzer, GPIO.LOW) 
     GPIO.output(pino_sensor_led, GPIO.LOW)

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
     print ("Codigo de retorno = {0:0.1f}").format(response.status_code)

     config = requests.get('https://projetoiotpuc.firebaseio.com/config.json').json()
     
     definirAlarme(Decimal(temp), Decimal(umid))

     #GPIO.output(18, GPIO.LOW)
     print ("Aguarde {0:0.1f} segundos para efetuar nova leitura...\n").format(config["intervaloMonitoramento"])
     time.sleep(config["intervaloMonitoramento"])
   else:
     # Mensagem de erro de comunicacao com o sensor
     print("Falha ao ler dados do DHT11 !!!")
