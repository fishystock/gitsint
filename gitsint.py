import argparse
from collections import defaultdict
from git import Repo
from tabulate import tabulate

def extract_emails_and_timezones(repo_path):
    repo = Repo(repo_path)
    data = defaultdict(set)
    seen_commits = set()

    for ref in repo.references:
        for commit in repo.iter_commits(ref):
            if commit.hexsha not in seen_commits:
                seen_commits.add(commit.hexsha)
                email = commit.author.email
                tz = commit.authored_datetime.strftime('%z')
                data[email].add(tz)

    return data

def main():
    parser = argparse.ArgumentParser(description='Extract emails and timezones from a local GitHub repository')
    parser.add_argument('repo_path', type=str, help='Path to the local GitHub repository')
    args = parser.parse_args()

    print(f'Fetching information from {args.repo_path}. This may take awhile on large repositories.')

    data = extract_emails_and_timezones(args.repo_path)
    table = [(email, ', '.join(sorted(timezones))) for email, timezones in sorted(data.items())]
    print(tabulate(table, headers=["Email", "UTC Offset(s)"], tablefmt="grid"))

if __name__ == '__main__':
    main()
