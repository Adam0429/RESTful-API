from flask import Flask,abort,request,redirect,render_template,jsonify  
from flask_script import Manager
# from flask_bootstrap import Bootstrap
# from wtforms import StringField,SubmitField
# from wtforms.validators import Required


app = Flask('my web')
app.config['SECRET_KEY'] = '1234231'


members = {
	'wfh': {	
	'name':'wangfeihong',
	'age':'20',
	'IQ':5000
	},

	'wy' : {
	'name':'wuyu',
	'age':'100',
	'IQ':0	
	},

	'cyx' : {
	'name':'chenyixiao',
	'age':'2',
	'IQ':0
	},

	'dw' : {
	'name':'duwei',
	'age':'0',
	'IQ':0
	}
}

# @app.errorhandler(404)
# def not_found(error):
#     return jsonify({'error': 'Not found'})

@app.route('/todo/api/v1.0/member/', methods=['GET'])
def get_members():	
	return jsonify(members)

@app.route('/todo/api/v1.0/member/<name>', methods=['GET'])
def get_member(name):
	if name not in members.keys():
		abort(404)
	else:
		return jsonify(members[name])
	

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000,debug=True)
