from ._anvil_designer import profilesetup_form2Template
from anvil import *

class profilesetup_form2(profilesetup_form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
