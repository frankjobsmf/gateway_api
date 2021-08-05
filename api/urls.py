#django urls
from django.urls import path

#SERVICES -> NOTE
from .services.Note.NoteService import (
    #list
    ListNotesByUserIdAPI,
    #list note by id
    ListNoteById,
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
    #refresh token
    RefreshTokenAPI,
)

urlpatterns = [
    #NOTE #################################################
    #list
    path(
        'notes-userid', 
        ListNotesByUserIdAPI.as_view()
    ),
    #list note by id
    path(
        'note-id/id=<int:id>', 
        ListNoteById.as_view()
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
    #refresh token
    path(
        'refresh-token',
        RefreshTokenAPI.as_view(),
    ),
]
