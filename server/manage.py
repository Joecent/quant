from flask import Flask
from Data  import MysqlData

app = Flask(__name__)
 
 
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/app')
def hello_moco():
    return 'Hello Moco'

@app.route('/my_data')
def my_data():
    data2 = MysqlData()
    data3 = data2.fetch_mysql()
    return data3
    #return data.fetch_mysql()
if __name__ == '__main__':
    app.run()
