from ._anvil_designer import profilesetup_formTemplate
from anvil import *

class profilesetup_form(profilesetup_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
