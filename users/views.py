from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response

class CookieTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        # If error (like wrong login)
        if response.status_code != 200:
            return response

        access_token = response.data.get('access')
        refresh_token = response.data.get('refresh')

        # Set cookies
        response.set_cookie(
            key='access_token',
            value=access_token,
            httponly=True,
            secure=False,
            samesite='Lax'
        )

        response.set_cookie(
            key='refresh_token',
            value=refresh_token,
            httponly=True,
            secure=False,
            samesite='Lax'
        )

        return response
    