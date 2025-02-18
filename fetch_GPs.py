#!/usr/bin/env python3

import pandas as pd
import requests

df = pd.DataFrame(requests.get("https://healthpoint.co.nz/geo.do?zoom=18&branch=gps-accident-urgent-medical-care").json()["results"])
print(df)
df.to_csv("GPs.csv", index=False)