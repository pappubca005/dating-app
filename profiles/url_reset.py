# from django.conf.urls import url
# from django.core.urlresolvers import reverse_lazy
from django.urls import reverse_lazy
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.urls import re_path as url

urlpatterns = [
    url(
        "^$",
        PasswordResetView.as_view(),
        {"post_reset_redirect": reverse_lazy("password_reset_done")},
        name="password_reset",
    ),
    url(r"^done/$", PasswordResetDoneView.as_view(), name="password_reset_done"),
    url(
        r"^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$",
        PasswordResetConfirmView.as_view(),
        {"post_reset_redirect": reverse_lazy("password_reset_complete")},
        name="password_reset_confirm",
    ),
    url(
        "^complete/$",
        PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
