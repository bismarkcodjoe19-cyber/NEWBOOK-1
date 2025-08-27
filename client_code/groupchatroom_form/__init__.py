from ._anvil_designer import groupchatroom_formTemplate
from anvil import *

class groupchatroom_form(groupchatroom_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
