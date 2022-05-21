from django.contrib import admin

# Register your models here.
from mobil_api.models import Worker, Visit, POS


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ["name", "phone_num"]
    list_filter = ["name"]
    search_fields = ["name"]


@admin.register(POS)
class POSAdmin(admin.ModelAdmin):
    list_display = ["pos_name"]
    list_filter = ["pos_name"]
    search_fields = ["pos_name"]


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ["date", "pos_name", "worker_name", "lat", "long"]
    list_filter = ["pos"]
    search_fields = ["pos__pos_name", "pos__worker__name"]

    def pos_name(self, obj):
        return obj.pos.pos_name

    def worker_name(self, obj):
        return obj.pos.worker.name
