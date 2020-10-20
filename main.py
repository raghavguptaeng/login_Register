from flask import Flask,render_template,request
import mysql.connector
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/login"
db = SQLAlchemy(app)
mydb = mysql.connector.connect(host="localhost",user="root",passwd="")
m = mydb.cursor() #------------ m will exeute all mysql commands
m.execute('use login')#---- we are using database login
db = SQLAlchemy(app)
#----- making a table strusture for entering elements in mysql
class details(db.Model):
	email = db.Column(db.String(60), primary_key = True)
	name = db.Column(db.String(60), nullable=False)
	passw = db.Column(db.String(20), nullable=False)
#------------- Following are the routes for login page
@app.route('/',methods=['GET','POST'])
def login():
	if(request.method == 'POST'):
		email = request.form.get('uname')
		pas = request.form.get('passw')
		m.execute("select passw from details where email = '{0}' ".format(email))
		for i in m:
			if(i[0]==pas):
				return render_template('success.html')
	return render_template("index.html")
@app.route('/index.html',methods=['GET','POST'])
def login_back():
	if (request.method == 'POST'):
		email = request.form.get('uname')
		pas = request.form.get('passw')
		#------- Checking of id and password starts here
		m.execute("select passw from details where email = '{0}' ".format(email))
		for i in m:
			if (i[0] == pas):
				return render_template('success.html')
	return render_template("index.html")

#-------------- following is the route for registeration page
@app.route('/Register.html',methods=['GET','POST'])
def register():
	if (request.method == 'POST'):
		uname = request.form.get('uname')
		passw = request.form.get('passw')
		email = request.form.get('email')
		data = details(email = email,name = uname,passw=passw)
		db.session.add(data)
		db.session.commit()
	return render_template("Register.html")
#--------------------------------------------------------------

if __name__ == '__main__':
	app.run(debug=True)
