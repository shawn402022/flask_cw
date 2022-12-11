from app import app
from flask import render_template
from app.models import Post

user_data = { 
    'hamzah':{
        'user_id':1,
        'email': 'hamzah@gmail.com',
        'name': 'Hamzah Ali',
        'favfood':'mac n cheese',
        'is_active': True,
        'reviews': ['growing','loud']
    },

    'yahya':{
        'user_id':2,
        'email': 'yahya@gmail.com',
        'name': 'Yahya Ali',
        'favfood':'breast milk',
        'is_active': True,
        'reviews': ['loud', 'quiet']
    },

    'soufian':{
        'user_id':3,
        'email': 'souf@gmail.com',
        'name': 'souf ali',
        'favfood':'breast milk',
        'is_active': False,
        'reviews': ['loud', 'quiet']
    }
}

car_data = {
    '0': {
        "name": "Maruti Swift Dzire VDI",
        "year": 2014,
        "selling_price": 450000
    },
    '1': {
        "name": "Skoda Rapid 1.5 TDI Ambition",
        "year": 2014,
        "selling_price": 370000
    },
    '2': {
        "name": "Honda City 2017-2020 EXi",
        "year": 2006,
        "selling_price": 158000
    }
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/profile/<username>')
def display_profile(username):
    return render_template('1_profile.html.j2',**user_data[username])

@app.route('/cars')
def display_cars():
    return car_data

@app.route('/cars/cars')
def display_car_id():
    return render_template('cars2.html.j2', car_data=car_data)

@app.route('/posts')
def posts():
    all_posts =Post.query.all()
    return render_template('posts.html', posts=all_posts)

#Create a dynamic route that allos us
#to get a singple post, based on it's id

@app.route('/post/<id>')
def post_by_id(id):
    post = Post.query.get(int(id))
    return render_template('post-single.html', post=post)