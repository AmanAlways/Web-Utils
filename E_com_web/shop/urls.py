from django.urls import path
from.import views

urlpatterns = [
    path('', views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="Tracking Status"),
    path("search/", views.search, name="Search"),
    path("productview/", views.productview, name="Productview"),
    path("checkout/", views.checkout, name="Checkout"),
    path("wishlist/", views.wishlist, name="wishlist"),
    path("viewcart/", views.viewCart, name="View Cart")

]
