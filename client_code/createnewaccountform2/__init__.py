from ._anvil_designer import createnewaccountform2Template
from anvil import *

class createnewaccountform2(createnewaccountform2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
