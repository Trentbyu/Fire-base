
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth
from firebase_admin import  storage

import pyrebase



firebase_config =  { "apiKey": "AIzaSyAPVchmwUHrBTlXohSiNOFi5HVQOYvCO1U",
  "authDomain": "cse-310-aea3a.firebaseapp.com",
  "databaseURL": "https://cse-310-aea3a-default-rtdb.firebaseio.com",
  "projectId": "cse-310-aea3a",
  "storageBucket": "cse-310-aea3a.appspot.com",
  "messagingSenderId": "377868974496",
  "appId": "1:377868974496:web:be9e762b3c4be1c39f0cc5"}


firebase = pyrebase.initialize_app(firebase_config)
a = firebase.auth()

cred = credentials.Certificate("serviceAccountKey.json")


firebase_admin.initialize_app(cred, {'storageBucket': 'cse-310-aea3a.appspot.com'})

db = firestore.client()
tb = firebase.database()

my_log_in = input("Do you have a sign in? Y/N?")

if my_log_in.lower() == "N": #create an email and password to be able to log in 
    email = input("Enter your email: ")
    password = input("Enter your Password: ")
    user = auth.create_user(email = email,password =  password)
    print("user_created")
    login = a.sign_in_with_email_and_password(email ,  password)
    user_idToken = a.get_account_info(login["idToken"])
else:# this is if you already have an email and password set up.
    email = input("Enter your email: ")
    password = input("Enter your Password: ")

    login = a.sign_in_with_email_and_password(email ,  password)
    user_idToken = a.get_account_info(login["idToken"])


logged_in = True

while logged_in:


    option = input(f"\nWhat Would you like to do type [1-5]\n1. Upload/Remove to Fire Data Base\n2. write to Real Time DataBase\n3. Upload To Storage \n4. View User idToken\n5. query database\n6. quit\nEnter Here: ")

    if option == "1": # this is so you can add to an existing collection
        option_1 = input("To update type - 1 to create type - 2 to remove document type - 3? Add yourself Table type - 4: ")
        if option_1 == "1":
            collection_name = input("what is the collection name? : ")
            document = input("what is the document name? : ")
            key = input("what is the key name? : ")
            value = input("what is the  value? : ")
            db.collection(collection_name).document(document).update({key : value})
        
        elif option_1 == "2": # This is when you want to create a new collection 
            collection_name = input("what is the collection name? : ")
            document = input("what is the document name? : ")
            key = input("what is the key name? : ")
            value = input("what is the  value? : ")
            db.collection(collection_name).document(document).set({key : value})
        elif option_1 == "3": 
            collection_name = input("what is the collection name? : ")
            document = input("what is the document name? : ")
            db.collection(collection_name).document(document).delete()
        else:
            collection_name = "PEOPLE"
            first_name = input("WHat is your first name: ")
            last_name = input("WHat is your Last name: ")
            Email_name = input("WHat is your Email: ")
            db.collection(collection_name).document(first_name + " " + last_name).set({"Email" : Email_name})
            




    elif option == "2": # The user can add info to a real time data base
        name = input("what is the child name? : ")
        key = input("what is the key name? : ")
        value = input("what is the  value? : ")
        tb.child(name).set({key: value})

    elif option == "3": # you are able to upload files to storage 
        fileName = input("insert your filename here: ")
        bucket = storage.bucket()
        blob = bucket.blob(fileName)
        blob.upload_from_filename(fileName)
    
    elif option == "4":# print out your user information
        print(user_idToken)    

    elif option == "5":
        collection_name = input("what is the collection name? : ")
        document = input("what is the document name? : ")

        doc_ref = db.collection(collection_name).document(document)
        doc = doc_ref.get()
        print(doc.to_dict())



    elif option == "6": # in order to log out 
        logged_in = False
        print("You are logged out")
    
    else: print(f"\n\n Type 1-6 \n\n")
   



