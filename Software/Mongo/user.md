Show User
---------
> show users

Create User
-----------
db.createUser({
    user: 'your_name',
    pwd: 'your_password',
    roles: [{ role: 'readWrite', db:'your_db'}]
})

Delete User
-----------
db.dropUser('username')
