url_login = "https://auth.fu.do/authenticate" 
url_users = "https://api.fu.do/users?a=-1"

headers = {
	"Accept": "application/json",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
}

payload = {
	"login":"admin@cesarrestaurants",
	"password": "Cesar123.",
	"a": -1
}

