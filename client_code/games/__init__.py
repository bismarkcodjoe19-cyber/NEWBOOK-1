from ._anvil_designer import gamesTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Games(GamesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  from ._anvil_designer import GamesTemplate
from anvil import *

class games(gamesTemplate):
  def __init__(self, **properties):
    # Initialise the form and its components
    self.init_components(**properties)

    # Load the Ludo game into the RichText component
    self.game_area.content = """
        <iframe src="/_/theme/ludo/index.html"
                width="100%"
                height="600"
                style="border:none;">
        </iframe>
        """

