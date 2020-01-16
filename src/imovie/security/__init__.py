# -*- coding: utf-8 -*-
"""
security package.
"""

from pyrin.packaging.context import Package


class SecurityPackage(Package):
    """
    security package class.
    """

    NAME = __name__
    DEPENDS = []
    COMPONENT_NAME = 'security.component'
