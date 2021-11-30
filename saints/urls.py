from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('saints/', SaintsView.as_view()),
    path('visitors/', VisitorsView.as_view()),
    path('gateoneimages/<int:pk>/', GateOneImageDetail.as_view()),
    path('reports/', ReportsView.as_view()),
    path('attendances/', AttendancesView.as_view()),
    path('fellowships/', FellowshipsView.as_view()),
    path('activities/', ActivitiesView.as_view()),
    path('accountabilityleaders/', AccountabilityLeadersView.as_view()),
    path('accountabilitygroups/', AccountabilityGroupsView.as_view()),
    path('leaders/', LeadersView.as_view()),
    path('homealtars/', HomeAltarsView.as_view()),
    path('cases/', CasesView.as_view()),
    path('gateoneimages/', GAteOneImagesView.as_view()),


]
