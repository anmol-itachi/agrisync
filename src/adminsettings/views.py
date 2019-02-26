from .utils import set_settings, set_default, get_settings
from .mixins import SettingsMixin, RedirectMixin
from django.contrib import messages


class SettingsChangeView(SettingsMixin):
    """
    View for settings change
    """
    pass


class SettingsChangeDoneView(SettingsMixin):
    """
    change settings and redirect to change settings
    """
    def get(self, request, *args, **kwargs):
        set_settings(request.POST)
        messages.success(request, "Settings changed successfully ...")
        return RedirectMixin.as_view(redirect_url='settings:settings_change')(request)


class SettingsResetView(SettingsMixin):
    """
    reset settings and redirect to change settings
    """
    def get(self, request, *args, **kwargs):
        set_default()
        set_settings(get_settings())
        messages.success(request, "Settings reset successfully ...")
        return RedirectMixin.as_view(redirect_url='settings:settings_change')(request)
