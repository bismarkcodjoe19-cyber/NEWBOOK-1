from ._anvil_designer import creategroup_formTemplate
from anvil import *

class creategroup_form(creategroup_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
