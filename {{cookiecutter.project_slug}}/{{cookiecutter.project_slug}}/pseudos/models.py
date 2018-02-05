# -*- coding: utf-8 -*-

from django.db import models


class Pseudo(models.Model):
    """
    just a bas class to test python path
    """
    name = models.CharField(max_length=34)
