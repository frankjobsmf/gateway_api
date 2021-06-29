#python
from datetime import datetime
now = datetime.now()

#requests
import requests

#PyJWT
import jwt

#rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

#constante para el microservicio note_service
URL_NOTE_API = 'http://127.0.0.1:8002/note/'

#serializers
from .noteSerializers import (
    #add
    AddNoteSerializer,
    #update
    UpdateNoteSerializer,
)

#list
class ListNotesByUserIdAPI(APIView):

    def get(self, request, *args, **kwargs):

        #cabecera de la peticion
        header_authorization = request.headers['Authorization']

        try:
            #decodificando el token que viene el Headers -> Authorization
            decoded_jwt = jwt.decode(header_authorization, 'secret-note-app', algorithms=['HS256'])

            user_id = decoded_jwt['user']['id']

            #preparando endpoint para notes-userid
            endpoint_note = 'notes-userid/id=' + str(user_id)
            
            #llamando a la api de notas por usuario id del microservicio note_servicio
            notes_get = requests.get( URL_NOTE_API + endpoint_note )
            notes = notes_get.json()
            
            return Response({
                "notes": notes['notes'],
                "status_code": notes['status_code']
            })
        
        except jwt.exceptions.InvalidTokenError:
            return Response({
                "message": "El token no es valido",
                "status_code": status.HTTP_401_UNAUTHORIZED
            })

#list note by id
class ListNoteById(APIView):
    def get(self, request, *args, **kwargs):

        #cabecera de la peticion
        header_authorization = request.headers['Authorization']

        try:
            # #decodificando el token que viene el Headers -> Authorization
            jwt.decode(header_authorization, 'secret-note-app', algorithms=['HS256'])

            #preparando endpoint para notes-userid
            endpoint_note = 'note-id/id=' + str(kwargs['id'])
            
            #llamando a la api de notas por usuario id del microservicio note_servicio
            note_get = requests.get( URL_NOTE_API + endpoint_note )
            note = note_get.json()
            
            return Response({
                "note": note['note'],
                "status_code": note['status_code']
            })
        
        except jwt.exceptions.InvalidTokenError:
            return Response({
                "message": "El token no es valido",
                "status_code": status.HTTP_401_UNAUTHORIZED
            })

#add
class AddNoteAPI(APIView):
    serializer_class = AddNoteSerializer   

    def post(self, request):

        #cabecera de la peticion
        header_authorization = self.request.headers['Authorization']        
        
        try:

            #decodificando el token que viene el Headers -> Authorization
            decoded_jwt = jwt.decode(header_authorization, 'secret-note-app', algorithms=['HS256'])

            user_id = decoded_jwt['user']['id']

            #validamos si los parametros que nos envian son iguales al serializador
            serializer = AddNoteSerializer(data=request.data)

            if serializer.is_valid():
                #endpoint para enviar diccionario de note
                endpoint_note = 'add'

                #estructura de note
                note_dict = {
                    'user_id': user_id,
                    'title': serializer.validated_data['title'],
                    'content': serializer.validated_data['content'],
                    'date': str(now.date())
                }
                
                #haciendo el post a la url del note_service
                note_resp = requests.post( URL_NOTE_API + endpoint_note, json={ 'note_dict': note_dict }).json()
                
                return Response({
                    "message": note_resp['message'],
                    "status_code": note_resp['status_code']
                })
                #
            return Response({
                "status_code": status.HTTP_400_BAD_REQUEST
            })
            #
        except jwt.exceptions.InvalidTokenError:
            return Response({
                "message": "El token no es valido",
                "status_code": status.HTTP_401_UNAUTHORIZED
            })
        
#update
class UpdateNoteAPI(APIView):
    
    serializer_class = UpdateNoteSerializer
    
    def put(self, request, *args, **kwargs):
        
        #cabecera de la peticion
        header_authorization = self.request.headers['Authorization']

        try:

            #decodificando el token que viene el Headers -> Authorization
            decoded_jwt = jwt.decode(header_authorization, 'secret-note-app', algorithms=['HS256'])


            #endpoint para actualizar la nota, debemos indicar el id de la nota que queremos actualizar
            endpoint_note = 'update/id=' + str(kwargs['id'])
        
            #validamos el serializador que nos han mandado
            serializer = UpdateNoteSerializer(data=request.data)
        
            if serializer.is_valid():
            
                #estructura de note
                note_dict = {
                    'title': serializer.validated_data['title'],
                    'content': serializer.validated_data['content']
                }
                
                #haciendo el put a la url del note_service
                note_resp = requests.put( URL_NOTE_API + endpoint_note, json={ 'note_dict': note_dict })
                note = note_resp.json()
                
                return Response({
                    "message": note['message'],
                    "status_code": note['status_code']
                })
                #
            return Response({
                "status_code": status.HTTP_400_BAD_REQUEST
            })
            #
        except jwt.exceptions.InvalidTokenError:
            return Response({
                "message": "El token no es valido",
                "status_code": status.HTTP_401_UNAUTHORIZED
            })
        

        
#delete
class DeleteNoteAPI(APIView):
    
    def delete(self, request, *args, **kwargs):
        
        #cabecera de la peticion
        header_authorization = self.request.headers['Authorization']

        try:

            #decodificando el token que viene el Headers -> Authorization
            decoded_jwt = jwt.decode(header_authorization, 'secret-note-app', algorithms=['HS256'])
            
            #endpoint para actualizar la nota, debemos indicar el id de la nota que queremos actualizar
            endpoint_note = 'delete/id=' + str(kwargs['id'])

            #haciendo el delete a la url del note_service
            note_resp = requests.delete( URL_NOTE_API + endpoint_note )
            note = note_resp.json()
            
            return Response({
                "message": note['message'],
                "status_code": note['status_code']
            })
            #
        except jwt.exceptions.InvalidTokenError:
            return Response({
                "message": "El token no es valido",
                "status_code": status.HTTP_401_UNAUTHORIZED
            })
