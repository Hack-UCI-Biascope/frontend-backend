import os

from dotenv import load_dotenv


def test_env() -> None:
    """Test the retrieval of environment variables."""
    load_dotenv()
    print(os.environ["SECRET"])
    assert os.environ["SECRET"] == "186d580cbf9b546467925b12af9e730e09ccca8078bcd189c5ab338e8c3787dc"
