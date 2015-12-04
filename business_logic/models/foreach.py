# -*- coding: utf-8 -*-
#

from django.db import models
from django.utils.encoding import smart_unicode
from django.utils.translation import gettext as _

class ForeachStatement(models.Model):
    class Meta:
        verbose_name = _('Foreach statement')
        verbose_name_plural = _('Foreach statements')
