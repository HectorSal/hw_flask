from flask import Flask

name = "Lisa"
city_names = ["Paris", "London", "Rome", "Tahiti"]


myapp_obj = Flask(__name__)

@myapp_obj.route("/")
def home():
    string = '''
	<html>
	<head>
		 <title>Home Page - my blog</title>
	</head>
	<body>
		<h1>Welcome ''' + name + '''!</h1>
		<a href="https://www.google.com/">not google</a>
		<ul>
			'''
    list= ""
    for i in range(len(city_names)):
        list = list + "<li>" + city_names[i] + "</li>"
    return string + list + '''</ul>
	</body>
	</html>'''
myapp_obj.run()
