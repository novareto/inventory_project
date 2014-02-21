# -*- coding: utf-8 -*-
# Copyright (c) 2007-2013 NovaReto GmbH
# cklinger@novareto.de

import uvclight

from uvclight.backends import zodb
from .interfaces import IInventorySystem


class InventorySystem(zodb.Model):
    uvclight.schema(IInventorySystem)
