import os
from src import main

try:os.mkdir("Hasil/CP")
except:pass
try:os.mkdir("Hasil/OK")
except:pass

if __name__=="__main__":
	main.CheckLicenseKey(
		).Check(
	)