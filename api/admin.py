from django.contrib import admin
from .models import Donation, Donee, UserProfile

class DonationAdmin(admin.ModelAdmin):
    exclude = ["amount_donated"]

class DoneeAdmin(admin.ModelAdmin):
    pass

class UserProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Donation, DonationAdmin)
admin.site.register(Donee, DoneeAdmin)
admin.site.register(UserProfile, UserProfileAdmin)

admin.site.site_header = "Wicare administration"
admin.site.site_url = "https://sangwani-coder.github.io/wicare"
admin.site.site_title = "Wicare site admin"


