from django.contrib import admin
from .models import PasanakuGroup, Member, Round, Payment, Invitation

admin.site.register(PasanakuGroup)
admin.site.register(Member)
admin.site.register(Round)
admin.site.register(Payment)
admin.site.register(Invitation)

