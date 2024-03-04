from django.contrib import admin
from root.models import (
    Service,
    ContactUs,
    Testimonial,
    Team,
)

admin.site.register(Service)
admin.site.register(Team)
admin.site.register(Testimonial)
admin.site.register(ContactUs)