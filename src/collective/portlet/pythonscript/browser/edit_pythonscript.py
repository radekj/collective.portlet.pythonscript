from Products.CMFPlone import PloneMessageFactory as _
from Products.Five.browser import BrowserView
from collective.portlet.pythonscript.content.scriptmanager import IPythonScriptManager
from Products.statusmessages.interfaces import IStatusMessage
from plone.protect import CheckAuthenticator, PostOnly

class EnablePythonScriptView(BrowserView):
    """View for enabling Python Script."""
    
    def __call__(self, id):
        """Rescan and redirect."""
        # Check against CSRF.
        CheckAuthenticator(self.request)
        PostOnly(self.request)

        manager = IPythonScriptManager(self.context)
        msg = self.performAction(manager, id)
        IStatusMessage(self.request).addStatusMessage(msg)
        self.request.response.redirect(self.context.absolute_url() + '/@@manage_pythonscript')
        
    def performAction(self, manager, id):
        """Enable script and return portal message."""
        manager.enableScript(id)
        return _(u'Script enabled')
    
class DisablePythonScriptView(EnablePythonScriptView):
    """View for disabling Python Script."""

    def performAction(self, manager, id):
        """Disable script and return portal message."""
        manager.disableScript(id)
        return _(u'Script disabled')
