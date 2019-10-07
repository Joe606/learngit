#'''练习使用flask读取mysql数据，不使用orm'''
from flask import Flask

def create_app():
	app = Flask(__name__)
	app.config.update(
		DEBUG = True,
		TESTING = False,
		SECRET_KEY = '1234***',
	)


	from movie.index import bp
	app.register_blueprint(bp)

	return app
	

