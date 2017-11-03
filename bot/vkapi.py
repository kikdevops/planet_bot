import vk

session = vk.Session()
api = vk.API(session, v=5.0)


def send_message(user_id, token, message, attachment=""):
    api.messages.send(access_token=token, user_id=str(user_id), message=message, attachment=attachment)

def get_user_data(user_id):
	try:
		res = api.users.get(user_ids = str(user_id))
	except Exception as err:
		print(err)
		res = None
	return res
