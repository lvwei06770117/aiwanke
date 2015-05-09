# -*- coding: utf-8 -*-
__author__ = 'wei'

from django import template
from django.template import Library
from django.utils.six.moves.urllib.parse import urljoin
from django.conf import settings
from django.utils.encoding import iri_to_uri

register = Library()

@register.filter
def get_range( value ):
    """
        Filter - returns a list containing range made from given value
        Usage (in template):

        <ul>{% for i in 3|get_range %}
          <li>{{ i }}. Do something</li>
        {% endfor %}</ul>

        Results with the HTML:
        <ul>
          <li>0. Do something</li>
          <li>1. Do something</li>
          <li>2. Do something</li>
        </ul>

        Instead of 3 one may use the variable set in the views
    """
    return range( value )
