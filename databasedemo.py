import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyB_VHnTA25q0Gal-7SJU1nHjc2-tGovrPo",
  'authDomain': "id-card-gen-caa8d.firebaseapp.com",
  'databaseURL': "https://id-card-gen-caa8d-default-rtdb.firebaseio.com",
  'projectId': "id-card-gen-caa8d",
  'storageBucket': "id-card-gen-caa8d.appspot.com",
  'messagingSenderId': "737601243554",
  'appId': "1:737601243554:web:0cb33796426201b1d04afb",
  'measurementId': "G-K1L084BCH8"
};

firebase = pyrebase.initialize_app(firebaseConfig)
storage = firebase.storage()
database = firebase.database()

database.child("IDS")
data = {
    "Name" : "Yash",
    "mail" : "ybhappa@gmail.com"
}
database.set(data)