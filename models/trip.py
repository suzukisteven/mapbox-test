from models.base_model import BaseModel
import peewee as pw

class Trip(BaseModel):
    longitude = pw.DecimalField(unique=False, null=True)
    latitude = pw.DecimalField(unique=False, null=True)
    address = pw.CharField(unique=True, null=True)