"""Repo resolution -- delegates to rhdh_lifecycle.repo."""

from rhdh_lifecycle.repo import GITHUB_REPO, resolve_repo_root  # noqa: F401

__all__ = ["GITHUB_REPO", "resolve_repo_root"]
