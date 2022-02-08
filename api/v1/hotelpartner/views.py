from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from hotelpartner.models import HotelChain
from . import serializer

class HotelChainAPI(ListCreateAPIView):
    querySet = HotelChain.objects.all()
    serializer_class = serializer.HotelChainSerializer
    permissions_class = (AllowAny,)

    def get_queryset(self):
        return HotelChain.objects.all()
        # return Response({"status": True,
        #                  "message": "List Hotel chain",
        #                  "data": HotelChain.objects.all()
        #                  })
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"status": True,
                         "message": "Hotel chain added!",
                         "data": serializer.data
                         }, status=status.HTTP_201_CREATED, headers=headers)


class HotelchainUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = serializer.HotelChainSerializer
    def get_queryset(self):
        return HotelChain.objects.filter(id = self.kwargs.get('pk'))

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response({"status": True,
                         "message": "Hotel chain update!",
                         "data": serializer.data
                         })

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)