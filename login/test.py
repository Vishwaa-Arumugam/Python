# # import requests, pprint
# from geopy.distance import geodesic as GD
# #
# # place_name = input('ENTER the city name : ').split(',')
# # d = []
# #
# # for i in range(len(place_name)):
# #     response = requests.get(f"https://api.tomtom.com/search/2/geocode/{place_name[i]}.json?key=xIHjaLJlArvKxQ0dzAYEKCx4W6JV0fCl")
# #     a = response.json()
# #     pprint.pprint(a['results'][0]['position'])
# #
# # #     d[place_name[i]] = a['results'][0]['position']
# # print(d)
#
# from geopy.geocoders import Nominatim
#
# geolocator = Nominatim(user_agent="MyApp")
#
# place_name = input('ENTER the city name : ').split(',')
# a=[]
#
# for i in range(len(place_name)):
#     location = geolocator.geocode(place_name[i])
#     a.append((location.latitude, location.longitude))
#     # print(location.latitude, location.longitude)
# print("distance : ", GD(a[0],a[1]).km)

# from playwright.sync_api import sync_playwright
# import pandas as pd, openpyxl
#
# def test():
#
#     with sync_playwright() as p:
#
#         checkin_date = '2023-06-06'
#         checkout_date = '2023-06-08'
#
#         URL = f'https://www.booking.com/searchresults.en-us.html?checkin={checkin_date}&checkout={checkout_date}&selected_currency=USD&ss=Chennai&ssne=Chennai&ssne_untouched=Chennai&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_type=city&group_adults=1&no_rooms=1&group_children=0&sb_travel_purpose=leisure'
#
#         print(URL)
#
#         browser = p.chromium.launch(headless=False)
#         page = browser.new_page()
#         page.goto(URL, timeout=60000)
#
#         hotels = page.locator('//div[@data-testid="property-card"]').all()
#         print(f'There are: {len(hotels)} hotels.')
#
#         hotels_list = []
#         for hotel in hotels:
#             hotel_dict = {}
#             hotel_dict['hotel'] = hotel.locator('//div[@data-testid="title"]').inner_text()
#             hotel_dict['price'] = hotel.locator('//span[@data-testid="price-and-discounted-price"]').inner_text()
#             hotel_dict['score'] = hotel.locator('//div[@data-testid="review-score"]/div[1]').inner_text()
#             hotel_dict['avg review'] = hotel.locator('//div[@data-testid="review-score"]/div[2]/div[1]').inner_text()
#             hotel_dict['reviews count'] = \
#             hotel.locator('//div[@data-testid="review-score"]/div[2]/div[2]').inner_text().split()[0]
#
#             hotels_list.append(hotel_dict)
#
#
#
#         print(hotels_list)
#
#         df = pd.DataFrame(hotels_list)
#         df.to_csv('test.csv', index=False)
#
#         browser.close()
#
# if __name__ == "__main__":
#     test()

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/receive_list', methods=['POST'])
def receive_list():
    input_list = request.get_json()
    print(input_list)  # Print the received list in the Flask server console

    return jsonify({'message': 'List received'})


if __name__ == '__main__':
    app.run()

