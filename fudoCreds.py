url_login = "https://auth.fu.do/authenticate" 
url_users = "https://api.fu.do/users?a=-1"

headers = {
	"Accept": "application/json",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "token":"eyJhbGciOiJIUzI1NiJ9.eyJ1aSI6MSwidWEiOnRydWUsInVyIjoxLCJ1bCI6ImFkbWluQGNlc2FycmVzdGF1cmFudHMiLCJhaSI6Mjc3NDAxLCJzaWMiOjExLCJjaSI6IjQiLCJleHAiOjE3NDU0NTIwNjN9.Y6HdlosJ_PY6a1Vpp-kqotyZguv4QrjqUctOhVSDgCo"
}

payload = {
	"login":"admin@cesarrestaurants",
	"password": "Cesar123.",
	"a": -1
}

