##### Especialização em Arquitetura de Software Distribuído
##### Disicplina: Internet das Coisas (IoT)
##### Trabalho Final: Sistema de monitoramento de temperatura e umidade
##### Professor: Ilo Riveiro
##### Alunos: Pedro Amaral (68072) e Vinícius Amaral (67652)

##### 1. Objetivo
> Desenvolver um sistema para monitoramento da temperatura e umidade de ambientes, oferecendo mecanismos para alertar os responsáveis caso o nível máximo e/ou mínimo permitido de um dos itens monitorados seja ultrapassado.

##### 2. Viabilizadores técnicos
>* **Raspberry Pi 1 B+**: hardware para leitura dos dados;
>* **Protoboard:** placa para montagem de circuitos elétricos experimentais;
>* **Dht22:** sensor de umidade e tempuratura;
>* **Buzzer:** dispositivo para emissão de alertas sonoros;
>* **Led**: dispositivo para emissão de alertas visuais;
>* **Python 2.7**: linguagem de programação interpretada;
>* **Adafruit Python DHT:** biblioteca escrita em Python para leitura dos sensores;
>* **Ionic:** framework para desenvolvimento de aplicações móveis híbidas;
>* **Firebase:** banco de dados NoSQL da Google;
>* **OneSignal**: Ferramenta gratuita para envio de push notification.

##### 3. Resultados alcançados
> Foi criado um programa na linguagem Python, usando a biblioca Adafruit, capaz de ler os dados coletados por um sensor de temperatura e umidade acoplado ao Raspberry Pi onde o programa é executado. A cada leitura, os dados coletados são enviados para um banco de dados NoSQL criado na nuvem por meio de uma requisição HTTP (POST). 

> A periodicidade das medições pode ser determinada pelo usuário por meio de um aplicativo, disponível para a plataforma Android. Nesse aplicativo também é possível que o usuário determine os níveis máximos e/ou mínimos permitidos para cada item monitorado. Caso os níveis sejam ultrapassados, o usuário receberá uma notificação em seu celular informando o ocorrido. Além disso, é possível que o usuário acompanhe em tempo real as medições realizadas.

> Quando os níveis determinados pelo usuário forem atingidos, além da notificação enviada para o celular onde o aplicativo estiver instalado, um alerta sonoro e outro visual também serão emitidos com o objetivo de informar a ocorrência da anormalidade às pessoas que estiverem no ambiente monitorado.

##### 4. Demonstração
>* https://www.youtube.com/

##### 5. Observações para compilar o aplicativo
>* Em www/index.html, trocar <PROJECT_ID>  para o identificador do projeto no Firebase.
>* Em www/js/app.js, trocar <APP_ID> pelo id do aplicativo OneSignal e trocar <GOOGLE_ID> pelo id do aplicativo na Google (conforme instruções do OneSignal).
