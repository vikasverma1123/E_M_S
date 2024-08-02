from django.contrib import admin
from EMS_App.models import  CollegeEvent, EventAdvisor, PartiesEvent, TechnicalEvent, WeddingEvent

from EMS_App.models import Contact

admin.site.register(Contact)
admin.site.register(EventAdvisor)
admin.site.register(WeddingEvent)
admin.site.register(PartiesEvent)
admin.site.register(CollegeEvent)
admin.site.register(TechnicalEvent)


