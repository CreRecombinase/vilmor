import pytest

from vilmor.base.github import fetch_all_tags_gh


@pytest.mark.xfail()
def test_fetch_all_tags_gh():
    assert len(fetch_all_tags_gh("https://github.com/conda/vilmor")) > 1
