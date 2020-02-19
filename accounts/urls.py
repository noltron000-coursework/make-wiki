from django.urls import path
from accounts.views import SignUpView

urlpatterns = [
	path('', SignUpView.as_view(), name='signup'),
]
