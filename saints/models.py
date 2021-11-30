import datetime
from typing import Match
from django.db import models
from django.contrib.auth.models import User


class AccountabilityLeader(models.Model):
    name = models.ForeignKey("Saint", on_delete=models.CASCADE)
    accountability_group = models.ForeignKey(
        "AccountabilityGroup", on_delete=models.CASCADE)

    def contact(self):
        return self.name.phone

    def __str__(self):
        return self.name.name


class FellowshipImage(models.Model):
    title = models.CharField(max_length=40, null=True)
    description = models.CharField(max_length=200)
    image = models.ImageField(
        upload_to="fellowships/images", blank=True, null=True)
    imageLink = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Leader(models.Model):
    name = models.ForeignKey("Saint", on_delete=models.CASCADE)
    department = models.ForeignKey("Department", on_delete=models.CASCADE)

    def __str__(self):
        return self.name.name


class Department(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Sunday_Service(models.Model):
    date = models.DateTimeField()
    duration = models.DurationField()
    banner = models.ImageField(upload_to="services/banners")
    report = models.FileField(upload_to="services/reports")
    visitors = models.ManyToManyField("Visitor")


class Saint(models.Model):
    name = models.CharField(max_length=100, unique=True)
    FIRST = "1"
    SECOND = "2"
    THIRD = "3"
    FOURTH = "4"
    GRADUATE = 'GR'
    YEAR_IN_SCHOOL_CHOICES = [
        (FIRST, "first"),
        (SECOND, 'second'),
        (THIRD, 'third'),
        (FOURTH, 'fourth'),
        (GRADUATE, 'graduate'),
        ("PR", 'professional'),
    ]

    accountability_group = models.ForeignKey(
        'AccountabilityGroup', on_delete=models.SET_NULL, null=True, blank=True)
    STABLE = "stable"
    MIDSTABLE = "mid-stable"
    UNSTABLE = "unstable"
    UNRESPONSIVE = "unresponsive"

    STABLILITY = [
        (STABLE, 'stable'),
        (MIDSTABLE, 'mid-stable'),
        (UNSTABLE, 'unstable'),
        (UNRESPONSIVE, 'unresponsive'),
    ]
    phone = models.CharField(max_length=15)
    residence = models.CharField(max_length=50)
    stability = models.CharField(max_length=15,
                                 choices=STABLILITY,
                                 default=UNSTABLE,)
    gender = models.CharField(max_length=10, choices=[
        ('sister', 'sister'), ("brother", "brother")], default='brother')
    year = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FIRST,
    )
    departments = models.ManyToManyField("Department")

    home_altar = models.ForeignKey(
        'HomeAltar', on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    New = "new"
    Faithful = "faithful"
    Leader = "leader"

    SaintType = [
        (New, 'New  beleiver'),
        (Faithful, 'Faihful'),
        (Leader, 'Leader'),
        ("pastor", 'Pastor'),
        ("seniorpastor", 'Senior Pastor'),
        ("reverend", "Reverend"),
        ('bishop', "Bishop")
    ]
    saint_level = models.CharField(
        max_length=13, choices=SaintType, default=Faithful)
    married = models.BooleanField()
    child = models.BooleanField()
    attendedServices = models.ManyToManyField(
        "Sunday_Service", blank=True)

    def status(self):
        return len(self.attendedServices)

    def __str__(self):
        return self.name


class ActivityImage(models.Model):
    image = models.ImageField(
        upload_to="reports/images", null=True, blank=True)
    note = models.CharField(max_length=50)
    eventType = models.CharField(max_length=30, choices=[("fellowship", "Fellowship"),
                                                         ("activity", "Activity"),
                                                         ("service", "Service")
                                                         ])
    fellowshipA = models.ForeignKey(
        'Fellowship', on_delete=models.CASCADE, verbose_name="fellowship", null=True, blank=True)
    Activity = models.ForeignKey(
        'Activity', on_delete=models.CASCADE, verbose_name="activity", null=True, blank=True)
    Service = models.ForeignKey(
        'Sunday_Service', on_delete=models.CASCADE, verbose_name="service", null=True, blank=True)

    def event(self):
        if self.Activity != None:
            return "Activity"
        if self.fellowshipA != None:
            return "Fellowship"
        if self.Service != None:
            return "Service"

    def __str__(self):
        return self.image


class Fellowship(models.Model):
    name = models.CharField(max_length=30)
    # fellowshipreport = models.ForeignKey(
    #     "Report", on_delete=models.CASCADE, null=True)
    image = models.ImageField(
        upload_to="reports/images", null=True, blank=True)
    location = models.CharField(max_length=20, null=True)
    date = models.DateField('')
    Time = models.TimeField(null=True)
    duration = models.DurationField()

    def attendances(self):
        return Attendance.objects.filter(fellowship=self)

    def __str__(self):
        return str(self.name) + str(self.date)


class Activity(models.Model):
    activities = [('washingOfmaterials', 'Washing Of Materials'),
                  ("evangelism", "Evangelism"), ("other", 'Other Activities')]
    type = models.CharField(max_length=30, choices=activities, default='other')
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=20, null=True)
    image = models.ImageField(upload_to="reports/images", null=True)
    date = models.DateField('')
    Time = models.TimeField(null=True)
    duration = models.DurationField()

    def __str__(self):
        return str(self.name) + str(self.date)


class Attendance(models.Model):
    fellowship = models.ForeignKey(
        'Fellowship', on_delete=models.CASCADE, blank=True)
    activity = models.ForeignKey(
        "Activity", on_delete=models.CASCADE, blank=True)
    saint = models.ForeignKey('Saint', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.fellowship) + 'Attendance'


class Report(models.Model):
    fellowshipA = models.ForeignKey(
        'Fellowship', on_delete=models.CASCADE, verbose_name="fellowship", null=True)

    date = models.DateField(null=True)
    title = models.CharField(max_length=100)
    report = models.TextField()
    document = models.FileField(upload_to="reports/docs", blank=True)
    author = models.ForeignKey('Saint', on_delete=models.CASCADE)
    images = models.ManyToManyField("FellowshipImage")

    def __str__(self):
        return str(self.fellowshipA) + " " + 'Report'


class AccountabilityGroup(models.Model):
    group_number = models.IntegerField(unique=True)

    leader = models.ForeignKey(
        'Saint', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.group_number)


class Visitor(models.Model):
    name = models.CharField(max_length=100)
    home_altar = models.ForeignKey(
        'HomeAltar', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField()
    contact = models.CharField(max_length=15)
    fellowship = models.ForeignKey(
        'Fellowship', on_delete=models.CASCADE, null=True)
    DeptOfInterest = [
        ('worship', 'worship'),
        ('ushering', 'ushering'),
        ('violin', 'violin'),
        ('keyboard', 'keyboard'),
        ('decoration', 'decoration'),
        ('hospitality', 'hospitality'), ('security', 'security'),

    ]
    interestedDepartment = models.CharField(
        max_length=20, choices=DeptOfInterest)

    def __str__(self):
        return self.name


class HomeAltar(models.Model):
    name = models.CharField(max_length=40)
    Senior_Pastor = models.CharField(max_length=30)
    contact = models.IntegerField()
    region = models.CharField(max_length=30)

    def __str__(self):
        return self.name


def year_choices():
    return [(r, r) for r in range(1984, datetime.date.today().year+1)]


def current_year():
    return datetime.date.today().year


class GateOneImage(models.Model):
    caserel = models.ForeignKey(
        "Case", on_delete=models.SET_NULL, null=True, verbose_name="Case")
    dateofRecording = models.DateTimeField()
    image = models.ImageField(upload_to="sick/gateoneimages", null=True)

    def __str__(self):
        return str(self.caserel.name)


class Case(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=12, choices=[
        ('sister', 'sister'), ("brother", "brother")], default='brother')
    YearOfBirth = models.DateField()
    image = models.ImageField(upload_to="gateone/shorts", null=True)
    StartOfCondition = models.DateField()
    residence = models.CharField(max_length=25)
    condition = models.CharField(
        max_length=80, verbose_name="Sickness/Disability")
    recorded = models.BooleanField(null=True)
    contact = models.CharField(max_length=14, blank=True, null=True)
    videoLink = models.URLField(null=True, blank=True)

    def age(self):
        return datetime.date.today() - self.YearOfBirth

    def __str__(self):
        return self.name
