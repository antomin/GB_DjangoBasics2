from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, ListView, UpdateView


class OrdersListView(ListView):
    pass


class OrdersCreateView(CreateView):
    pass


class OrdersUpdateView(UpdateView):
    pass


class OrdersDeleteView(DeleteView):
    pass
