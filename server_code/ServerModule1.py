import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime

@anvil.server.callable
def AddDetails(Name , Email , Feedback):
  app_tables.feedback.add_row(
    Name = Name,
    Email = Email,
    Feedback = Feedback,
    Created = datetime.now()
  )