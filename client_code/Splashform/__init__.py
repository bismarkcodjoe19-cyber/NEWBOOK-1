from ._anvil_designer import SplashformTemplate
from anvil import *

class Splashform(SplashformTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
