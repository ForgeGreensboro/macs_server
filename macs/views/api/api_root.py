from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view('GET')
def api_root(request, format=None):
    return Response({
        'members': reverse('member-list', request=request, format=format),
        'machines': reverse('machines-list', request=request, format=format)
        })
