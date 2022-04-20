from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager

URL = "https://www.kartago.sk/"
URL_poznavacky = URL+"poznavaci-zajezdy"
URL_poznavacky_vikendy = URL+"poznavaci-zajezdy#vikendy"
URL_poznavacky_rodiny = URL+"poznavaci-zajezdy#rodiny"
URL_poznavacky_zazitky = URL+"poznavaci-zajezdy#rodiny"
URL_pobocky = URL+"kontakty/nase-predajne"
URL_kluby = URL+"uzitocne-informacie/mango-club"
#URL_detail = URL+"spanielsko/costa-almeria/roquetas-de-mar/ar-almerimar?KEY=2207812211&DS=32768&GIATA=0&D=63350|211764&HID=142164&MT=2&RT=15&NN=7&RD=2022-08-01&DD=2022-07-25&DP=483&TO=483|1837|2933|3437&MNN=7&TT=1&PID=359709&DPR=KARTAGO-SK&TTM=1&DF=2022-07-25|2022-08-25&ERM=0&NNM=7|8|9|10|11|12|13&ac1=2&kc1=1&ka1=6&ic1=0#/prehled"
URL_detail = URL+"grecko/rhodos/afanadou/afandou-beach?KEY=2192069476&DS=32768&GIATA=7139&D=63316|63319|63324|63402|63471&HID=3813&MT=5&RT=15&NN=7&RD=2022-09-09&DD=2022-09-02&DP=1837&TO=1837&MNN=7&TT=1&PID=2821&DPR=KARTAGO-SK&TTM=1&DF=2022-09-01|2022-09-18&ERM=0&NNM=7|8|9|10|11|12|13&ac1=2&kc1=1&ka1=6&ic1=0#/prehled"
URL_SRL = URL + "vysledky-vyhladavania?d=63316|63319|63324|63402|63471&tt=1&to=483|1837|2933|3437&dd=2022-08-06&rd=2022-09-23&nn=7|8|9|10|11|12|13&ka1=6&kc1=1&ac1=2"
#URL_SRL = URL + "vysledky-vyhladavania?d=63350|211764&tt=1&to=483|1837|2933|3437&dd=2022-07-01&rd=2022-08-31&nn=7|8|9|10|11|12|13&ka1=6&kc1=1&ac1=2"
URL_covidInfo = URL+"covid-info"
URL_FM = URL+"first-minute"
URL_faq = URL+"faq"
URL_lm = URL+"last-minute"
URL_stat = URL+"grecko"
URL_groupsearch = URL+"vysledky-vyhladavania?tt=1&to=483|1837|2933|3437&dd=2022-09-01&rd=2022-09-25&nn=7|8|9|10|11|12|13&ka1=6&kc1=1&ac1=2"
URL_FT_results = URL+"hledani-vysledky?q="
import time
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import smtplib, ssl
from email.mime.text import MIMEText
from to_import_secret import emailPass
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



def setUp(self):
  self.driver = webdriver.Chrome(ChromeDriverManager().install())
  generalDriverWaitImplicit(self.driver)
  #self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
  #self.driver = webdriver.Opera(executable_path=OperaDriverManager().install())
  #self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

def tearDown(self):
  self.driver.quit()

def sendEmail(msg):
  fromx = 'alertserverproblem@gmail.com'
  to = 'ooo.kadoun@gmail.com'
  msg = MIMEText(msg)
  msg['Subject'] = "SRWEB1"
  msg['From'] = fromx
  msg['To'] = to

  server = smtplib.SMTP('smtp.gmail.com:587')
  server.starttls()
  server.ehlo()
  server.login("alertserverproblem@gmail.com", emailPass)
  server.sendmail(fromx, to, msg.as_string())
  server.quit()

def generalDriverWaitImplicit(driver):
  driver.implicitly_wait(25)
def acceptConsent(driver):

  generalDriverWaitImplicit(driver)
  time.sleep(3)
  try:
    generalDriverWaitImplicit(driver)
    element = driver.execute_script(
      """return document.querySelector('#usercentrics-root').shadowRoot.querySelector("button[data-testid='uc-accept-all-button']")""")
    print(element)
  except NoSuchElementException:
    print("NOSUCH")
  except TimeoutException:
    pass

  if element != None:
    element.click()

  else:
    print("consent pass")
    pass


def acceptConsent5(driver):
  time.sleep(2)
  try:
    element = driver.execute_script(
      """return document.querySelector('#usercentrics-root').shadowRoot.querySelector("button[data-testid='uc-accept-all-button']")""")
  except NoSuchElementException:
    return

  except TimeoutException:
    pass
  try:
    element.click()
  except TimeoutException:
    pass
  except NoSuchElementException:
    return

def closeExponeaBanner(driver):
    time.sleep(1.5)
    wait = WebDriverWait(driver, 150000)
    driver.maximize_window()
    try:
      exponeaBanner = driver.find_element_by_xpath("//*[@class='exponea-popup-banner']")
      if exponeaBanner.is_displayed():
        wait.until(EC.visibility_of(exponeaBanner))
        exponeaCrossAndBanner = driver.find_element_by_xpath(
          "//*[@class='exponea-popup-banner']//*[@class='exponea-close']")
        exponeaCrossAndBanner.click()
        time.sleep(2)

    except NoSuchElementException:
      print("nenasle se exponea banner")

def acceptConsent3(driver):
  time.sleep(2)

  element = driver.execute_script(
      """return document.querySelector('#usercentrics-root').shadowRoot.querySelector("button[data-testid='uc-accept-all-button']")""")
  if element !=0:

      pass

  else:
      element.click()


desired_cap = {
"os" : "Windows",
"os_version" : "11",
"browser" : "Edge",
"browser_version" : "latest",
"browserstack.local" : "false",
"browserstack.selenium_version" : "3.5.2"
}