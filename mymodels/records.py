from django.db import models

from djangotoolbox.fields import ListField
from djangotoolbox.fields import DictField
# Create your models here.
    
class Hospital_Record(models.Model):
    record =DictField()
    
    def getbyfields(self,**kwargs):
        # to filter records
        return {}
        
    def getdocuments(self,*args,**kwargs):
        # to get record from collection