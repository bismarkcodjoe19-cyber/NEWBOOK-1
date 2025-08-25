from ._anvil_designer import profilesetup_form2Template
from anvil import *

class profilesetup_form2(profilesetup_form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def text_box_1_pressed_enter(self, **event_args):
     query = self.text_box_1.text.lower()
     results = [item for item in self.all_items if query in item.lower()]
     print(results)  # You can replace this with logic to display results

