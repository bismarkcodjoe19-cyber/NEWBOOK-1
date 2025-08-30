from ._anvil_designer import phonecallformTemplate
from anvil import *

class phonecallform(phonecallformTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
