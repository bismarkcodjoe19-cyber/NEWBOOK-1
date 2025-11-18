from ._anvil_designer import ludo_formTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ludo_form(ludo_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

from anvil import *
import anvil.server

class ludo_lorm(ludo_formTemplate):
    def __init__(self, **properties):
        # Set up form
        self.init_components(**properties)

        # Load the Ludo game into the RichText/iframe
        self.game_frame.url = "_/theme/assets/ludo/index.html"

        # Optional: Track which user is playing
        if anvil.users.get_user():
            self.label_user.text = f"Player: {anvil.users.get_user()['username']}"
        else:
            self.label_user.text = "Guest Player"

    # Example: Start new session
    def button_new_session_click(self, **event_args):
        user = anvil.users.get_user()
        if user:
            anvil.server.call('start_ludo_session', user['id'])
            alert("New Ludo session started!")
        else:
            alert("Please log in to start a session.")

