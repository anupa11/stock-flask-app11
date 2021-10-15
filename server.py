# API Key : d6cd75b36a0c9a4c6ad1a038177b6ea3
# https://financialmodelingprep.com/api/v3/stock/real-time-price/AAPL?apikey=d6cd75b36a0c9a4c6ad1a038177b6ea3
# https://financialmodelingprep.com/api/v3/profile/AAPL?apikey=d6cd75b36a0c9a4c6ad1a038177b6ea3
# https://financialmodelingprep.com/api/v3/financials/income-statement/AAPL?apikey=d6cd75b36a0c9a4c6ad1a038177b6ea3&period=quarter

from flask import Flask, render_template

from blueprints.home import home
from blueprints.stock import stock


app = Flask(__name__)


app.register_blueprint(stock, url_prefix='/stock')
app.register_blueprint(home)





    
if __name__ == '__main__':
    app.run(debug=True)
