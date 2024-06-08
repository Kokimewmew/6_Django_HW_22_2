from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


def home(request):
    return render(request, template_name='home.html')


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"
    extra_context = {
        'title': 'contacts'
    }

    def get_context_data(self, **kwargs):
        if self.request.method == 'POST':
            name = self.request.POST.get('name')
            phone = self.request.POST.get('phone')
            message = self.request.POST.get('message')
            print(f'You have new message from {name}({phone}): {message}')
        return super().get_context_data(**kwargs)


# def contacts(request):
#    if request.method == 'POST':
#        name = request.POST.get('name')
#        phone = request.POST.get('phone')
#        message = request.POST.get('message')
#        print(f'{name} {phone} {message}')
#    return render(request, template_name='contacts.html')


class ProductsListview(ListView):
    model = Product


# def products_list(request):
#    products = Product.objects.all()
#    context = {"products": products}
#    return render(request, 'product_list.html', context)


class ProductsDetailview(DetailView):
    model = Product

# def products_detail(request, pk):
#    product = get_object_or_404(Product, pk=pk)
#    context = {"product": product}
#    return render(request, 'product_detail.html', context)
