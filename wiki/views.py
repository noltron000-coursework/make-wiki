from wiki.models import Page

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class PageList(ListView):
	'''
	Renders a list of all Pages.

	==CHALLENGES==
	1. GET: Have a homepage showing all Pages in your wiki.
	2. Add a descriptive docstring for PageList.
	3. Replace `pass` below with your code.
		-> Render a template named `list.html`.
	'''
	model = Page

	def get(self, request):
		'''
		GET Pages
		-> Returns a list of wiki pages.
		'''
		# ==TODO==
		# -> Get more intimate with .get_queryset() and .all()
		# -> Get more familiar with render(), and its params
		# -> Understand what the request param is
		pages = self.get_queryset().all()
		return render(request, 'list.html', {
			'pages': pages
		})

class PageDetail(DetailView):
	'''
	Renders a specific page based on it's slug.
	
	==CHALLENGES==
	1. GET: Have a homepage showing the details of your page.
	2. Add a descriptive docstring for PageDetail.
	3. Replace `pass` below with your code.
		-> Render a template named `page.html`.

	==STRETCHES==
	1. Import the PageForm class from forms.py.
		-> This ModelForm allows edits in existing Page objects.
	2. GET: Render an edit form below the page details.
	3. POST: Check if the data in the form is valid.
		-> If True, save the data. 
			Redirect back to the DetailsView.
		-> If False, display all the errors in the template.
			Do not redirect; display above the form fields.

	==NOTE==
	-> After successfully editing a Page: 
		-> Use Django Messages to "flash" a success message.
			`{PAGE_TITLE} has been successfully updated.`
	-> Don't hard-coding the path to redirect to.
		-> Use the `reverse` function to return the path instead.
	'''
	model = Page

	def get(self, request, slug):
		'''
		Returns a specific of wiki page by slug.
		'''
		# ==TODO==
		# -> Get more intimate with .get_queryset() and .get()
		# -> Get more familiar with render(), and its params
		# -> Understand the slug__iexact param
		# -> Understand what the request param is
		page = self.get_queryset().get(slug__iexact=slug)
		return render(request, 'page.html', {
			'page': page
		})

	def post(self, request, slug):
		'''
		Creates a new post!
		'''
		pass
