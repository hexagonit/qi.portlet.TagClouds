# from Products.PloneTestCase import PloneTestCase
# from Products.Five.testbrowser import Browser
# from qi.portlet.TagClouds import testing


# PloneTestCase.setupPloneSite()


# class TagCloudsTestCase(PloneTestCase.PloneTestCase):
#     """We use this base class for all the tests in this package.
#     """
#     layer = testing.layer


# class TagCloudsFunctionalTestCase(PloneTestCase.FunctionalTestCase):
#     """We use this class for functional integration tests.
#     """
#     layer = testing.layer

#     def getCredentials(self):
#         return '%s:%s' % (PloneTestCase.default_user,
#             PloneTestCase.default_password)

#     def getBrowser(self, loggedIn=True):
#         """ instantiate and return a testbrowser for convenience """
#         browser = Browser()
#         if loggedIn:
#             auth = 'Basic %s' % self.getCredentials()
#             browser.addHeader('Authorization', auth)
#         return browser



from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import unittest


class QiPortletTagCloudsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        """Set up Zope."""

        # Required by Products.CMFPlone:plone-content to setup defaul plone site.
        z2.installProduct(app, 'Products.PythonScripts')

        # Load ZCML
        import qi.portlet.TagClouds
        self.loadZCML(package=qi.portlet.TagClouds)

    def setUpPloneSite(self, portal):
        """Set up Plone."""

        # Installs all the Plone stuff. Workflows etc. to setup defaul plone site.
        self.applyProfile(portal, 'Products.CMFPlone:plone')

        # Install portal content. Including the Members folder! to setup defaul plone site.
        self.applyProfile(portal, 'Products.CMFPlone:plone-content')


        # Install into Plone site using portal_setup
        self.applyProfile(portal, 'qi.portlet.TagClouds:default')

    def tearDownZope(self, app):
        """Tear down Zope."""
        z2.uninstallProduct(app, 'Products.PythonScripts')


FIXTURE = QiPortletTagCloudsLayer()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,), name="QiPortletTagCloudsLayer:Integration")
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,), name="QiPortletTagCloudsLayer:Functional")


class IntegrationTestCase(unittest.TestCase):
    """Base class for integration tests."""

    layer = INTEGRATION_TESTING


class FunctionalTestCase(unittest.TestCase):
    """Base class for functional tests."""

    layer = FUNCTIONAL_TESTING