Operator
--------
+ Query:
    - $exists: { field: { $exists: <boolean> } }
+ Aggregation:
    - $match: { $match: { <query> } }
    - $group: { $group: { \_id: <expression>, <field1>: { <accumulator1> : <expression1> }, ... } }

Methods
-------
- `db.collection.deleteMany()`: Removes all documents that match the filter from a collection.
