from .models import AccountabilityGroup, AccountabilityLeader, Case, GateOneImage, HomeAltar, Leader, Saint, Report, Attendance, Fellowship, Sunday_Service, Visitor, Activity
from rest_framework import serializers


class SaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saint
        fields = '__all__'


class FellowshipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fellowship
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'


class SundayServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sunday_Service
        fields = '__all__'


class VisitorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = '__all__'


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'


class LeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leader
        fields = '__all__'


class AccountabilityLeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountabilityLeader
        fields = '__all__'


class AccountabilityGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountabilityGroup
        fields = '__all__'


class HomeAltarSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeAltar
        fields = "__all__"


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = "__all__"


class GateOneImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GateOneImage
        fields = "__all__"
