from ._anvil_designer import profile_previewTemplate
from anvil import *


class profile_preview(profile_previewTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
