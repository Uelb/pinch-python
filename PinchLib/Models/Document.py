# -*- coding: utf-8 -*-

"""
   PinchLib.Models.Document
 
   This file was automatically generated for Pinch by APIMATIC v2.0 ( https://apimatic.io ) on 06/01/2016
"""
from PinchLib.Models.BaseModel import BaseModel

class Document(BaseModel):

    """Implementation of the 'Document' model.

    TODO: type model description here.

    Attributes:
        url (string): Where to retrieve the document
        thumb_url (string): If possible, a thumbnail of the document
        id (int): TODO: type description here.
        name (string): TODO: type description here.

    """

    def __init__(self, 
                 url = None,
                 thumb_url = None,
                 id = None,
                 name = None):
        """Constructor for the Document class"""
        
        # Initialize members of the class
        self.url = url
        self.thumb_url = thumb_url
        self.id = id
        self.name = name

        # Create a mapping from Model property names to API property names
        self.names = {
            "url": "url",
            "thumb_url": "thumb_url",
            "id": "id",
            "name": "name",
        }

    @classmethod
    def from_dictionary(cls, 
                        dictionary):
        """Creates an instance of this model from a dictionary
       
        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.
            
        Returns:
            object: An instance of this structure class.
            
        """

        if dictionary == None:
            return None
        else:	
            # Extract variables from the dictionary
            url = dictionary.get("url")
            thumb_url = dictionary.get("thumb_url")
            id = dictionary.get("id")
            name = dictionary.get("name")
            # Return an object of this model
            return cls(url,
                       thumb_url,
                       id,
                       name)
