from django.http.response import Http404
from django.shortcuts import render
from django.shortcuts import render
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from saints.admin import LeaderAdmin

from saints.serializers import AccountabilityGroupsSerializer, AccountabilityLeaderSerializer, ActivitySerializer, AttendanceSerializer, CaseSerializer, FellowshipsSerializer, GateOneImageSerializer, HomeAltarSerializer, LeaderSerializer, ReportSerializer, SaintSerializer, SundayServiceSerializer, VisitorsSerializer
from .models import AccountabilityGroup, AccountabilityLeader, Case, GateOneImage, HomeAltar, Leader, Saint, Report, Attendance, Fellowship, Sunday_Service, Visitor, Activity


# class SaintAttendance(APIView):

#     def get_object(self, name):
#         try:
#             return Attendance.objects.get(saint=name)
#         except Attendance.DoesNotExist:
#             raise Http404

#     def get(self, name, format=None):
#         attendance = self.get_object(name)
#         serializer = AttendanceSerializer(Attendance)
#         return Response(serializer.data)

class SaintsView(generics.ListAPIView):
    queryset = Saint.objects.all()
    serializer_class = SaintSerializer
    permission_classes = [permissions.IsAuthenticated]


class CasesView(generics.ListAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    permission_classes = [permissions.IsAuthenticated]


class AttendancesView(generics.ListAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReportsView(generics.ListAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]


class VisitorsView(generics.ListCreateAPIView):
    queryset = Visitor.objects.all()
    serializer_class = VisitorsSerializer
    permission_classes = [permissions.IsAuthenticated]


class HomeAltarsView(generics.ListCreateAPIView):
    queryset = HomeAltar.objects.all()
    serializer_class = HomeAltarSerializer
    permission_classes = [permissions.IsAuthenticated]


class AccountabilityGroupsView(generics.ListCreateAPIView):
    queryset = AccountabilityGroup.objects.all()
    serializer_class = AccountabilityGroupsSerializer
    permission_classes = [permissions.IsAuthenticated]


class LeadersView(generics.ListCreateAPIView):
    queryset = Leader.objects.all()
    serializer_class = LeaderSerializer
    permission_classes = [permissions.IsAuthenticated]


class AccountabilityLeadersView(generics.ListCreateAPIView):
    queryset = AccountabilityLeader.objects.all()
    serializer_class = AccountabilityLeaderSerializer
    permission_classes = [permissions.IsAuthenticated]


class FellowshipsView(generics.ListCreateAPIView):
    queryset = Fellowship.objects.all()
    serializer_class = FellowshipsSerializer
    permission_classes = [permissions.IsAuthenticated]


class ActivitiesView(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]


class SundayservicesView(generics.ListCreateAPIView):
    queryset = Sunday_Service.objects.all()
    serializer_class = SundayServiceSerializer
    permission_classes = [permissions.IsAuthenticated]


class GAteOneImagesView(generics.ListCreateAPIView):
    queryset = GateOneImage.objects.all()
    serializer_class = GateOneImageSerializer
    permission_classes = [permissions.IsAuthenticated]


class GateOneImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GateOneImage.objects.all()
    serializer_class = GateOneImageSerializer
   # permission_classes=[permissions.AllowAny]
    permission_classes = [permissions.AllowAny]
