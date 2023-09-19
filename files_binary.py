# import requests
#
# url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSIIYBJYkk1Awy6BLgzpSYedtcIly842HuzRiuYkojioA&s'
#
# response = requests.get(url)
# print(response.content)
#
# with open('flowers.png', mode='wb') as file:
#     file.write(response.content)

with open('flowers.png', mode='rb') as file:
    print(file.read())


