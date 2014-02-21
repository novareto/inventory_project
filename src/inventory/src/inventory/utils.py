# -*- coding: utf-8 -*-


from uvclight.backends.zodb import Root
from cromlech.configuration.utils import load_zcml
from cromlech.i18n import register_allowed_languages
from cromlech.dawnlight import DawnlightPublisher
from cromlech.browser import PublicationBeginsEvent, PublicationEndsEvent
from cromlech.browser import IPublicationRoot
from zope.interface import implements
from zope.event import notify
from webob.dec import wsgify
from cromlech.webob.request import Request
from cromlech.dawnlight import ViewLookup
from cromlech.dawnlight import view_locator, query_view
from cromlech.zodb import get_site, Site
from cromlech.zodb import initialize_applications


view_lookup = ViewLookup(view_locator(query_view))


class Root(Root):
    implements(IPublicationRoot)

    title = u"Example Site"
    description = u"An Example application."
    dummy = ""


KEY = "zodb.connection"


class WSGIApplication(object):

    def __init__(self, name):
        self.name = name
        self.publisher = DawnlightPublisher(view_lookup=view_lookup)

    @wsgify(RequestClass=Request)
    def __call__(self, request):
        conn = request.environment[KEY]
        site = get_site(conn, self.name)
        with Site(site) as site:
            response = self.publisher.publish(
                request,
                site,
                handle_errors=True
            )
        return response


def create_my_app(db):
    initialize_applications(db, lambda: {'inventory': Root})


def app_factory(global_conf, name, zcml_file, langs='en'):
    load_zcml(zcml_file)
    allowed = langs.strip().replace(',', ' ').split()
    register_allowed_languages(allowed)
    return WSGIApplication(name)
