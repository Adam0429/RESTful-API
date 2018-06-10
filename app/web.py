from flask import Flask,abort,request,redirect,render_template,jsonify
import json
import pymysql


app = Flask('my web')
app.config['SECRET_KEY'] = '1234231'
db = pymysql.connect("localhost","root","970429","test",charset="utf8mb4")

# def get_blogs():
# 	cursor = db.cursor()
# 	cursor.execute('select * from blog')
# 	result = cursor.fetchall()
# 	return jsonify(result)

@app.route('/todo/api/v1.0/search/blogs/', methods=['GET','POST'])
def get_blogs():
	cursor = db.cursor()
	cursor.execute('select * from blog')
	result = cursor.fetchall()
	return jsonify(result)

@app.route('/todo/api/v1.0/search/blog/<name>', methods=['GET','POST'])
def get_blog(name):
     cursor = db.cursor()
     cursor.execute('select * from blog where title ="'+name+'"')
     result = cursor.fetchall()
     return jsonify(result)

@app.route('/todo/api/v1.0/add/blog/<name>', methods=['GET','POST'])
def add_blog(name):
	cursor = db.cursor()
	cursor.execute("insert into blog values('"+name+"')")
	db.commit()
	return 'add success'

class Service(object):
	_instance = None
	def __new__(cls, *args, **kw):
		if not cls._instance:
			cls._instance = super(Service, cls).__new__(cls, *args, **kw)
			return cls._instance

	def __init__(self):
		pass

	def get_blogs(self):
		cursor = db.cursor()
		cursor.execute('select * from blog')
		result = cursor.fetchall()
		return json.dumps(result)

	def get_blog(self,name):
         cursor = db.cursor()
         cursor.execute('select * from blog where title ="'+name+'"')
         result = cursor.fetchall()
         return json.dumps(result)

	def add_blog(self,name):
		cursor = db.cursor()
		cursor.execute("insert into blog values('"+name+"')")
		db.commit()
		return 'add success'


service = Service()

@app.route('/', methods=['GET','POST'])
def index():
	data = json.loads(service.get_blogs())
	return render_template('index.html',datas = data)

@app.route('/search/<name>/', methods=['GET','POST'])
def search(name):
	data = json.loads(service.get_blog(name))
	return render_template('index.html',datas= data)

@app.route('/addblog/<name>/', methods=['GET','POST'])
def addblog(name):
	data = service.add_blog(name)
	return render_template('index.html', datas=[data])



if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000,)