import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Setup
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Previous Tutorial:
# db.collection('pymenu').add({'category':'Beverage', 'name':'Water', 'price':2.99})

# Add documents:
# db.collection('MenuMaker').add({'category': 'Beverage', 'name': 'Water', 'price': 0.99, 'specialty': False})
# db.collection('MenuMaker').add({'category': 'Beverage', 'name': 'Fountain Soda', 'price': 1.49, 'specialty': False})
# db.collection('MenuMaker').add({'category': 'Beverage', 'name': 'Shirley Temple', 'price': 3.49, 'specialty': True})
# db.collection('MenuMaker').add(
#     {'category': 'Beverage', 'name': 'Blood Orange Margarita', 'price': 4.99, 'specialty': True})
# db.collection('MenuMaker').add({'category': 'Appetizer', 'name': 'Shrimp Bites', 'price': 6.99, 'specialty': False})
# db.collection('MenuMaker').add({'category': 'Appetizer', 'name': 'French Fries', 'price': 6.49, 'specialty': False})
# db.collection('MenuMaker').add({'category': 'Appetizer', 'name': 'Escargot', 'price': 9.99, 'specialty': True})
# db.collection('MenuMaker').add({'category': 'Appetizer', 'name': 'Cocktail Meatballs', 'price': 9.49, 'specialty': True})
# db.collection('MenuMaker').add({'category': 'Meal', 'name': 'Filet Mignon', 'price': 22.49, 'specialty': False})
# db.collection('MenuMaker').add({'category': 'Meal', 'name': 'Penne Alla Vodka', 'price': 18.49, 'specialty': False})
# db.collection('MenuMaker').add(
#     {'category': 'Meal', 'name': 'Skillet-Cooked Duck Breast', 'price': 29.99, 'specialty': True})
# db.collection('MenuMaker').add(
#     {'category': 'Meal', 'name': 'Cashew Milk Alfredo Pasta', 'price': 20.99, 'specialty': True})
# db.collection('MenuMaker').add({'category': 'Dessert', 'name': 'Fruit Sundae', 'price': 10.49, 'specialty': False})
# db.collection('MenuMaker').add({'category': 'Dessert', 'name': 'Chocolate Moose Cake', 'price': 13.99, 'specialty': True})
# db.collection('MenuMaker').add({'category': 'Dessert', 'name': 'Cannolis', 'price': 9.49, 'specialty': False})
# db.collection('MenuMaker').add({'category': 'Dessert', 'name': 'Crème Brulee', 'price': 12.99, 'specialty': True})

# Dummy Menu Item:
# db.collection('pymenu').document('Dummy').set({'category': 'Dummy', 'name': 'Dummy', 'price': 0.00})

# Read Data:
#   Getting Document with a known id -
#   result = db.collection('pymenu').document("Dummy").get()
#   if result.exists:
#       print(result.to_dict())
#   Get all documents in a collection -
#   menu = db.collection('MenuMaker').get()
#   for item in menu:
#       print(item.to_dict())
#   Querying -
#       menu = db.collection('MenuMaker').where("price", ">", 9.99).get()
#       for item in menu:
#           print(item.to_dict())

# Delete Data:
#   Known Id -
#       db.collection('pymenu').document('Dummy3').delete()
#   Known Id - Field -
#       db.collection('pymenu').document('Dummy2').update({"price": firestore.DELETE_FIELD})
#   Unknown Id
docs = db.collection('pymenu').get()
for doc in docs:
    key = doc.id
    db.collection('pymenu').document(key).delete()
