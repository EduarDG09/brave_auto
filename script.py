# Script para automatizar Brave Browser --

# imports 
from datetime import datetime
import webbrowser, time, subprocess, random
import pyautogui as pyg

# globals
webs = ["https://2captcha.com/",
"https://forobeta.com/",
"https://raidforums.com/",
"https://www.blackhatworld.com/",
"https://foro-ptc.com/index.php",
"https://www.idle-empire.com/",
"https://eurekasurveys.com/",
"https://surveys.gobranded.com/",
"https://cointiply.com/",
"https://forobeta.com/temas/de-regreso-a-espana-ayuda.867882/page-2",
"https://forobeta.com/temas/me-compre-una-linda-note-n_n.867917/",
"https://forobeta.com/temas/buenas-alguien-que-me-ayude-tengo-este-problema.867918/",
"https://forobeta.com/temas/quien-me-ayuda-a-pagar-el-vip.867909/",
"https://vendercomprardolares.com/calculadora-comisiones-paypal.php",
"https://myprofitland.com/",
"https://www.deepl.com/translator",
"https://es.dll-files.com/",
"https://www.online-stopwatch.com/online-clock-smooth-seconds/full-screen/",
"https://www.monetizados.com/seo",
"https://devcode.la/",
"https://www.infospyware.com/",
"https://smspva.com/",
"https://enlyft.com/tech/products/skype",
"https://arnaldoochoa.gr8.com/lpc_not_found.html",
"https://opinatron.com/",
"https://dinerogeeks.com/como-crear-un-blog-para-ganar-dinero/",
"https://enfoquenomada.com/blog/",
"https://foro20.com/",
"https://www.ganardineroenblog.info/ganar-dinero-con-hitleap/",
]
surfing = False
lastMouseMove = datetime.now()
endSurfing = 20

def abrir_navegador(web): 
    webbrowser.open(web)
    surfing = True

def cerrar_navegador():
    aw = pyg.getActiveWindow()
    while "Brave" not in aw.title:
        aw = pyg.getActiveWindow()
        time.sleep(1)
    with pyg.hold("ctrl"):
        pyg.press("f4")
    return

while True:
    if (surfing == False):
        rand_web = random.choice(webs)
        abrir_navegador(rand_web)
    else:
        now = datetime.now()
        diff = now - lastMouseMove
        if (diff.total_seconds >= 3):
            pyg.moveRel(10, 10, .5)
        elif (diff.total_seconds >= endSurfing):
            cerrar_navegador()
            surfing = False


    cerrar_navegador()
    time.sleep(3)
