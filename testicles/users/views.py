from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, DeleteView

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserListView(LoginRequiredMixin, ListView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_list_view = UserListView.as_view()


class UserUpdateView(LoginRequiredMixin, UpdateView):

    model = User
    fields = ["name", "username",  "profile_pic", "email"]

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    def get_object(self):
        return User.objects.get(username=self.request.user.username)


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"
    success_url = '/'
    success_message = "Account Deleted"

user_delete_view = UserDeleteView.as_view()


class UserRequestsMadeView(LoginRequiredMixin, ListView):
    model = User
    template_name = "users/user_requests.html"

    def get_queryset(self):
        key = self.request.user.id
        req_user = User.objects.get(id=key)
        return req_user.providerrequests_set.all()

user_requests_made = UserRequestsMadeView.as_view()
