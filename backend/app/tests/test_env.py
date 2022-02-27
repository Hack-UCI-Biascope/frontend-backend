import os


def test_env() -> None:
    """Test the retrieval of environment variables."""
    print(os.environ["SECRET"])
    assert os.environ["SECRET"] == "186d580cbf9b546467925b12af9e730e09ccca8078bcd189c5ab338e8c3787dc"
