import os

import pymongo
from typing import Type, List


class MongoHelper:
    """
       A helper class for simplifying MongoDB operations in Python.

       Attributes:
           uri (str): The MongoDB database URI.
           databaseName (str): The name of the MongoDB database.
           client (pymongo.MongoClient): The MongoDB client instance.
           py_mongo_db (pymongo.database.Database): The MongoDB database instance.

       Args:
           collection (str): The name of the MongoDB collection to work with.
           model (Type): The custom model class to use for data mapping.
       """
    uri = os.environ.get("MONGO_DATABASE_URI")
    databaseName = os.environ.get("MONGO_DATABASE_NAME")
    if uri is None or databaseName is None:
        raise 'Please Set MONGO_DATABASE_URI And MONGO_DATABASE_NAME in ENV'
    client = pymongo.MongoClient(uri)
    py_mongo_db = client[databaseName]

    def __init__(self, collection=None, model=None):
        """
                Initialize the MongoHelper instance.

                Args:
                    collection (str): The name of the MongoDB collection to work with.
                    model (Type): The custom model class to use for data mapping.
        """
        self.collection = collection

        self.model = model

    def insert(self, data: dict):
        """
                Insert a document into the MongoDB collection.

                Args:
                    data (dict): The data to be inserted.
        """
        self.py_mongo_db[self.collection].insert_one(data)

    def find_one_by(self, find_by: str, value):
        """
                Find a document in the MongoDB collection based on a specific field and value.

                Args:
                    find_by (str): The field to search for.
                    value: The value to search for in the specified field.

                Returns:
                    dict: The found document.
        """
        return self.py_mongo_db[self.collection].find_one({find_by: value})

    def find_greater_than(self, find_by: str, greater_than, greater_or_equal: bool = False):
        """
                Find a document where the specified field is greater than a given value.

                Args:
                    find_by (str): The field to compare.
                    greater_than: The value to compare against.
                    greater_or_equal (bool): If True, include documents with values equal to `greater_than`.

                Returns:
                    dict: The found document.
        """
        if greater_or_equal:
            return self.py_mongo_db[self.collection].find_one({find_by: {"$gte": greater_than}})
        else:
            return self.py_mongo_db[self.collection].find_one({find_by: {"$gt": greater_than}})

    def find_less_than(self, find_by: str, less_than, less_or_equal: bool = False):
        """
            Find a document in the MongoDB collection where the specified field is less than a given value.

            Args:
                find_by (str): The field to compare.
                less_than: The value to compare against.
                less_or_equal (bool, optional): If True, include documents with values equal to `less_than`.

            Returns:
                dict: The found document or None if no matching document is found.
        """
        if less_or_equal:
            return self.py_mongo_db[self.collection].find_one({find_by: {"$lte": less_than}})
        else:
            return self.py_mongo_db[self.collection].find_one({find_by: {"$lt": less_than}})

    def find(self, query=None):
        """
           Retrieve documents from the MongoDB collection based on the specified query.

           Args:
               query (dict, optional): The query conditions. If None, retrieves all documents.

           Returns:
               pymongo.cursor.Cursor: A cursor to iterate over the documents matching the specified query.
           """

        return self.py_mongo_db[self.collection].find(query)

    def find_one(self, query):
        """
            Retrieve a single document from the MongoDB collection based on the specified query.

            Args:
                query (dict): The query conditions.

            Returns:
                dict: The found document or None if no matching document is found.
        """
        return self.py_mongo_db[self.collection].find_one(query)

    def find_specific_fields(self, find_by: str, equal_to: str, selected_field: list):
        """
            Retrieve documents from the MongoDB collection with specific fields based on a condition.

            Args:
                find_by (str): The field to use for the retrieval condition.
                equal_to: The value to match for the retrieval condition.
                selected_field (list): List of fields to include in the result.

            Returns:
                pymongo.cursor.Cursor: A cursor to iterate over the documents matching the specified condition
                                      with only the selected fields.

            Raises:
                ValueError: If the selected_field list is empty.
        """

        if not selected_field:
            raise ValueError("Please make sure that selected_field is not empty")

        returned_fields = {field: 1 for field in selected_field}
        query = {find_by: equal_to} if find_by is not None and equal_to is not None else {}

        return self.py_mongo_db[self.collection].find(query, returned_fields)

    def update_one_doc(self, update_where, equal_value, **kwargs):
        """
            Update a single document in the MongoDB collection based on a specified field and value.

            Args:
                update_where (str): The field to use for the update condition.
                equal_value: The value to match for the update condition.
                **kwargs: Keyword arguments representing the fields and values to update.

            Returns:
                pymongo.results.UpdateResult: The result of the update operation, including the number of modified documents.
        """
        query = {update_where: equal_value}
        updated_doc = {"$set": {**kwargs}}

        return self.py_mongo_db[self.collection].update_one(query, updated_doc)

    def update_many_doc(self, update_where, equal_value, **kwargs):
        """
            Update multiple documents in the MongoDB collection based on a specified field and value.

            Args:
                update_where (str): The field to use for the update condition.
                equal_value: The value to match for the update condition.
                **kwargs: Keyword arguments representing the fields and values to update.

            Returns:
                pymongo.results.UpdateResult: The result of the update operation, including the number of modified documents.
        """
        query = {update_where: equal_value}
        updated_docs = {"$set": {**kwargs}}

        return self.py_mongo_db[self.collection].update_many(query, updated_docs)

    def delete_one_doc(self, delete_where, equal_value):
        """
            Delete a single document from the MongoDB collection based on a specified field and value.

            Args:
                delete_where (str): The field to use for the deletion condition.
                equal_value: The value to match for the deletion condition.

            Returns:
                pymongo.results.DeleteResult: The result of the delete operation, including the number of deleted documents.
        """
        return self.py_mongo_db[self.collection].delete_one({delete_where: equal_value})

    def drop_collection(self):
        """
            Drop (delete) the entire MongoDB collection associated with the MongoHelper instance.

            Returns:
                dict: A dictionary containing information about the operation, including success or failure.
        """
        return self.py_mongo_db[self.collection].drop()

    def query(self, condition: dict = None, order_by: str = None, ascending: bool = True,
              no_cursor_timeout: bool = False, first_record: bool = False, returned_fields: list = None,
              page_number: int = 1, page_size: int = 100):
        """
        Query the MongoDB collection with optional conditions and sorting.

        Args:
            condition (dict): The query conditions.
            order_by (str): The field to sort by.
            ascending (bool): If True, sort in ascending order; otherwise, in descending order.

            no_cursor_timeout (bool): If True, the cursor will not expire.
            first_record (bool): If True, return only the first record.
            returned_fields (List[str]): List of fields to be returned from the database.
            page_number (int): The page number to retrieve (default is 1).
            page_size (int): The number of documents per page (default is 100).

        Returns:
            list or dict: List of documents or a single document based on the specified criteria.
        """

        query_params = {}

        if condition is not None:
            query_params['filter'] = condition
        if returned_fields is not None:
            projection = {field: 1 for field in returned_fields}
            query_params['projection'] = projection
        if no_cursor_timeout:
            query_params['no_cursor_timeout'] = True

        if order_by is not None:
            sort_order = pymongo.ASCENDING if ascending else pymongo.DESCENDING
            if order_by == "id":
                order_by = "_id"
            query_params['sort'] = [(order_by, sort_order)]

        skip_count = (page_number - 1) * page_size

        query_result = self.py_mongo_db[self.collection].find(**query_params).skip(skip_count).limit(page_size)
        result_list = []
        for record in query_result:
            record["id"] = record.pop("_id")
            result_list.append(self.model(**record))
        if not result_list:
            return None
        if first_record:
            return result_list[0]

        return result_list

    def get_document_count(self):
        """
        Get the total number of documents in the MongoDB collection.

        Returns:
            int: The total number of documents.
        """
        return self.py_mongo_db[self.collection].count_documents({})
