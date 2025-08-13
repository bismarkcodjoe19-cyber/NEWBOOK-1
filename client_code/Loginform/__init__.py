from ._anvil_designer import LoginformTemplate
from anvil import *


class Loginform(LoginformTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def youtube_video_1_state_change(self, state, **event_args):
    """This method is called when the video changes state (eg PAUSED to PLAYING)"""
    pass
