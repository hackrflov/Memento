db.createUser({
    user: 'ian',
    pwd: 'secretPassword',
    roles: [{ role: 'readWrite', db:'cool_db'}]
})
