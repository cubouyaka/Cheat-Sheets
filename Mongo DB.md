
# Basics 

Open that shell in a terminal:  
```mongosh 
mongosh
```

Show databases:
```mongosh 
show dbs
```

Use a database: put us inside `db_name` db and creates it if it doesn't exists already:
```mongosh
use db_name
```

Then to see our collections inside the db we are using:
```mongosh
show collections
```

To see everything that is in the collection (ie without any conditions):
```mongosh 
db_name.collection_name.find()
```

To delete the `db_name` database:
```mongosh 
db_name.dropDatabase()
```

# Insert

Insert One object in our collection:
```mongosh 
db_name.collection_name.insertOne({name: "Alex"})
```
Insert Many objects in once:
```mongosh 
db_name.collection_name.insertMany([{name: "Alex"}, {name: "Luce"}])
```



# Sort

To Sort by age increasing first, then by decreasing name (alphabetically) on a find result:
```mongosh 
db_name.collection_name.find().sort({age: 1, name: -1})
```


# Count

To `count` how many `users` have age `43`:
```mongosh
db_name.users.countDocuments({ age: 43})
```

# Find

## Find with specific value

Find all the objects with a specific name (or all that are not named differently):
```mongosh 
db_name.collection_name.find({name: "Alex"})
db_name.collection_name.find({name: {$eq: "Alex"}})
db_name.collection_name.find({name: {$neq: "Luce"}})
```

Find all the objects with name `Alex` and age `23`:
```mongosh
db_name.collection_name.find({name: "Alex", age: 23})
db_name.collection_name.find({$and: [{age: 23, name: "Alex"})
```

Find all the objects with a specific age but displaying only the name field and the adress and without the id:
```mongosh 
db_name.collection_name.find({age: 27}, {name: 1, adress: 1, _id: 0})
```

To find all the objects with a specific age, displaying everythinf except the age
```mongosh 
db_name.collection_name.find({age: 27}, {age: 0})
```

## Greater than, Less than, or equal

To find all the objects with age greater than (or equal, less than, less or equal) a specific value:
```mongosh 
db_name.collection_name.find({age: {$gt: 23}})
db_name.collection_name.find({age: {$gte: 34}})
db_name.collection_name.find({age: {$lt: 17}})
db_name.collection_name.find({age: {$lte: 84}})
```

## Find from a list

To find all the objects with `name` in a given a list (or not in the list, the opposite):
```mongosh
db_name.collection_name.find({name: {$in: ["Alex", "Luce"]}})
db_name.collection_name.find({name: {$nin: ["Cinna", "Lucie"]}})
```

## Find if given key exist

To find all the object that have a key `age` (or not by replacing by `False`) but doesn't check if the value exists:
```mongosh
db_name.collection_name.find({age: {$exists: True}})
```

## Find One

Find the first `user` that has age equal to `33`:
```mongosh
db_name.collection_name.findOne({ age: 33})
```

## Complexe Examples

Find `users` with age between 20 and 45 and with `name` equal to `Alex` or `Luce`:
```mongosh
db.users.find({age : {$gte: 20, $lte: 45}, name: {$in: ["Alex", "Luce"]}})
```

Find `users` with age greater than `24` or named `Alex`:
```mongosh
db_name.collection_name.find({ $or: [{ age: { $gte: 45}}, {name: "Alex"}]})
```

Find `users` that have greater `money` than `debt`:
```mongosh
db_name.collection_name.find({$expr: {$gt: ["$money", "$debt"]}})
```

# Update

## Update One

##### Update all `users` that have `age` equal  to `23` to an age equal to `24`:
```mongosh
db_name.users.updateOne({age: 23}, {$set: {age: 24}})
```
Which is the same as incrementing the `age` by `1`:
```mongosh
db_name.users.updateOne({age: 23}, {$inc: {age: 1}})
```

##### Update properly (rename and unset):
```mongosh
db_name.users.updateOne({_id: ObjectId("13424646758458")}, {$rename: {name: "Alex"}})
```

And to `unset` properly a value:
```mongosh
db_name.users.updateOne({_id: ObjectId("13424646758458")}, {$unset: {age: ""}})
```

##### Add a new value in `hobbies`:
```mongosh
db_name.users.updateOne({_id: ObjectId("13424646758458")}, {$push: {hobbies: "Swimming"}})
```
##### Remove a value 
```mongosh
db_name.users.updateOne({_id: ObjectId("1342466758458")}, {$pull: {hobbies: "Running"}})
```
## Update Many

Remove all the addresses (so when the adress exists):
```mongosh
db_name.users.updateMany({address: {$exists: true}}, {$unset: {address: ""}})
```
# Delete

## DeleteOne

```mongosh
db_name.users.deleteOne({name: "John"})
```

## DeleteMany

Delete all `users` that don't have an age:
```mongosh
db_name.users.deleteMany({age: {$exists: false}})
```


