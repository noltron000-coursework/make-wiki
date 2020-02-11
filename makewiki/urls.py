'''
Makewiki URL Configuration

The `urlpatterns` list routes URLs to views.
For more information please see:
- https://docs.djangoproject.com/en/2.2/topics/http/urls/

== EXAMPLES ==
Function views
- Add an import:
	- `from my_app import views`
- Add a URL to urlpatterns: 
	-	`path('', views.home, name='home')`

Class-based views
- Add an import:  from other_app.views import Home
- Add a URL to urlpatterns:
	-	`path('', Home.as_view(), name='home')`

Including another URLconf
- Import the include() function:
	- `from django.urls import include, path`
- Add a URL to urlpatterns:
	-	`path('blog/', include('blog.urls'))`
'''

from django.contrib import admin
from django.urls import include, path

'''
== CHALLENGES ==
- Uncomment the path() for the wiki app below.
	Use it to direct any request (except `/admin` URLs)
	to the the `wiki` app's URL configuration.
	Use the above docstring to guide you if you feel stuck.
- Make sure Django doesn't give you any
	warnings or errors when you run the server:
	- `python manage.py runserver`.
'''
urlpatterns = [
	# Admin Site
	path('admin/', admin.site.urls),

	# Wiki App
	path('', include('wiki.urls')),
]
