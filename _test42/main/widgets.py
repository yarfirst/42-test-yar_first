from django import forms
from django.templatetags.static import static


class CalendarWidget(forms.DateInput):
    @property
    def media(self):
        return forms.Media(
            css={
                'all': ('http://code.jquery.com/ui/1.10.3/themes/smoothness/jquery-ui.css',)
            },
            js=(
                'http://code.jquery.com/jquery-1.9.1.js',
                'http://code.jquery.com/ui/1.10.3/jquery-ui.js',
                static('js/calendar_widget.js'),
            )
        )

    def __init__(self, attrs=None, format=None):
        final_attrs = {'wtype': 'datepicker'}
        if attrs is not None:
            final_attrs.update(attrs)
        super(CalendarWidget, self).__init__(attrs=final_attrs, format=format)
