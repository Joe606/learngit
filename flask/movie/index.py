from flask import (Blueprint,g,request,render_template,flash)
from movie.to_mysql import connection

con,cur = connection()

bp = Blueprint('index',__name__)
@bp.route('/')
def index():
	name = '蜘蛛侠'
	sql = '''desc movie;'''
	cur.execute(sql)
	data = cur.fetchall()

	return str(data)

@bp.route('/m',methods=('GET','POST'))
def m():
	if request.method == 'GET':
		data = '请输入！'
	elif request.method == 'POST':
		name = request.form['movie_name']
		name = name.strip()
		sql = '''select * from movie where title="'%s'";''' %name
		
		
		if cur.execute(sql):
			data = cur.fetchall()[0]

		else:
			data = '抱歉，未录入!!!'
			flash(data)

	return render_template('data.html',data=data)