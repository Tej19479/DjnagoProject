from django.urls import path
from . import views

app_name = "shopapp"
urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("/about", views.about, name="AboutUs"),
    path("/contact", views.contact, name="ContactUs"),
    path("/search/", views.search, name="Search"),
    path("/checkout/", views.checkout, name="Checkout"),
    path("/tracker", views.tracker, name="TrackingStatus"),
    path("/prodView", views.productView, name="ProductView"),
    path("/handlerequest", views.handlerequest, name="Handlerequest"),
    path("/logout", views.logout, name="logout"),

]
