from flask import Flask, request, url_for, redirect, send_from_directory, jsonify, make_response, Response, stream_with_context, send_file
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from PIL import Image
from base64 import encodebytes
import io
import os
from db import Account, House, Room
from random import random
from utils import searchController
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///roomstolet.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['IMAGE_UPLOADS'] = r'C:\Users\HP\Desktop\Scripts\RoomsToLet\uploads'
app.config['images'] = 'D:/GDWhatsApp/Media/GBWhatsApp Images'

db = SQLAlchemy(app)

@app.route('/')
def home():
	return 'Home'

@app.route('/login2/<username>/<password>')
def login2(password, username):
	acc = db.session.query(Account).filter_by(username=username, password=password).first_or_404()

	return acc.username
@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		acc = db.session.query(Account).filter_by(username=username, password=password).first()
		if acc:
			return f'{username} == post was succesfull completed'
		else:
			return 'Invalid username or password'
	else:
		return 'Not sure what happend'
@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
	''' create an account for a user '''
	if request.method == 'POST':
		firstname = request.form['firstname']
		secondname = request.form['secondname']
		email = request.form['email']
		username = request.form['username']
		password = request.form['password']
		image = request.files['image']
		image.save(f'uploads/{secure_filename(image.filename)}')
		acc = Account(firstname=firstname,
					  secondname=secondname,
					  email=email,
					  username=username,
					  password=password,
					  avatar=secure_filename(image.filename))
		db.session.add(acc)
		db.session.commit()
		return 'Ok'
	else:
		return "couldn't create account"
@app.route('/house', methods=['GET', 'POST'])
def house():
	if request.method == 'POST':
		housetype = request.form['housetype']
		location_description = request.form['location_description']
		floorspace = request.form['floorspace']
		name = request.form['name']
		region = request.form['region']
		location = request.form['location']
		rooms = request.form['rooms']
		water = True if request.form['water'] == 'True' else False
		rent = request.form['rent']
		gps = request.form['gps']

		#upload the  picture 
		file = request.files['picture']
		file.save(f'uploads/{secure_filename(file.filename)}')
		picture = secure_filename(file.filename)
		hse = House(housetype=housetype,
					location_description=location_description,
					floorspace=floorspace,
					name=name,
					region=region,
					location=location,
					rooms=rooms,
					water=water,
					rent=rent,
					pictures=picture,
					gps=gps
					)
		db.session.add(hse)
		db.session.commit()
		return 'Uploaded succesfully'
	else:
		return 'An error occured'
@app.route('/room', methods=['GET','POST'])
def room():

	if request.method == 'POST':
		name = request.form['hotelname']
		region= request.form['region']
		roomtype = request.form['roomtype']
		location = request.form['location']
		gps = request.form['gps']
		amount = request.form['amount']
		description = request.form['description']
		rm = Room(hotelname=name,
				  region=region,
				  roomtype=roomtype,
				  location=location,
				  gps=gps,
				  amount=amount,
				  description=description,
				  )
		#upload the picture
		if request.files['picture']:
			file = request.files['picture']
			file.save(f'uploads/{secure_filename(file.filename)}')
			picture = secure_filename(file.filename)
			rm.picture = picture
		else:
			rm.picture = ''
		db.session.add(rm)
		db.session.commit()
		return 'succesfully updated'
	else:
		return 'An error occured'

@app.route('/check_username', methods=['GET','POST'])
def check_username():
	if request.method == 'POST':
		username = request.form['username']
		acc = db.session.query(Account).filter_by(username=username).first()
		if acc:
			return 'Invalid'
		else:
			return 'Not in use'

@app.route('/upload', methods=['GET', 'POST'])
def upload():
	if request.method == 'POST':
		file = request.files['file']
		file.save(f'uploads/{secure_filename(file.filename)}')
		return 'uploaded succesfully'
	else:
		return 'Error uploading file'
@app.route('/files')
def file():
	return redirect(url_for('uploads', filename='tehran.mp4'))

@app.route('/search', methods=['GET', 'POST'])
def search():
	if request.method == 'POST' or request.method == 'GET':
		query = request.form['searchQuery']
		searchcontroller = searchController(query=query)
		return jsonify(searchcontroller)
	return 404




@app.route('/uploads/<filename>')
def uploads(filename=''):
	return send_from_directory(app.config['IMAGE_UPLOADS'], filename)

def get_response_image(image_path):
    pil_img = Image.open(image_path, mode='r') # reads the PIL image
    byte_arr = io.BytesIO()
    pil_img.save(byte_arr, format='png') # convert the PIL image to byte array
    encoded_img = encodebytes(byte_arr.getvalue()).decode('utf-8') # encode as base64
    return encoded_img

@app.route('/get_images',methods=['GET'])
def get_images():
    ##result  contains list of path images
	result = images_path()
		
	return jsonify(images=result)
@app.route('/get_file/<filepath>',methods=['GET'])
def get_file(filepath):
	filename = filepath
	return send_from_directory(app.config['images'], filename)
	
def images_path():
	import os
	path = 'D:/GDWhatsApp/Media/GBWhatsApp Images'
	img = os.listdir(path)
	imgs = [i for i in img if i.endswith('.jpg') or i.endswith('.png')]
	return imgs


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0',  use_reloader=True)



