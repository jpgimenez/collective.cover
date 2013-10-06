# -*- coding: utf-8 -*-

import zope.event
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
from zope.component import getMultiAdapter
from zope.component import queryMultiAdapter
from zope.interface import implements
from zope.component import getMultiAdapter
from collective.cover.tiles.configuration import ITilesConfigurationScreen
from zope.component import getUtility
from zope.component import queryUtility
from plone.dexterity.interfaces import IDexterityFTI
from z3c.form import interfaces
from plone.dexterity.schema import SCHEMA_CACHE
from plone.behavior.interfaces import IBehavior
from plone.dexterity.utils import iterSchemata
from zope.interface import alsoProvides
from zope.pagetemplate.interfaces import IPageTemplate
from z3c.form.widget import AfterWidgetUpdateEvent


class BasicTile(Tile):

    index = ViewPageTemplateFile("templates/field.pt")
    is_configurable = True

    # def __call__(self, *args, **kwargs):
    #     self.index = ViewPageTemplateFile("templates/{0}.pt".format(self.id))
    #     if self.id is not None:
    #         self.request.response.setHeader('X-Tile-Url',
    #                 self.url[len(self.context.absolute_url()) + 1:])
    #     return self.index(self, *args, **kwargs)

    def widget(self):
        for schema in iterSchemata(self.context):
            field = schema.get(self.id, None)
            if field is not None:
                break;
        widget = queryMultiAdapter((field, self.request),
                    interfaces.IFieldWidget,
                    name=self.id)
        if widget is None:
            widget = queryMultiAdapter((field, self.request),
                        interfaces.IFieldWidget)            
        if queryMultiAdapter((None, self.request, None, None, widget),
            interface=IPageTemplate,
            name='display_{0}'.format(self.id)):
            widget.mode = 'display_{0}'.format(self.id)
        else:
            widget.mode = 'display'
        widget.context = self.context
        alsoProvides(widget, interfaces.IContextAware)
        widget.update()
        zope.event.notify(AfterWidgetUpdateEvent(widget))
        return widget

    def get_tile_configuration(self):
        # tile_conf_adapter = getMultiAdapter(
        #     (self.context, self.request, self), ITilesConfigurationScreen)
        # configuration = tile_conf_adapter.get_configuration()

        # return configuration
        return {}
