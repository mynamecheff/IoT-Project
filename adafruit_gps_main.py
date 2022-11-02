import gps_funktion
import umqtt_robust2 as mqtt
from machine import Pin
from time import sleep
import neopixel
from time import sleep 
# Her kan i placere globale varibaler, og instanser af klasser
#np = neopixel.NeoPixel(Pin(21), 12)
i = 0
gps1 = 0
def gps_main():
    try:
        # Denne variabel vil have GPS data når den har fået kontakt til sattellitterne ellers vil den være None
        gps_data = gps_funktion.gps_to_adafruit
        print(f"\ngps_data er: {gps_data}")
        
        #For at sende beskeder til andre feeds kan det gøres sådan:
        #Indsæt eget username og feednavn til så det svarer til dit eget username og feed du har oprettet
        #mqtt.web_print(gps_data, 'DIT_ADAFRUIT_USERNAME/feeds/DIT_FEED')
        
        #For at vise lokationsdata på adafruit dashboard skal det sendes til feed med /csv til sidst
        #For at sende til GPS lokationsdata til et feed kaldet mapfeed kan det gøres således:
        #mqtt.web_print(gps_data, 'DIT_ADAFRUIT_USERNAME/feeds/mapfeed/csv')        
        sleep(4) # vent mere end 3 sekunder mellem hver besked der sendes til adafruit
        
        if gps_data == gps1:
            print("please move or something")
           # np.fill(40,200,100)
            #np.write()
        else:
            sleep(1)
          #  np.fill((255,255,100))
           # np.write()
            mqtt.web_print(gps_data,'NamesJeff/feeds/mapfeed/csv') # Hvis der ikke angives et 2. argument vil default feed være det fra credentials filen      
             
        sleep(4)  # vent mere end 3 sekunder mellem hver besked der sendes til adafruit
        
        gps1 = gps_data
        if len(mqtt.besked) != 0: # Her nulstilles indkommende beskeder
            mqtt.besked = ""            
        mqtt.sync_with_adafruitIO() # igangsæt at sende og modtage data med Adafruit IO             
        print(".", end = '') # printer et punktum til shell, uden et enter        
    # Stopper programmet når der trykkes Ctrl + c
    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        mqtt.c.disconnect()
        mqtt.sys.exit()

 
 
