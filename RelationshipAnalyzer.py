def get_relationship_count(commit_hash, path, combinations):
    """
    Gets a value indicating if the path was modified as part of the specified commit hash. If it was modified, a 1
    will be returned. Otherwise a 0 will be returned.
    :param commit_hash: The commit hash.
    :param path: The file in question
    :param combinations: the list of file combinations to analyze
    :return: 1 if the file was modified as part of the commit hash, otherwise 0
    """

    for entry in combinations:
        if entry['hash'] == commit_hash:
            if path in entry['paths']:
                return 1
            else:
                return 0

    return 0
