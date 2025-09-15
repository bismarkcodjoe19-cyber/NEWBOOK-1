from ._anvil_designer import status_holder_panelTemplate
from anvil import *

class status_holder_panel(status_holder_panelTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
