from flask import Blueprint, render_template
import requests

stock = Blueprint('stock', __name__)

def fetch_price(ticker):
    data = requests.get(f'https://financialmodelingprep.com/api/v3/stock/real-time-price/{ticker}', params={'apikey': 'd6cd75b36a0c9a4c6ad1a038177b6ea3'}).json()
    
    return data["price"]

def fetch_income(ticker):
    financials = requests.get(f'https://financialmodelingprep.com/api/v3/financials/income-statement/{ticker}', params={'period': 'quarter', 'apikey': 'd6cd75b36a0c9a4c6ad1a038177b6ea3'}).json()["financials"]
    financials.sort(key=lambda quarter: quarter["date"])
    return financials

@stock.route('/<string:ticker>')
def quote(ticker):
    price = fetch_price(ticker)
    return render_template('stock/quote.html', ticker = ticker, stock_price = price)

@stock.route('/<string:ticker>/financials')
def financials(ticker):
    data = fetch_income(ticker)

    chart_data = [float(q["EPS"]) for q in data if q["EPS"]]
    chart_params = {"type": 'line',
                    "data": {
                        'labels': [q["date"] for q in data if q["EPS"]],
                        'datasets': [{'label': 'EPS', 'data': chart_data}]
                    }}




    return render_template('stock/financials.html', ticker = ticker, financials = data, chart_params = chart_params)
