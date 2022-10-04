
import firebase_admin
from firebase_admin import credentials # verifies that this computer can access the database as an admin 
from firebase_admin import firestore # create collections and documents 
from firebase_admin import auth # auth allows to  check with the database if user exists 
from firebase_admin import  storage # allows storage 


from firebase_confige import firebase_config


import pyrebase# this is for real time data base 


# this is the config for pyrebase module. This allows the user to interact with the real time data base



firebase = pyrebase.initialize_app(firebase_config)
a = firebase.auth()

cred = credentials.Certificate("serviceAccountKey.json") #This is the key that allows python to access firebase as an admin 

firebase_admin.initialize_app(cred, {'storageBucket': 'cse-310-aea3a.appspot.com'})# Allows the user to store information using storage bucket

db = firestore.client() # everything else is used with db / firebase_admin
tb = firebase.database()# only used for real time data base

my_log_in = input("Do you have a sign in? Y/N?") # gives the user a chance to create a log in or sign in 

if my_log_in.lower() == "n": #create an email and password to be able to log in 
    email = input("Enter your Email: ")
    password = input("Enter your Password: ")
    user = auth.create_user(email = email,password =  password)#creates a user using firebase_admin
    print("user_created")
    login = a.sign_in_with_email_and_password(email ,  password) # this created a token which is unique to the user 
    user_idToken = a.get_account_info(login["idToken"])
else:# this is if you already have an email and password set up.
    email = input("Enter your Email: ")
    password = input("Enter your password: ")
    login = a.sign_in_with_email_and_password(email ,  password)
    user_idToken = a.get_account_info(login["idToken"])

User = str(user_idToken).split(",")
User = User[2].split(":")
User = User[1].strip("\'")


logged_in = True

while logged_in: #while the user is logged in 

    option = input(f"\nWhat Would you like to do type [1-5]\n1. Upload/Remove to Fire Data Base\n2. Real Time DataBase\n3. Upload To Storage \n4. View User idToken\n5. query database\n6. quit\nEnter Here: ")

    if option == "1": # this is so you can add to an existing collection
        option_1 = input("To update type - 1 \nto create type - 2  \nto remove document type - 3?  \nAdd yourself to  people Table type - 4\n enter: ")
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
            collection_name = input("what is the collection name? : ") # gets the collection name from user
            document = input("what is the document name? : ")
            db.collection(collection_name).document(document).delete()
        elif option_1 == "4": #be able to add your own table to the people collection to save. Also shows user token to show when they uploaded and who.
            collection_name = "PEOPLE"
            first_name = input("What is your first name: ")
            last_name = input("What is your Last name: ")
    
            Address = input("What is your address: ")
            db.collection(collection_name).document(first_name + " " + last_name).set({"Email" :User , "Address" : Address , "User_token" : user_idToken})

    elif option == "2": # The user can add info to a real time data base
        option_2 = input("Do you want to write a message - type 1 or receive - type 2? ")
        if option_2 == "1":
            Name = input("What is your name: ")
            value = input("what is the message? : ")
            tb.child("Message").update({ Name: value}) # this uses pyrebase for the real time data base.
        if option_2 == "2":
            message = tb.child("Message").get()
            print(message.val())

    elif option == "3": # you are able to upload files to storage 
        fileName = input("insert your filename here: ")
        bucket = storage.bucket() #this is what allows the file to be uplaoded 
        blob = bucket.blob(fileName)
        blob.upload_from_filename(fileName)
    
    elif option == "4":# print out your user information
        print(user_idToken)    

    elif option == "5":
        collection_name = "PEOPLE" # makes it easy for the user to access their data if they dont need to know the collection name
        first_name = input("What is your first name: ")
        last_name = input("What is your Last name: ")
        doc_ref =  db.collection(collection_name).document(first_name + " " + last_name)
        doc = doc_ref.get()
        print(doc.to_dict())# grabs the data at that collection and document

    elif option == "6": # in order to log out 
        logged_in = False
        print("You are logged out") # the program stops and the user is logged out
    
    else: print(f"\n\n Type 1-6 \n\n") # this runs the loop if the user selects the wrong number
   



