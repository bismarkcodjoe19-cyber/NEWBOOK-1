from ._anvil_designer import messagefeed_formTemplate
from anvil import *

class messagefeed_form(messagefeed_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
