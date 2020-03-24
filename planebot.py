import pandas as pd
import numpy as np
import requests

prezzomin=100
destinazione=["Perù","Argentina"]
mese=["Novembre 2020"]

URL = "https://api.skypicker.com/flights"
  
# location given here 
fly_from =	"ROM"
fly_to 	= "STN"
date_from =	"23/04/2021"
date_to =	"28/04/2021"
# defining a params dict for the parameters to be sent to the API 
PARAMS = {'fly_from':fly_from, 'fly_to':fly_to,'date_from':date_from,'date_to':date_to,'partner': "picky"} 
  
# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 
data = r.json() 
print(data)