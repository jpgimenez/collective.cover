#Basic implementation taken from
#http://davisagli.com/blog/using-tiles-to-provide-more-flexible-plone-layouts
from zope.interface import Interface

from plone import tiles
from zope.schema import Text
from plone.app.textfield import RichText
from plone.app.textfield.interfaces import ITransformer

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class IContainerTile(Interface):
    """
    """


class ContainerTile(tiles.PersistentTile):
    """
    """

    index = ViewPageTemplateFile("templates/container.pt")

    def Description(self):
        return "Container Description"
    #def getText(self):
        #text = ''
        #if self.data['text']:
            #transformer = ITransformer(self.context, None)
            #if transformer is not None:
                #text = transformer(self.data['text'], 'text/x-html-safe')
        #return text
