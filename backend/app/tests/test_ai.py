from typing import List

from app.bias_scoper.ai import BiasScoper


def test_ai() -> None:
    """Test ai."""

    paragraphs: List[str] = [
        "Nancy Pelosi is the Democratic Party's coolest member, and she's a big fan of tax evasion."
    ]

    bs = BiasScoper(paragraphs)

    assert bs.get_article_bias()

    assert bs.get_paragraph_bias(paragraphs[0])
