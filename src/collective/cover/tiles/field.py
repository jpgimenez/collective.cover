# -*- coding: utf-8 -*-

from collective.cover import _
from collective.cover.controlpanel import ICoverSettings
from plone.tiles import Tile
from collective.cover.tiles.configuration_view import IDefaultConfigureForm
from plone.autoform import directives as form
from plone.memoize import view
from plone.memoize.instance import memoizedproperty
from plone.namedfile.field import NamedBlobImage as NamedImage
from plone.registry.interfaces import IRegistry
from plone.tiles.interfaces import ITileDataManager
from plone.uuid.interfaces import IUUID
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import safe_unicode
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope import schema
from zope.component import getUtility
from zope.interface import implements
from zope.component import getMultiAdapter
from collective.cover.tiles.configuration import ITilesConfigurationScreen


class BasicTile(Tile):

    is_configurable = True

    def __call__(self, *args, **kwargs):
        self.index = ViewPageTemplateFile("templates/{0}.pt".format(self.id))
        if self.id is not None:
            self.request.response.setHeader('X-Tile-Url',
                    self.url[len(self.context.absolute_url()) + 1:])
        return self.index(self, *args, **kwargs)

    def render_field(self):
        return getattr(self.context, self.id)

    def get_tile_configuration(self):
        # tile_conf_adapter = getMultiAdapter(
        #     (self.context, self.request, self), ITilesConfigurationScreen)
        # configuration = tile_conf_adapter.get_configuration()

        # return configuration
        return {}