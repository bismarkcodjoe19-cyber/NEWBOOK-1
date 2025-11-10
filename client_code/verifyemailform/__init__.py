from ._anvil_designer import verifyemailformTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class verifyemailform(verifyemailformTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    pass

  def timer_1_show(self, **event_args):
    """This method is called when this timer's form is shown on the screen (or it is added to a visible form)"""
    pass
