from flask import Flask , render_template , request , url_for
import investpy


app = Flask(__name__)

@app.route('/' )
def home():

    return render_template ('index.html')

@app.route('/result')
def result():
    stock  = request.args.get('stock').upper()

    return render_template('result.html' , stock=stock)




if __name__ == '__main__' :
    app.run()