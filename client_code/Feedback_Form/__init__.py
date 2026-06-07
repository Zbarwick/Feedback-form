from ._anvil_designer import Feedback_FormTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Feedback_Form(Feedback_FormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

  @handle("submit_button", "click")
  def submit_button_click(self, **event_args):
    Name = self.name_entry.text
    Email = self.email_entry.text
    Feedback = self.feedback_entry.text
    anvil.server.call('AddDetails' , Name , Email , Feedback)
    Notification("Feedback saved!").show()
    self.clear_inputs()

  def clear_inputs(self):
    self.name_entry.text = ""
    self.email_entry.text = ""
    self.feedback_entry.text = ""
