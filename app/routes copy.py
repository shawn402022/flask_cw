# from app import app
# from flask import render_template

# user_data = { 
#     'hamzah':{
#         'user_id':1,
#         'email': 'hamzah@gmail.com',
#         'name': 'Hamzah Ali',
#         'favfood':'mac n cheese',
#         'is_active': True,
#         'reviews': ['growing','loud']
#     },

#     'yahya':{
#         'user_id':2,
#         'email': 'yahya@gmail.com',
#         'name': 'Yahya Ali',
#         'favfood':'breast milk',
#         'is_active': True,
#         'reviews': ['loud', 'quiet']
#     },

#     'soufian':{
#         'user_id':3,
#         'email': 'souf@gmail.com',
#         'name': 'souf ali',
#         'favfood':'breast milk',
#         'is_active': False,
#         'reviews': ['loud', 'quiet']
#     }
# }

# car_data = {
#     '0': {
#         "name": "Maruti Swift Dzire VDI",
#         "year": 2014,
#         "selling_price": 450000
#     },
#     '1': {
#         "name": "Skoda Rapid 1.5 TDI Ambition",
#         "year": 2014,
#         "selling_price": 370000
#     },
#     '2': {
#         "name": "Honda City 2017-2020 EXi",
#         "year": 2006,
#         "selling_price": 158000
#     }
# }

# #create 2 routes/templates:
# # - display all cars using a for loop and thier information( not dynamic)

# # - display a specific car and its's inforamtion (will be dynamc, you can use the car's id in the car data dictionary)

# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/profile/<username>')
# def display_profile(username):
#     return render_template('1_profile.j2',**user_data[username])

# @app.route('/profile/car')
# def display_car():
#     return render_template('cars.html',car_data=car_data)
 


# @app.route('/profile/car/<carid>')
# def display_carName(carid):
#     return render_template('cars2.html',
#     car_data=car_data)




# # Get all users and thier data
# @app.route('/api/users')
# def get_users():
#     return user_data

# @app.route('/api/user/<username>')
# def get_user_by_username(username):
#     if username in user_data:
#         return user_data[username]
#     return f'user with username {username} not found'

# # Get all user emails
# @app.route('/api/users/emails')
# def get_user_emails():
#     emails =[]

#     for user in user_data.values():
#         emails.append(user['email'])

#     return emails

# @app.route('/api/user/email/<email>')
# def get_user_by_email(email):
#     for user in user_data:
#         if user['email'] == email:
#             return user

#     return f'user with email {email} not found'


# #endpoint with two parameters
# # @app.route('/api/user/<username>/reviews/<review_idx>')
# # def get_user_review(username,review_idx):
# #     return user_data[username]['reviews'][int(review_idx)]

# # Write an endpoint, that returns a list of active user's names
# @app.route('/api/user/active')
# def get_user_active():
#     active = []
#     for user in user_data:
#         if user_data[user]['is_active'] == True:
#             active.append(user)
           
#     return active
    
# # you have to define a route variable





# # Get all cars

# @app.route('/api/user/car')
# def get_all_cars():
#     return car_data



# # Get cars in a dictionary separated by year, for example:
# # car_year_result = {
# #     2014: ["Maruti Swift Dzire VDI","Skoda Rapid 1.5 TDI Ambition"],
# #     2006: ["Honda City 2017-2020 EXi"]
# # }

# @app.route('/api/user/cars/years')
# def get_car_by_year():
#     result ={}
#     for car in car_data.values():
#         if car['year'] in result:
#             result[car['year']].append(car['name'])
        
#         else:
#             result[car['year']] = [car['name']]

#     return result





# # Get a car by it's ID (it's ID is just the key in the car data dictionary)
# @app.route('/api/user/car/<carid>')
# def get_car_id(carid):
#     carid = int(carid)
#     if carid in car_data:
#         return car_data[carid]

#     return f'{carid} not found'


 

# # Get all cars below a given price point, so if the user enters 380000, you'd show the second and third cars

# @app.route('/api/user/price/<price>')
# def get_car_below_price(price):
#     result = []
#     price = int(price)
#     for car in car_data.values():
#         if car['selling_price'] < price:
#             result.append(car)
#     return result




