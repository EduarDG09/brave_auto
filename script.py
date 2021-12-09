# Script para automatizar Brave Browser --

# imports 
from datetime import datetime
import webbrowser, time, logging, random
import pyautogui as pyg

# globals
logging.basicConfig(filename="log.txt", filemode="a", format="%(asctime)s,%(msecs)d %(levelname)s %(message)s") 
webs = ["https://2captcha.com/",
"https://forobeta.com/",
"https://raidforums.com/",
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
firstTime = True
lastMouseMove = datetime.now()
lastSurf = datetime.now()
startedSurfing = datetime.now()
stopAt = random.choice([(2*60*60), (60*60), (3*60*60)])
pagTime = random.choice([(20*60), (15*60), (30*60)])

def openBrowser(web): 
    logging.info("Navegando " + web + "...")
    webbrowser.open(web)

def closeBrowser():
    keepGoing = True
    aw = pyg.getActiveWindow()
    while keepGoing:
        if hasattr(aw, "title"):
            if "Brave" not in aw.title:
                aw = pyg.getActiveWindow()
                time.sleep(15)
                continue
            keepGoing = False
            break
    with pyg.hold("ctrl"):
        pyg.press("f4")
    return

def closePrevTab():
    keepGoing = True
    time.sleep(1)
    aw = pyg.getActiveWindow()
    while keepGoing:
        if hasattr(aw, "title"):
            if "Brave" not in aw.title:
                aw = pyg.getActiveWindow()
                time.sleep(15)
                continue
            keepGoing = False
            break
    with pyg.hold("ctrl"):
        pyg.press("1")
        time.sleep(.5)
        pyg.press("w")

logging.info("Inicia el bot!")
while True:
    if (surfing == False):
        rand_web = random.choice(webs)
        surfing = True
        openBrowser(rand_web)
        if (firstTime == True):
            firstTime = False
            continue
        closePrevTab()
    else:
        aw = pyg.getActiveWindow()
        keepGoing = True
        while keepGoing:
            if hasattr(aw, "title"):
                if "Brave" not in aw.title:
                    aw = pyg.getActiveWindow()
                    time.sleep(15)
                    continue
                keepGoing = False
                break
        
        now = datetime.now()
        if (random.randint(1, 10) == 3):
            pyg.scroll(-100)
        if ((now - lastMouseMove).total_seconds() >= random.choice([10, 30, 45, 5])):
            width, height = pyg.size()
            pyg.moveTo(random.randrange(0, width), random.randrange(80, height-80), .75)
            lastMouseMove = datetime.now()
        if ((now - lastSurf).total_seconds() >= pagTime):
            logging.info("Tiempo gastado en la página: " + str(pagTime) + " segundos.")
            pagTime = random.choice([(20*60), (15*60), (30*60)])
            lastSurf = datetime.now()
            surfing = False
        if ((now - startedSurfing).total_seconds() >= stopAt):
            openBrowser("https://google.com")
            closePrevTab()
            sleepFor = random.choice([(5*60*60), (8*60*60), (12*60*60)])
            logging.info("Descansando por: " + str(sleepFor/3600) + " horas.")
            time.sleep(sleepFor)
            surfing = False
            startedSurfing = datetime.now()
            lastSurf = datetime.now()
            stopAt = random.choice([(2*60*60), (60*60), (3*60*60)])
            continue
        

