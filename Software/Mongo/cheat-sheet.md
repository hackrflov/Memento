Operator
--------
+ Query:
    - $exists: { field: { $exists: <boolean> } }
+ Update:
    - $set: { $set: { <field1>: <value1>, ... } }
    - $unset: { $unset: { <field1>: "", ... } }
+ Aggregation:
    - $match: { $match: { <query> } }
    - $group: { $group: { \_id: <expression>, <field1>: { <accumulator1> : <expression1> }, ... } }

Methods
-------
- `db.collection.deleteMany()`: Removes all documents that match the filter from a collection.
