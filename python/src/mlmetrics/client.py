import os
from urllib import request
import json

class Client:
  def __init__(self, token=None, url=None):
    if url:
      self.url = url
    else:
      self.api_url = os.environ.get("MLMETRICS_API_URL", "https://www.mlmetrics/api")

    if token:
      self.token = token
    else:
      self.token = os.environ.get("MLMETRICS_TOKEN")

  def runs(self, run_ids):
    request_url=self.url + '/runs/get?run_ids=' + ",".join(run_ids)
    req = request.Request(request_url, method="GET")
    req.add_header('Authorization', 'Bearer ' + self.token)
    r = request.urlopen(req)
    content = r.read()
    print(json.loads(content))

    # TODO: Store raw and summary statistics.

    return []
