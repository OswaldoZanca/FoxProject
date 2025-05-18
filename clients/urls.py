from django.urls import path
from clients.views import (
    ClientListCreateView,
    ClientRetrieveUpdateDestroy
)


urlpatterns = [
    path(
        'clients/',
        ClientListCreateView.as_view(),
        name='client-list-create'
    ),
    path(
        'clients/<int:pk>/',
        ClientRetrieveUpdateDestroy.as_view(),
        name='client-detail'
    )
]
