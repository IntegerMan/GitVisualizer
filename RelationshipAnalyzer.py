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


def build_edge_list(df):
    """
    Builds an edge list out of a collection of grouped data in a Pandas data frame. It is assumed that the groups
    will have an index that is the name of the file and each row will have a series of columns starting with "rel_"
    and ending with the name of the file and contain the count of times the files are modified together.

    :param df: the Pandas grouped data frame.
    :return: an array of edge nodes defining the file the edge is from, the edge is to, and the strength
    """

    edges = []
    index = 0

    for path in df.index:
        for col in df.columns:
            # Only pay attention to relationship columns
            if not col.startswith('rel_'):
                continue

            # strip out 'rel_'
            to_path = col[len('rel_'):]

            # Ignore self-relations
            if to_path == path:
                continue

            # Extract the strength
            val = df.iloc[index][col]

            # Ignore no relationship edges
            if val <= 0:
                continue

            edges.append({'from': path, 'to': to_path, 'strength': val})
        index += 1

    return edges


def build_edge_tuples(df):
    """
    Builds an edge tuple list out of a collection of grouped data in a Pandas data frame. It is assumed that the groups
    will have an index that is the name of the file and each row will have a series of columns starting with "rel_"
    and ending with the name of the file and contain the count of times the files are modified together.

    :param df: the Pandas grouped data frame.
    :return: an array of edge tuples with the file the edge is from and the edge is to
    """

    edges = []
    index = 0

    for path in df.index:
        for col in df.columns:
            # Only pay attention to relationship columns
            if not col.startswith('rel_'):
                continue

            # strip out 'rel_'
            to_path = col[len('rel_'):]

            # Ignore self-relations
            if to_path == path:
                continue

            # Extract the strength
            val = df.iloc[index][col]

            # Ignore no relationship edges
            if val <= 0:
                continue

            edges.append((path, to_path))
        index += 1

    return edges
