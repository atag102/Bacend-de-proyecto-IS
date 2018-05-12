from django.db import models
from mongoengine import Document, fields

# Create your models here.

class usuario(Document):

	Cuenta=fields.StringField()
	Clave=fields.StringField()
	Correo=fields.StringField()
	
class verificacion(Document):

	VF=fields.StringField()
