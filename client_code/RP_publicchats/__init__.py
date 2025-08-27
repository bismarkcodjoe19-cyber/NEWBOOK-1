from ._anvil_designer import RP_publicchatsTemplate
from anvil import *

class RP_publicchats(RP_publicchatsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
