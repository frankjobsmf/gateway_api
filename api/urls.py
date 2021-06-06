#django urls
from django.urls import path

#SERVICES -> NOTE
from .services.Note.NoteService import (
    #list
    ListNotesByUserIdAPI,
    #add
    AddNoteAPI,
    #update
    UpdateNoteAPI,
    #delete
    DeleteNoteAPI,
)

#SERVICES -> USER
from .services.User.UserService import (
    #register
    RegisterAPI,
    #login
    LoginAPI,
)

urlpatterns = [
    #NOTE #################################################
    #list
    path(
        'notes-userid', 
        ListNotesByUserIdAPI.as_view()
    ),
    #add
    path(
        'add', 
        AddNoteAPI.as_view()
    ),
    #update
    path(
        'update/id=<int:id>',
        UpdateNoteAPI.as_view()
    ),
    #delete
    path(
        'delete/id=<int:id>',
        DeleteNoteAPI.as_view(),
    ),

    #USER #################################################
    #register
    path(
        'register',
        RegisterAPI.as_view(),
    ),
    #login
    path(
        'login',
        LoginAPI.as_view(),
    ),
]
