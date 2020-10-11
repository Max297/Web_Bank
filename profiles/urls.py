from django.conf.urls import url
from . import views

app_name = "profiles"

urlpatterns = [
    url(r"^account/$", views.index, name = "account"),
    url(r"^money_transfer/", views.money_transfer, name = "money_transfer"),
    url(r"^loan_app/$", views.loan, name = "loan_app"),
    url(r"^online_pay/$", views.online_pay, name = "online_pay"),
    url(r"settings/$", views.settings, name = "settings"),
    url(r"delete_account/$", views.delete_account, name = "delete_account")
]
