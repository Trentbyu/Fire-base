
import pyrebase



firebase_config =  { "apiKey": "AIzaSyAPVchmwUHrBTlXohSiNOFi5HVQOYvCO1U",
  "authDomain": "cse-310-aea3a.firebaseapp.com",
  "databaseURL": "https://cse-310-aea3a-default-rtdb.firebaseio.com",
  "projectId": "cse-310-aea3a",
  "storageBucket": "cse-310-aea3a.appspot.com",
  "messagingSenderId": "377868974496",
  "appId": "1:377868974496:web:be9e762b3c4be1c39f0cc5"}


firebase = pyrebase.initialize_app(firebase_config)



tb = firebase.database()

auth = firebase.auth()


tb.child("Name").set({"name" : "tb"})


# MAKE USER AND AUTHENTICATE 
#get the valid email and password from the user
email = input("Please Enter Your Email : ")
password = input("Please Enter Your Password : ")

#and authenticate the user 
user = auth.create_user_with_email_and_password(email, password)
print("User Created Successfully")
