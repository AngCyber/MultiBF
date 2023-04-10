import os
from src import menu

try:
	os.mkdir("Hasil/CP")
except:pass
try:
	os.mkdir("Hasil/OK")
except:pass
try:
	os.system("pip install fake_useragent")
except:pass
menu.CheckLicenseKey().Check()