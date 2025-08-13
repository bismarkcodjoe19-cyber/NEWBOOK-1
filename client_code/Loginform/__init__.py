from ._anvil_designer import LoginformTemplate
from anvil import *


class Loginform(LoginformTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
