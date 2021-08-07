from pydriller import Repository

def analyzeRepository(repoPath):
    fileModifications = []
    pathCombinations = []

    for commit in Repository(repoPath).traverse_commits():
        paths = []
        for file in commit.modified_files:
            paths.append(file.new_path)
            record = {
                'path': file.new_path,
                'commit': commit.hash,
                'author': commit.author.name,
                'lines_added': file.added_lines,
                'lines_deleted': file.deleted_lines,
            }
            fileModifications.append(record)
        pathCombinations.append(paths)

    return pathCombinations, fileModifications
