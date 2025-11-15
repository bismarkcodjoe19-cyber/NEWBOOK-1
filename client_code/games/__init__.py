from ._anvil_designer import gamesTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class gamesgamesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  self.game_area.content = """
<iframe src="/_/theme/ludo/index.html"
        width="100%"
        height="600"
        style="border:none;">
</iframe>
"""

