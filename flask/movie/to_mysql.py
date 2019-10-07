import pymysql
def connection():
	con = pymysql.connect(
		host='49.232.154.41',
		port=3306,
		user='root',
		passwd='',
		db='douban_movie'
		)
	cur = con.cursor()
	return con,cur