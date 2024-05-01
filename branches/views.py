from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, DetailView, UpdateView
from .models import Branch
from .forms import BranchForm


def home(request):
    first_branch = Branch.objects.first()
    if first_branch:
        return redirect('update_branch', pk=first_branch.pk)
    return render(request, 'branches/home.html')

def new_branch(request):
    new_branch = Branch.objects.create()
    return redirect('update_branch', pk=new_branch.pk)

# create edit branch view
class UpdateBranchView(UpdateView):
    model = Branch
    fields = '__all__'
    template_name_suffix = '_update_form'

    def get_success_url(self) -> str:
        return reverse('update_branch', kwargs={'pk': self.kwargs.get('pk')})

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        prev_branches = Branch.objects.filter(pk__lt=self.kwargs.get('pk'))
        next_branches = Branch.objects.filter(pk__gt=self.kwargs.get('pk'))
        prev_len = len(prev_branches)
        if prev_len:
            context['first_branch_pk'] = prev_branches[0].pk
            context['prev_branch_pk'] = prev_branches[prev_len - 1].pk
        next_len = len(next_branches)
        if next_len:
            context['next_branch_pk'] = next_branches[0].pk
            context['last_branch_pk'] = next_branches[next_len - 1].pk
        context['total_prev'] = prev_len + 1
        context['total'] = prev_len + next_len + 1
        return context
