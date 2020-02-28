from firebase import firebase
import json
firebase = firebase.FirebaseApplication('https://ai-doctor-97577.firebaseio.com/', None)
data = {
       'username':'abhishek',
       'password':'pass1'
       ''
      }

result = firebase.put('users',username,data['username'])


result=firebase.get('/users/username','')


print (result)
