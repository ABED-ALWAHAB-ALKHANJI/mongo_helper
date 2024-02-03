<!-- Header with Logo and Library Name -->
<div align="center">
  <img src="https://doctor-devops.com/wp-content/uploads/2024/02/logo.png" alt="MongoHelper Logo" width="150" height="100">
  <h1 style="display: inline-block; color: #3498db; vertical-align: super;">MongoHelper</h1>
</div>

<!-- Introduction Section -->
## Introduction
MongoHelper is a Python library that simplifies MongoDB operations by providing a convenient interface for common tasks.

<!-- Installation Section -->
## Installation
```bash
pip install mongo-helper
```
## Usage
Make sure to set the following environment variables:

MONGO_DATABASE_URI: Your MongoDB database URI.
MONGO_DATABASE_NAME: Your MongoDB database name.

Then import it in you project
```
from mongo_helper import MongoHelper
```
# Initialize MongoHelper
```
mongo_helper = MongoHelper(collection='your_collection', model=YourModelClass)
```
# Insert data
```
mongo_helper.insert({'key': 'value'})
```
# Find a document
```
document = mongo_helper.find_one_by(find_by=yourKey, value=yourValue)
```
# Find a document Greater Than
```
documents = mongo_helper.find_greater_than(find_by=yourKey, greater_than=yourValue,greater_or_equal=False)
```
# Find a document Less Than
```
documents = mongo_helper.find_greater_than(find_by=yourKey, less_than=yourValue,less_or_equal=False)
```
# Find a document Return Only Specific Fields
```
documents = mongo_helper.find_specific_fields(find_by=yourKey, equal_to=yourValue,selected_field=['key1','key2'])
```
# Find a documents Return as Model Objects
```
documents = mongo_helper.query()
```
# Update a document
```
mongo_helper.update_one_doc('key', 'value', new_key='new_value')
```
# Delete a document
```
mongo_helper.delete_one_doc('key', 'value')
```
## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
This library is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
