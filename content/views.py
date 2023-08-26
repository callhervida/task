from django.db.models import Avg, Count
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


from .models import Content, Rate
from .serializers import ContentSerializer


class ContentList(APIView):
    """An end point to show content's title, context, amount of users that rated and
    user's rate if existed"""

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, ]

    def get(self, request):

        user_id = request.user.id

        content_obj = Content.objects.all()

        if not content_obj:
            response = {
                'data': '',
                'message': 'there is no content'
            }

            return Response(response, status=400)

        content_serialized = ContentSerializer(content_obj, many=True)

        content_list = []
        for i in content_serialized.data:
            content_id = i['id']

            rate_obj = Rate.objects.filter(content=content_id, user=user_id).first()

            if rate_obj:
                user_rate = rate_obj.rate
            else:
                user_rate = None

            i.update({"user_rate": user_rate})

            content_list.append(i)

        response = {
            'data': content_list,
            'message': 'Successful'
        }

        return Response(response, status=200)


class Rating(APIView):
    """An end point to rate the desired content while updating average rating"""
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, ]

    def post(self, request):

        user_id = request.user.id

        content_id = request.data.get('content_id')

        rate = request.data.get('rate')

        if not rate in range(0, 6):
            response = {
                'data': '',
                'message': 'Rating must be between 0 and 5'
            }

            return Response(response, status=400)

        content_obj = Content.objects.filter(id=content_id)

        if not content_obj.first():
            response = {
                'data': '',
                'message': 'Content does not exist'
            }

            return Response(response, status=400)

        rate_obj = Rate.objects.filter(user=user_id, content=content_id)

        if rate_obj.first():

            rate_obj.update(rate=rate)

            rate_mean = Rate.objects.filter(content=content_id).aggregate(Avg('rate'))

            content_obj.update(rate_mean=round(rate_mean.get('rate__avg'), 1))

        else:

            Rate.objects.create(
                user_id=user_id,
                content_id=content_id,
                rate=rate
            )

            rate_mean = Rate.objects.filter(content=content_id).aggregate(Avg('rate'), Count('user'))

            content_obj.update(
                rate_mean=round(rate_mean.get('rate__avg'), 1),
                user_count=rate_mean.get('user__count')
            )

        response = {
            'data': '',
            'message': 'Successful'
        }

        return Response(response, status=200)



