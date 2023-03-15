
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

Assume you have a database named "store" with a collection named "products". Each document in the "products" collection has the following fields:

-   _id (ObjectID)
-   name (string)
-   price (number)
-   category (string)
-   stock (number)
-   reviews (array of objects with fields "username" and "comment")

0. Create the database and the collection

1.  Insert three documents into the "products" collection with the following fields:
- ```name: "Product A", price: 10, category: "Category 1", stock: 20, reviews: []```
- ```name: "Product B", price: 15, category: "Category 1", stock: 10, reviews: [{username: "User 1", comment: "Good product"}]```
- ```name: "Product C", price: 20, category: "Category 2", stock: 5, reviews: [{username: "User 2", comment: "Great product"}, {username: "User 3", comment: "Not worth the price"}]```


2.  Write a query to find all products in "Category 1" with a price greater than 12.
    
3.  Write a query to update the stock of "Product A" to 30.
    
4.  Write a query to add a new review to "Product B" with username "User 2" and comment "Average product".
    
5.  Write a query to remove the review with username "User 3" from "Product C".
    
6.  Write a query to find the average price of products in each category.
    
7.  Write a query to find the products with the highest and lowest stock levels.
    
8.  Write a query to find the number of products in each category with at least one review.
    
9.  Write a query to find the top 5 most reviewed products.
    
10.  Write a query to find all products where the sum of the length of all review comments is greater than 50.

## Solution

0. Create the database `store` and the collection `products`:
```mongosh
use store
db.createCollection("products")
```

1.  Insert three products into the collection:
```mongosh
db.products.insertMany([
	{name: "Product A", price: 10, category: "Category 1", stock: 20, reviews: []},
	{name: "Product B", price: 15, category: "Category 1", stock: 10, reviews: [{username: "User 1", comment: "Good product"}]},
	{name: "Product C", price: 20, category: "Category 2", stock: 5, reviews: [{username: "User 2", comment: "Great product"}, {username: "User 3", comment: "Not worth the price"}]}])
```

And let's verify everything was added correctly:
```mongosh
db.products.find()
```

2.  Write a query to find all products in "Category 1" with a price greater than 12:
```mongosh
db.products.find({category: "Category 1", price: {$gt: 12}})
```

3.  Write a query to update the stock of "Product A" to 30.
```mongosh
db.products.updateOne( {name: "Product A"}, {$set: {stock: 30}})
```

4.  Write a query to add a new review to "Product B" with username "User 2" and comment "Average product".
```mongosh
db.products.updateOne(
	{name: "Product B"},
	{$push: {reviews: {username: "User 2", comment: "Average Product"}}})
```

5.  Write a query to remove the review with username "User 3" from "Product C".
```mongosh
db.products.updateOne(
	{name: "Product C"},
	{$pull: {reviews: {username: "User 3"}}}
)
```

6.  Write a query to find the average price of products in each category.
``` mongosh
db.products.aggregate([
  {
    $group: {
      _id: "$category",
      avgPrice: { $avg: "$price" }}}])
```

7.  Write a query to find the products with the highest and lowest stock levels.
```mongosh
db.products.aggregate([
  { $sort: { stock: 1 } }, // sort by stock in ascending order
  { $limit: 1 }, // return the document with the lowest stock
], { collation: { locale: "en_US", numericOrdering: true } })
```

8.  Write a query to find the number of products in each category with at least one review.
```mongosh
db.products.aggregate([
  {
    $match: {
      reviews: { $ne: [] }
    }
  },
  {
    $group: {
      _id: "$category",
      count: { $sum: 1 }
    }
  }
])
```

9.  Write a query to find the top 3 most reviewed products.
```mongosh
db.products.aggregate([
  {
    $project: {
      name: 1,
      reviewsCount: { $size: "$reviews" }
    }
  },
  {
    $sort: { reviewsCount: -1 }
  },
  {
    $limit: 3
  }
])
```

This query uses the `$project` stage to create a new field called `reviewsCount` that contains the number of reviews for each product. It then sorts the products by the `reviewsCount` field in descending order using the `$sort` stage. Finally, it limits the output to the top 3 products using the `$limit` stage.

The result will be a list of documents that contain the name of the product and the number of reviews it has, sorted in descending order by the number of reviews, with only the top 3 products.

10.  Write a query to find all products where the sum of the length of all review comments is greater than 10.
```mongosh
db.products.find({
  $where: function() {
    var sum = 0;
    this.reviews.forEach(function(review) {
      sum += review.comment.length;
    });
    return sum > 10;
  }
})
```

This query uses the `$where` operator to execute a JavaScript function for each document in the `products` collection. The function iterates over the `reviews` array of each document, summing the length of all review comments. If the sum is greater than 50, the function returns `true`, indicating that the document should be included in the result set.