import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "YOUR_KEY"
NEWS_API_KEY = "NEWS_API_KEY"
acc_sid = "ACC_SID_FROM_TWILIO"
auth_token = "TWILIO_TOKEN"

parameters = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": STOCK_API_KEY
}

news_parameters = {
        "q": 'tesla',
        "apiKey": NEWS_API_KEY

    }

stock_response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
stock_response.raise_for_status()
whole_data = stock_response.json()["Time Series (60min)"]
data_list = [value for (key, value) in whole_data.items()]
yesterday_data = float(data_list[0]["4. close"])
day_before_yesterday_data = float(data_list[1]["4. close"])

difference = abs(yesterday_data - day_before_yesterday_data)

diff_percentage = (difference / yesterday_data) * 100
print(diff_percentage)

if diff_percentage > 5:

    news_response = requests.get(url="https://newsapi.org/v2/top-headlines", params=news_parameters)
    news_response.raise_for_status()

    news_headlines = []
    news_description = []
    for i in range(0, 3):
        news_data_0 = news_response.json()["articles"][i]
        news_title_0 = news_data_0["title"].split('|')
        news_desc = news_data_0["description"]
        news_headlines.append(news_title_0[0])
        news_description.append(news_desc)

    client = Client(acc_sid, auth_token)

    message = client.messages \
        .create(
        body=f"TSLA: 🔺{diff_percentage}%\n\n"
             f"HEADLINE : {news_headlines[0]}\n\n"
             f"DESCRIPTION: {news_description[0]}\n\n\n"
             f"HEADLINE : {news_headlines[1]}\n\n"
             f"DESCRIPTION: {news_description[1]}\n\n\n"
             f"HEADLINE : {news_headlines[2]}\n\n"
             f"DESCRIPTION: {news_description[2]}\n\n\n",
        from_='+15076783397',
        to='+919500288874'
    )
    print(message.status)
