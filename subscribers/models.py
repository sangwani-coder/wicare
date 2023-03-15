from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LOCATION_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

# Create your models here.
class Subscribers(models.Model):
    """
    Model that stores Subscribers details.
    """
    created = models.DateTimeField(auto_now_add=True)
    firstname = models.CharField(max_length=30, blank=True)
    lastname = models.CharField(max_length=30, blank=True)
    location = models.CharField(choices=LOCATION_CHOICES, default='python', max_length=100)
    mobile = models.CharField(max_length=30, blank=True)
    email = models.CharField(max_length=30, blank=True)
    owner = models.ForeignKey('auth.User', related_name='subscribers', on_delete=models.CASCADE)
    highlighted = models.TextField()

    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
       """
       Use the `pygments` library to create a highlighted HTML
       representation of the code snippet.
       """
       lexer = get_lexer_by_name(self.location)
    #    linenos = 'table' if self.linenos else False
    #    options = {'title': self.title} if self.title else {}
    #    formatter = HtmlFormatter(style=self.style, linenos=linenos,
    #                              full=True, **options)
    #    self.highlighted = highlight(self.code, lexer, formatter)
       super().save(*args, **kwargs)
