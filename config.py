import os
from typing import cast
from dotenv import load_dotenv

load_dotenv()

BASE_URL = cast(str, os.getenv("BASE_URL"))
USER = cast(str, os.getenv("QA_USER"))
PASSWORD = cast(str, os.getenv("QA_PASSWORD"))

if not USER or not PASSWORD or not BASE_URL:
    raise EnvironmentError("Enviorenment variables not configured!")