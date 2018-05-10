from django.shortcuts import render
from mongoengine import Document, fields
from django.views.generic import TemplateView
from usuario.models import usuario,verificacion
import json
from pymongo import MongoClient



# Create your views here.

class login(TemplateView):

	#Registrar una persona al sistema
	#---------------------------------------------------------------------------------------------------
	with open('usuario/AJSON2.json','r') as file:
		data=json.load(file)
		usuario.objects.create(Cuenta=data['Cuenta'],Clave=data['Clave'],Correo=data['Correo'])
	#---------------------------------------------------------------------------------------------------

	#Login verificar si un usuario esta registrado en el sistema
	#---------------------------------------------------------------------------------------------------
		mongoClient=MongoClient('localhost',27017)
		db=mongoClient.BDPI
		collection=db.usuario
		if(collection.find({"Cuenta":data['Cuenta'],"Clave":data['Clave'],"Correo":data['Correo']})):
			verificacion.objects.create(VF="V")
		else:
			verificacion.objects.create(VF="F")
	#---------------------------------------------------------------------------------------------------
	template_name='usuario/login.html'
