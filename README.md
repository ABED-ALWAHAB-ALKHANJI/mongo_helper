# MongoHelper Python Library

## Introduction
MongoHelper is a Python library that simplifies MongoDB operations by providing a convenient interface for common tasks.

## Installation
```bash
pip install mongo-helper
```
## Usage

from mongo_helper import MongoHelper

# Initialize MongoHelper
mongo_helper = MongoHelper(collection='your_collection', model=YourModelClass)

# Insert data
mongo_helper.insert({'key': 'value'})

# Find a document
document = mongo_helper.find_one_by('key', 'value')

# Update a document
mongo_helper.update_one_doc('key', 'value', new_key='new_value')

# Delete a document
mongo_helper.delete_one_doc('key', 'value')
Configuration
Make sure to set the following environment variables:

MONGO_DATABASE_URI: Your MongoDB database URI.
MONGO_DATABASE_NAME: Your MongoDB database name.
Contributing
...

License
...