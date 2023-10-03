import pyttsx3
import speech_recognition as sr
import webbrowser 
import pywhatkit
import yfinance as yf
import pyjokes
import wikipedia
import datetime
import pyaudio


#opciones de voz
    
voz_Fem_mexico= 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
voz_Fem_US= 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
voz_Mac_US= 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'

#Deteccion de voz y devolver el audio como texto
def lisen_voice_transform_text():
    #almacenar el reconocedor en varibale
    r = sr.Recognizer()
    
    #configurar microfono
    with sr.Microphone() as origen:
        #Tiempo de espera en lo que se abre el microfono y empiece a escuchar.
        r.pause_threshold = 0.5
        
        #Informar que comenzo la grabacion (NO ES NECESARIO PARA EL CODIGO PERO NOS SIRVE A LOS DESARROLLADORES PARA TESTEAR)
        print('ya puedes hablar')
        #cuando ya podamos hablar vamos a almacenar el una variable el audio que hayamos creado
        audio = r.listen(origen)        
        
        #Debemos estar dispuests a que hayan errores
        try:
            #buscar en google lo que haya escuchado
            pedido = r.recognize_google(audio, language='es-MX')
            
            #prueba de que pudo ingresar
            print(f'Dijiste: {pedido}')
            
            #Devoveler pedido
            return pedido
        #en caso de que no comprenda el audio
        except sr.UnknownValueError:
            
            #prueba de que no comprendio el audio
            print('Ups, no te entendí')

            return 'Sigo esperando'    
        
        #en caso de no resolver el pedido
        
        except sr.RequestError:
            #prueba de que no comprendio el audio
            print('Ups, no te entendí')

            return 'Sigo esperando'   

        #error inesperado
        except:
            pass
            

#Transformar lo que nosostros le dijismos  nos regrese en voz
def laura_speak_return(mensaje):
    #ensender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', voz_Fem_mexico)
    
    #pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()
       
#informar dia de la semana
def date_today():
    #crear var con fecha de hoy
    today = datetime.date.today()
    print(today)
    
    #dia de la semana 
    week_day = today.weekday()
    print(week_day)
    
    #nombres de los dias
    days_of_week = {0:'Lunes', 
                    1:'Martes', 
                    2:'Miércoles', 
                    3:'Jueves', 
                    4:'Viernes', 
                    5:'Sábado', 
                    6:'Domingo'}
    laura_speak_return(f'Hoy es {days_of_week[week_day]} {today}')
    
    #informar hora
    
#informar hora
def get_hour():
    #variable con datos de hora
    time = datetime.datetime.now()
    if time.hour == 1:
        time = f'Es la {time.hour} con {time.minute} minutos'
    else:
        time = f'Son las {time.hour} con {time.minute} minutos'
    print(time)
    #Decir la hora con voz
    laura_speak_return(time)
    
#saludo inicial
def greeting_initial():
    #Crear hora de dia (mañana, tarde, noche, madrugada)
    date_day = datetime.datetime.now()
    if 5 <= date_day.hour < 12:
        moment = 'Buenos días'
    elif 12 <= date_day.hour < 18:
        moment = 'Buenas tardes'
    else:
        moment = 'Buenas noches'
    #Decir el saludo
    laura_speak_return(f'Hola Luis, {moment} soy Laura tu asistente de voz')                                                                                                                                                                                                                                                                                                                                               
    
#Funcion Central  
def logic_IA():
    #Activar saludo
    greeting_initial()
    #variable de corte
    speak = True
    while speak:                 
        #activar micro y guardar audio
        instruction = lisen_voice_transform_text().lower()
        
        if 'abrir youtube' in instruction or 'abre youtube' in instruction:
            laura_speak_return('Claro, Abriendo Youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in instruction or 'abre navegador' in instruction:
            laura_speak_return('Por supuesto, abriendo Navegador')
            webbrowser.open('www.google.com')
            continue
        elif 'abrir twitch' in instruction or 'abre twitch' in instruction:
            laura_speak_return('Enseguida, Abriendo Twitch')
            webbrowser.open('https://www.twitch.tv')
            continue
        elif 'abrir facebook' in instruction or 'abre facebook' in instruction:
            laura_speak_return('Enseguida, Abriendo Facebook')
            webbrowser.open('https://www.facebook.com/')
            continue
        elif 'abrir paypal' in instruction or 'abre paypal' in instruction:
            laura_speak_return('Enseguida, Abriendo Paypal')
            webbrowser.open('https://www.paypal.com/')
            continue
        elif 'abrir udemy' in instruction or 'abre udemy' in instruction:
            laura_speak_return('Enseguida, Abriendo Udemy')
            webbrowser.open('https://www.udemy.com/')
            continue
        elif 'abrir platzi' in instruction or 'abre platzi' in instruction:
            laura_speak_return('Enseguida, Abriendo Platzi')
            webbrowser.open('https://platzi.com/')
            continue
        elif 'abrir chat-gpt' in instruction or 'abre chat-gpt' in instruction:
            laura_speak_return('Enseguida, Abriendo Chat-GPT')
            webbrowser.open('https://chat.openai.com')
            continue
        elif 'abrir crunchyroll' in instruction or 'abre Ccrunchyroll' in instruction:
            laura_speak_return('Enseguida, Abriendo Crunchyroll')
            webbrowser.open('https://www.crunchyroll.com/')
            continue
        elif 'abrir xbox' in instruction or 'abre Xbox' in instruction or 'página de xbox' in instruction:
            laura_speak_return('Enseguida, Abriendo Xbox')
            webbrowser.open('https://www.xbox.com/')
            continue
        elif 'abrir amazon' in instruction or 'abre amazon' in instruction:
            laura_speak_return('Enseguida, Abriendo Amazon')
            webbrowser.open('https://www.amazon.com.mx/')
            continue
        elif 'abrir mercadolibre' in instruction or 'abre mercadolibre' in instruction:
            laura_speak_return('Enseguida, Abriendo Mercado Libre')
            webbrowser.open('https://www.mercadolibre.com.mx/')
            continue
        elif 'abrir mercado pago' in instruction or 'abre mercado pago' in instruction:
            laura_speak_return('Enseguida, Abriendo Mercado Pago')
            webbrowser.open('https://www.mercadopago.com.mx/home?code=0iRDwFtkbA8fo1bOv0tv9atLmmDQhc7i&rtk=eyJraWQiOiIxIiwiYWxnIjoiUlMyNTYiLCJ0eXAiOiJKV1QifQ.eyJqdGkiOiJlNjIxODA5MC1kNzNlLTRiNDktOWU3Mi04YTJmM2M1MTJjMGUiLCJkZXRhY2hlZF9pZCI6Ijk5ZWU0NWI1LWQ4MWEtNDI5MS04MTQxLTUxZTNmZDdjOTRmOSIsInNpdGVfaWQiOiJNTE0iLCJjb21wbGV0ZWRfY2hhbGxlbmdlcyI6WyJFTlRFUl9QQVNTV09SRCJdLCJzdWIiOiI0NTQ1MjA3NzciLCJhdWQiOiJtcC1ob21lIiwiaXNzIjoicmVhdXRoZW50aWNhdGlvbiIsImlhdCI6MTY5MTUzMDYxMiwiZXhwIjoxNjkxNTMwOTEyLCJtYXhfdXNhZ2UiOjN9.HLhTo2ECurTAbzCx_huX7C6I3kE1MxHV6YZ5gnzrxamz3NZeVzESsSsvT0Ch-RgvoVsucgP5OwN6ODMRtdByzvGanE1v9a5jpr7vVW0IEfamf5WTc3xG7un-0ENSeDKM8xo2Omqf0S2mUqvQ48Ap5PcWF_N3tMgfZHli2r29WpMILZi_svU7flI4VV-AfA38YaXXKsuCBGtaZ_EvYCG5vS8GV_B7KUITVVeFpRUkkSJC2-VnKGHLCHinXbDb3Q3TOAo1FUMIVcun5Lggd6NLNR3L3MCLk3KyQ3zj4WTB5jn_SvVOzmRxZorQj-AxxTNyY0lzcFQi_f354AA3tR6-AA')
            continue
        elif 'abrir indeed' in instruction or 'abre indeed' in instruction:
            laura_speak_return('Enseguida, Abriendo indeed')
            webbrowser.open('https://mx.indeed.com')
            continue
        elif 'abrir computrabajo' in instruction or 'abre computrabajo' in instruction:
            laura_speak_return('Enseguida, Abriendo Computrabajo')
            webbrowser.open('https://mx.computrabajo.com')
            continue
        elif 'abrir cex' in instruction or 'abre cex' in instruction:
            laura_speak_return('Enseguida, Abriendo Cex')
            webbrowser.open('https://mx.webuy.com')
            continue
        elif 'abrir gameplanet' in instruction or 'abre gameplanet' in instruction:
            laura_speak_return('Enseguida, Abriendo Gameplanet')
            webbrowser.open('https://gameplanet.com')
            continue
        elif 'qué día es hoy' in instruction or 'fecha de hoy' in instruction or 'hoy qué día es' in instruction or 'dime la fecha' in instruction:
            date_today()
            continue
        elif 'qué hora es' in instruction or 'qué horas son' in instruction or 'dime la hora' in instruction or 'la hora' in instruction or 'dame la hora' in instruction:
            get_hour()
            continue
        elif 'buscar en wikipedia' in instruction or 'busca en wikipedia' in instruction:
            if 'buscar en wikipedia' in instruction:
                instruction = instruction.replace('buscar en wikipedia', '')
            elif 'busca en wikipedia' in instruction:
                instruction = instruction.replace('busca en wikipedia', '')
            else:
                laura_speak_return('Lo siento no pude entenderte')
            laura_speak_return('Buscando en Wikipedia')
            wikipedia.set_lang('es')
            result = wikipedia.summary(instruction, sentences = 1)
            laura_speak_return(f'Segun wikipedia')
            laura_speak_return(result)
            continue
        elif 'qué es'.lower() in instruction or 'quién es' in instruction:
            if 'qué es la'.lower() in instruction:
                instruction = instruction.replace('qué es la', '')
            elif 'qué es el'.lower() in instruction:
                instruction = instruction.replace('qué es el', '')
            elif 'qué es'.lower() in instruction:
                instruction = instruction.replace('qué es ', '')
            elif 'quién es'.lower() in instruction:
                instruction = instruction.replace('quién es', '')  
            pywhatkit.search(instruction)
            laura_speak_return(f'Buscando {instruction} en OperaGX')
            continue
        elif 'reproducir' in instruction or 'reproduce' in instruction:
            if 'reproducir' in instruction:
                instruction = instruction.replace('reproducir', '')
            elif 'reproduce' in instruction:
                instruction = instruction.replace('reproduce', '')
            laura_speak_return(f'Reproduciendo {instruction} en Youtube')
            pywhatkit.playonyt(instruction)
            continue
        elif 'broma' in instruction or 'chiste' in instruction:
            laura_speak_return(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in instruction or 'precio de la acción' in instruction:
            wallet = {'apple': 'AAPL', 'amazon': 'AMZN', 'google': 'GOOGL', 'sp-500': 'SP5C N', 'tesla': 'TSLA', 'microsoft':'MSFT',    
                      'Apple': 'AAPL', 'Amazon': 'AMZN', 'Google': 'GOOGL', 'Sp-500': 'SP5C N', 'Tesla': 'TSLA', 'Microsoft':'MSFT'}
            if 'precio de las acciones' in instruction:
                instruction = instruction.replace('precio de la acciones de', '')
            elif 'precio de la acción' in instruction:
                instruction = instruction.replace('precio de las acciones de', '')
            try:
                action_search= wallet[instruction.lower()]
                action_search = yf.Ticker(action_search)
                price_act = action_search.info['regularMarketPrice']
                laura_speak_return(f'El pecio actual de {instruction} es de {price_act}')
            except:
                laura_speak_return('intenta de nuevo')
                continue
        elif 'muchas gracias, Laura'.lower() in instruction:
            laura_speak_return('De nada, estoy para cualquier cosa que me necesites')
            break                            

logic_IA()                          
