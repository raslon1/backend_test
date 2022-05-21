from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from mobil_api.models import POS, Visit
from mobil_api.serializers import POSSerializer, VisitSerializer


class POSView(ListAPIView):
    serializer_class = POSSerializer

    # Список Торговых точек привязанных к переданному номеру телефона. Сдалал ГЕТ заппросом
    # http://localhost:8000/api/pos/?phone=8XXXXXXXXXX
    def get_queryset(self):
        if phone := self.request.query_params.get("phone", None):
            queryset = POS.objects.filter(worker__phone_num=phone)
            if queryset:
                return queryset
            else:
                raise NotFound("Worker not found")
        raise NotFound("Argument 'phone=' not found")


class VisitView(ListAPIView):
    def post(self, requests):
        worker_phone = self.request.data.get("phone")
        pos_pk = self.request.data.get("pos_id")
        lat = self.request.data.get("lat")
        long = self.request.data.get("long")


        if not worker_phone:
            return Response({"detail": "No phone number"})
        if not pos_pk:
            return Response({"detail": "No POS id"})
        if not lat or not long:
            return Response({"detail": "No lat or long"})

        pos_data = POS.objects.filter(pk=pos_pk, worker__phone_num=worker_phone).first()
        if pos_data:
            new_visit = Visit(pos=pos_data, lat=lat, long=long)
            new_visit.save()
            serializer = VisitSerializer(new_visit, many=False)
            return Response(serializer.data)

        return Response({"detail": "the employee is not tied to the outlet"})
