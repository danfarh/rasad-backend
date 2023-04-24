from django.urls import path
from users.views import (RegisterView, LoginView,
                        CreateCompanyView, AddVisitorByBossView,
                        RetrieveUpdateDestroyVisitorView, ListVisitorsView,
                        ListCompanyView,ReportVisitorsActivity,GetVisitorCoordinates,GetVisitorActivity)

app_name = 'users'
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('company/create/', CreateCompanyView.as_view(), name='create_company'),
    path('company/', ListCompanyView.as_view(), name='company'),
    path('visitors/', ListVisitorsView.as_view(), name='visitors'),
    path('add/visitor/', AddVisitorByBossView.as_view(), name='add_visitor'),
    path('visitor/<int:pk>/',RetrieveUpdateDestroyVisitorView.as_view(), name='edit_visitor'),
    path('report/visitor/<int:company_id>/',ReportVisitorsActivity.as_view(), name='report_visitor'),
    path('coordinates/visitor/', GetVisitorCoordinates.as_view(), name='coordinates_visitor'),
    path('visitor/activity/', GetVisitorActivity.as_view(), name='visitor_activity'),
]
