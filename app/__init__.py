from flask import Flask  #statement to import the Flask() function#
from app.routes import home
from app.routes import home, dashboard

def create_app(test_config=None): 
  # def keyword used to define the create_app() function.
  # set up app config
  app = Flask(__name__, static_url_path='/') #initiate from the root directory, in this instance - python-newsfeed
  app.url_map.strict_slashes = False
  app.config.from_mapping(
    SECRET_KEY='super_secret_key' #creating a server-side session. 
  )
  @app.route('/hello') #decorator - turns the hello() into a route
  def hello():
    return 'hello world'
# register routes
  app.register_blueprint(home)
  app.register_blueprint(dashboard)
 
# the above hello() returns a string
#The funtions return becomes the route's response
# the result browser link : http://127.0.0.1:5000/hello

  return app

  #note:
  # run the flask app :
  #step 1: export FLASK_APP=app in the app directory  for macos
  #step 2: python -m flask run in the app directory


#As a comparison, the following example code shows how to create the same route by using Express.js:
  # app.get('/hello', (req, res) => {
 # res.send('hello world');
#   });
