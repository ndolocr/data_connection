from django.db import models
from neomodel import(
    Relationship,
    StringProperty,
    StructuredNode,
    RelationshipTo,
    RelationshipFrom,
    UniqueIdProperty,
    IntegerProperty,
    ArrayProperty, 
    DateProperty
)
# Create your models here.

class TemporalData(StructuredNode):
    UID = UniqueIdProperty()
    ID_NO = StringProperty()
    ACC_NO = StringProperty()
    ACC_NAME = StringProperty()    
    CREATED_ON = DateProperty()