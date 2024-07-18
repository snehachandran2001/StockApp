from django.urls import path
from StockApp.views import global_market_data, indian_market_data, top_indian_companies_data

urlpatterns = [
    path('global-market/', global_market_data, name='global_market_data'),
    path('indian-market/', indian_market_data, name='indian_market_data'),
    path('top-indian-companies/', top_indian_companies_data, name='top_indian_companies_data'),
]
