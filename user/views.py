from django.shortcuts import render
from django.views import View


class HomePageView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass


class InformationDetailView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass


# 登陆才可发表，那如何做登陆限制呐？
class PublishInformationView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass
