HELP

git clone https://github.com/kikdevops/planet_bot.git; cp -r planet_bot/app/* mysite/

Run app with 
../flask/bin/python3.4 flask_app.py

curl -H "Content-Type: application/json" -X POST -d '{"type":"message_new","object":{"id":43, "date":1492522323, "out":0, "user_id":"your id", "read_state":0, "title":" ... ", "body":"помощь"}, "group_id":"group id"}' http://127.0.0.1:5000/

#hello
curl -H "Content-Type: application/json" -X POST -d '{"type": "group_join", "object": {"user_id": your id, "join_type" : "approved"}, "group_id": group id}' http://127.0.0.1:5000/
