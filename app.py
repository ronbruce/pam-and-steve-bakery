from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from data import bakery_items

# TODO
# Connect data.py to app.py.✅
# Insert data into bakery_database ✅
# Display data dynamically from data.py unto my web pages in template.✅
# Format items in the cart using video.
# Follow along with documentation to import any other data, or CRUD operation. 
app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')
#TODO 
# move secret key into a .env file.
app.config["SECRET_KEY"] = '51e5bbc093285a7ff86bfd0bb8bbd69404baa3f8'

client = MongoClient('mongodb://localhost:27017/')
# This is the MongoDB database for bakery items.
db = client['bakery_database']

# Inset data into a collection for bakery items.
bakery_collection = db["bakery_items"]


# Check for existing data before insertion.
# I'm using the count_documents method to check for any existing documents in my collection before insertion.
# If the count is equal to 0, it means there are no existing documents, so I insert the new data into the database using insert_many().
# However, if the count is not 0, it means data is already present, so the insertion is skipped.
# I'm using this approach to prevent duplicates from appearing in my database whenever I save my Python file.

count = bakery_collection.count_documents({})
if count == 0:
    # Insert new data
    bakery_collection.insert_many(bakery_items)
    print("Data inserted successfully.")
else:
    print("Data already exists. Skipping insertion")
    
@app.route("/", methods=['GET', 'POST'])
def index():
    title = "p&s bakery and restaurant"
    cart_items = db.bakery_collection.find()
    # bread_items = db.bakery_collection.find({"category":"bread"})
    # cake_items = db.bakery_collection.find({"category":"flatbread"})
    # drinks_items = db.bakery_collection.find({"category":"drinks"})
    return render_template("index.html", title=title, cart_items=cart_items)

@app.route('/menu/bread')
def bread():
    bread_title = "bread"
    return render_template("menu/bread.html", bread_title=bread_title)

@app.route('/menu/breakfast')
def breakfast():
    breakfast_title = "breakfast"
    return render_template("menu/breakfast.html", breakfast_title=breakfast_title)

@app.route('/menu/lunch')
def lunch():
    lunch_title = "lunch"
    return render_template("menu/lunch.html", lunch_title=lunch_title)

@app.route('/menu/snacks')
def snacks():
    snacks_title = "snacks"
    return render_template("menu/snacks.html", snacks_title=snacks_title)

@app.route('/menu/pastries')
def pastries():
    pastries_title = "pastries"
    return render_template("menu/pastries.html", pastries_title=pastries_title)

@app.route('/menu/sweetsTreats')
def sweetsTreats():
    sweets_treats_title = "sweets & treats"
    return render_template("menu/sweetsTreats.html", sweets_treats_title=sweets_treats_title)

@app.route('/menu/drinks')
def drinks():
    drinks_title = "drinks"
    return render_template("menu/drinks.html", drinks_title=drinks_title)

@app.route('/footer/aboutUs')
def aboutUs():
    about_us_title = "about us"
    return render_template("footer/aboutUs.html", about_us_title=about_us_title)

@app.route('/footer/contact')
def contact():
    contact_title = "contact"
    return render_template("footer/contact.html", contact_title=contact_title)

@app.route('/home/aboutGuyaneseFood')
def aboutGuyaneseFood():
    about_guyanese_food_title = "about guyanese food and culture"
    return render_template("home/aboutGuyaneseFood.html", about_guyanese_food_title=about_guyanese_food_title)

@app.route('/home/catering')
def catering():
    catering_title = "catering"
    return render_template("home/catering.html", catering_title=catering_title)

if __name__ == "__main__":
    app.config['ENV'] = 'development'
    app.run(debug=True)