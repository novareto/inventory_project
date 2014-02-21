# -*- coding: utf-8 -*-
# Copyright (c) 2007-2013 NovaReto GmbH
# cklinger@novareto.de

import uvclight
from dolmen.forms import crud

from .interfaces import IInventorySystem
from .models import InventorySystem
from dolmen.location import get_absolute_url


class Index(uvclight.TablePage):
    uvclight.context(uvclight.IRootObject)
    title = u"Inventory"
    description = u"BLA"

    cssClasses = {'table': 'tablesorter table table-striped table-bordered table-condensed'}
    cssClassEven = u'even'
    cssClassOdd = u'odd'

    @property
    def values(self):
        for obj in self.context.values():
            yield obj


class ColumnLink(uvclight.Column):
    uvclight.context(uvclight.IRootObject)
    uvclight.view(Index)
    header = u"System"

    def renderCell(self, item):
        return "<a href='%s'> %s </a>" % (
            get_absolute_url(item, self.request), item.system)


class ColumnCustomer(uvclight.Column):
    uvclight.context(uvclight.IRootObject)
    uvclight.view(Index)
    header = u"Customer"

    def renderCell(self, item):
        return item.customer


@uvclight.menuentry(uvclight.IContextualActionsMenu)
class Add(uvclight.AddForm):
    uvclight.title(u'Add')
    uvclight.name(u'add')
    uvclight.context(uvclight.IRootObject)
    fields = uvclight.Fields(IInventorySystem)

    def create(self, data):
        return InventorySystem(**data)

    def add(self, obj):
        self.context['inventory_%s' % len(self.context.items())] = self.obj = obj

    def nextURL(self):
        return get_absolute_url(self.obj, self.request)


@uvclight.menuentry(uvclight.IContextualActionsMenu)
class Edit(uvclight.EditForm):
    uvclight.title('Edit')
    uvclight.context(IInventorySystem)


@uvclight.menuentry(uvclight.IContextualActionsMenu)
class IndexInventory(uvclight.DisplayForm):
    uvclight.title('Display')
    uvclight.name('index')
    uvclight.context(IInventorySystem)


@uvclight.menuentry(uvclight.IContextualActionsMenu)
class Delete(uvclight.DeleteForm):
    uvclight.title('Delete')
    uvclight.context(IInventorySystem)
