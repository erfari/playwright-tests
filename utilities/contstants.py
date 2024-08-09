from pathlib import Path

BASE_URL = "https://stage.skies.land/"
TEST_URL = "https://stage.skies.land/svetlana"
EMAIL_TEST_USER = ""
PASSWORD_TEST_USER = ""
AUTOMATION_USER_AGENT: str = "automation"
DATA_PATH: Path = Path(Path(__file__).absolute().parent.parent, "data")
CHROME_DOWNLOAD_DIRECTORY: Path = DATA_PATH / "downloads"
DIFF_TOLERANCE_PERCENT: float = 0.01

