import os
from os import path


"""
This program is used once the vote has ended and we need to delete the remaining files
"""

if path.exists("pubkey.json"):
  os.remove("pubkey.json")
if path.exists("ci.json"):
  os.remove("ci.json")
if path.exists("resultats.json"):
  os.remove("resultats.json")
if path.exists("secretkeys.json"):
  os.remove("secretkeys.json")
if path.exists("vi.json"):
  os.remove("vi.json")
if path.exists("votes.json"):
  os.remove("votes.json")
if path.exists("globalConf.json"):
  os.remove("globalConf.json")