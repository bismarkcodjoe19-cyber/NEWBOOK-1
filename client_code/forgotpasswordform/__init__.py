from ._anvil_designer import forgotpasswordformTemplate
from anvil import *


class forgotpasswordform(forgotpasswordformTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    pass

  def timer_1_hide(self, **event_args):
    """This method is called when this timer's form is hidden from the screen (or it is removed from a visible form)"""
    pass
