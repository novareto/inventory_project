# -*- coding: utf-8 -*-
# Copyright (c) 2007-2013 NovaReto GmbH
# cklinger@novareto.de


from zope import interface, schema


class IInventorySystem(interface.Interface):
    """ Descirbes and cassifies the Systems
    """

    customer = schema.TextLine(
        title=u"Customer",
        description=u"Add the Customer here",
    )

    system = schema.TextLine(
        title=u"System",
        description=u"Please specify the System in terms of Intranet Extranet",
    )

    description = schema.Text(
        title=u"Description",
        description=u"Give a short Description of the System",
    )

    access = schema.Text(
        title=u"Access",
        description=u"Please describe the access methods for that System\
                      IP-Adress, Port, SSH-Credentials, HTTP-Credentials",
    )
