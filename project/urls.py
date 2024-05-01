from django.contrib import admin
from django.urls import path
from branches.views import home, new_branch, UpdateBranchView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('branches/', home, name='home'),
    path('branches/new/', new_branch, name='new_branch'),
    path('branches/<int:pk>/update/', UpdateBranchView.as_view(), name='update_branch'),
]
