from django.contrib import admin
from .models import PaymentData
import csv
from django.http import HttpResponse


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(
            meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field)
                                   for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"




@admin.register(PaymentData)
class PaymentAdmin(admin.ModelAdmin, ExportCsvMixin):
    actions = ["export_as_csv"]
    list_display = ('porderid', 'pmid', 'ptxnid', 'ptxnamount', 'ppaymentmode', 'pcurrency',
                    'ptxndate', 'pstatus', 'prespcode', 'prespmeg', 'pgatewayname', 'pbanktxnid', 'pbankname')
