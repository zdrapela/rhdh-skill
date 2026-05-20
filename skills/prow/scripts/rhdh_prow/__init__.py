"""Access openshift/release repo data (CI configs, cluster pools)."""


def ver_sort_key(version_str):
    """Sort key for version strings like '4.16' or '26.2'.

    NOTE: This is a copy of rhdh_lifecycle.redhat.ver_sort_key.
          Keep both copies in sync when modifying.
    """
    try:
        return [int(x) for x in version_str.split(".")]
    except ValueError:
        return [0]
