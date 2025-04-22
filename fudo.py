from requests import Session, Response
from fudoCreds import url_login, url_users, headers, payload
import json

session = Session()

def do_login(session: Session):
	response = session.post(url_login, data = payload, headers=headers)
	print("Status login:", response.status_code)
	print("Login response headers:", response.headers)
	print("Login response:", response.text)

	if response.status_code == 200:
		print("Login exitoso")
		token = response.json().get("token")
		return token
	else:
		print("Error de login")
		return None

def get_user_info():
	token = do_login(session)
	if token:
		headers_autorization = headers.copy()
		headers_autorization["Authorization"] = f"Bearer {token}"
		r = session.get(url_users, headers = headers_autorization)
		print("Status code:", r.status_code)
		print("Respuesta:", r.text)
		if r.status_code == 200:
			user_data = r.json()
			info_list = []
			for data in user_data.values():
				user_info = {
            		"correo": data.get("email"),
            		"nombre": data.get("name"),
            		"Tel activo": data.get("phone") if data.get("phone") else "No disponible",
            		"Last login": data.get("lastSignInAt"),
            	}

				info_list.append(user_info)
			return info_list
		else:
			print("error al obtener datos")
			return None

user_info = get_user_info()

if user_info:
	with open("user_information.json", "w", encoding="utf-8") as f:
		json.dump(user_info, f, ensure_ascii=False, indent=4)
else:
	print("No se logró obtener datos")