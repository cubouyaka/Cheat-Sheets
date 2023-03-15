
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
use db
```

Create a collection `users` in the db:
```mongosh
db.createCollection("users")
```

Then to see our collections inside the db we are using:
```mongosh
show collections
```

To see everything that is in the collection (ie without any conditions):
```mongosh 
db.users.find()
```

To delete the `db_name` database:
```mongosh 
db.dropDatabase()
```

# Insert

Insert One object in our collection:
```mongosh 
db.users.insertOne({name: "Alex"})
```
Insert Many objects in once:
```mongosh 
db.users.insertMany([{name: "Alex"}, {name: "Luce"}])
```

```mongosh
db.users.insertMany([{name: "Alex", age:12, money:2346, debt:12342},{name: "Luce", age:25, money:23896, debt:9232}, {name: "Leon", age:78, money:137, debt:54}, {name: "Cinna", age:56, money:5246, debt:8906},{name: "Lucie", age:56, money:231, debt:564}])
```


# Sort

To Sort by age increasing first, then by decreasing name (alphabetically) on a find result:
```mongosh 
db.users.find().sort({age: 1, name: -1})
```


# Count

To `count` how many `users` have age `56`:
```mongosh
db.users.countDocuments({ age: 56})
```

# Find

## Find with specific value

Find all the objects with a specific name (or all that are not named differently):
```mongosh 
db.users.find({name: "Alex"})
db.users.find({name: {$eq: "Alex"}})
db.users.find({name: {$ne: "Luce"}})
```

Find all the objects with name `Alex` and age `12`:
```mongosh
db.users.find({name: "Alex", age: 12})
db.users.find({$and: [{age: 12}, {name: "Alex"}]})
```

Find all the objects with a specific age but displaying only the name field and the adress and without the id:
```mongosh 
db.users.find({age: 56}, {name: 1, money: 1, _id: 0})
```

To find all the objects with a specific age, displaying everythinf except the age
```mongosh 
db.users.find({age: 78}, {age: 0})
```

## Greater than, Less than, or equal

To find all the objects with age greater than (or equal, less than, less or equal) a specific value:
```mongosh 
db.users.find({age: {$gt: 23}})
db.users.find({age: {$gte: 34}})
db.users.find({age: {$lt: 17}})
db.users.find({age: {$lte: 84}})
```

## Find from a list

To find all the objects with `name` in a given a list (or not in the list, the opposite):
```mongosh
db.users.find({name: {$in: ["Alex", "Luce"]}})
db.users.find({name: {$nin: ["Cinna", "Lucie"]}})
```

## Find if given key exist

To find all the object that have a key `age` (or not by replacing by `False`) but doesn't check if the value exists:
```mongosh
db.users.find({age: {$exists: true}})
```

## Find One

Find the first `user` that has age equal to `78`:
```mongosh
db.users.findOne({ age: 78})
```

## Complexe Examples

Find `users` with age between 20 and 45 and with `name` equal to `Alex` or `Luce`:
```mongosh
db.users.find({age : {$gte: 20, $lte: 45}, name: {$in: ["Alex", "Luce"]}})
```

Find `users` with age greater than `24` or named `Alex`:
```mongosh
db.users.find({ $or: [{ age: { $gte: 45}}, {name: "Alex"}]})
```

Find `users` that have greater `money` than `debt`:
```mongosh
db.users.find({$expr: {$gt: ["$money", "$debt"]}})
```

# Update

## Update One

##### Update all `users` that have `age` equal  to `23` to an age equal to `24`:
```mongosh
db.users.updateOne(
	{age: 12}, 
	{$set: {age: 13}})
```
Which is the same as incrementing the `age` by `1`:
```mongosh
db.users.updateOne(
	{age: 12}, 
	{$inc: {age: 1}})
```

##### Unset properly a value
```mongosh
db.users.updateOne(
	{_id: ObjectId("6411ff792acf93a4a8994221")},
	{$unset: {age: ""}})
```

##### Add a new value in `hobbies`
```mongosh
db.users.updateOne(
	{_id: ObjectId("6411ff792acf93a4a8994221")}, 
	{$push: {hobbies: "Swimming"}})
```

##### To add a list of value
```mongosh
db.users.updateOne(
	{_id: ObjectId("6411ff792acf93a4a8994221")},
	{$push: {hobbies: {$each: ["Swimming", "Running", "Walking"]}}})
```

##### Remove a value 
```mongosh
db.users.updateOne(
	{_id: ObjectId("6411ff792acf93a4a8994221")}, 
	{$pull: {hobbies: "Running"}})
```
## Update Many

Remove all the `debts` (when the `debt` exists):
```mongosh
db.users.updateMany(
	{debt: {$exists: true}}, 
	{$unset: {debt: ""}})
```
# Delete

## DeleteOne

```mongosh
db.users.deleteOne({name: "Luce"})
```

## DeleteMany

Delete all `users` that don't have an age:
```mongosh
db.users.deleteMany({age: {$exists: false}})
```

## Delete All

To delete all `users` we can use `deleteMany` with an empty filter `{}`:
```mongosh
db.users.deleteMany({})
```


# Exercise
## Task

Suppose you have a MongoDB collection called `orders` that contains documents representing customer orders. Each order document has the following structure:
``` json
{
  "_id": ObjectId("..."),
  "customer_id": ObjectId("..."),
  "order_date": ISODate("..."),
  "items": [
    {
      "product_id": ObjectId("..."),
      "quantity": NumberInt("..."),
      "price": NumberDecimal("...")
    },
    ...
  ]
}
```

Write MongoDB queries to answer the following questions:

1.  What is the total revenue generated by all orders in the collection?
    
2.  Which customer has the highest total order value? What is their total order value?
    
3.  Which product has been ordered the most frequently? How many times has it been ordered?
    
4.  Which customers have ordered a particular product (e.g., with product_id = ObjectId("..."))? How many times has it been ordered by each customer?
    
5.  Which customers have placed an order in each month of the year? What are their names and email addresses?

## Solution

Before starting let's create a collection `orders` inside a database `db` :
```mongosh
use db

```

1. 