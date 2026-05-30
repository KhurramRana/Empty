import os
import random
from datetime import datetime, timedelta

def populate():
    # End date is today, May 30, 2026
    # Start date is one year ago
    for i in range(365, -1, -1):
        date = (datetime.now() - timedelta(days=i)).strftime('%Y-%m-%dT12:00:00')

        # Variety: 0-10 commits (some days will be empty for a real look)
        num_commits = random.choices(range(11), weights=[1, 2, 3, 4, 3, 2, 1, 1, 1, 1, 1])[0]

        if num_commits > 0:
            print(f"Commiting {num_commits} times for {date}")
            for _ in range(num_commits):
                os.system(f'GIT_AUTHOR_DATE="{date}" GIT_COMMITTER_DATE="{date}" git commit --allow-empty -m "Update: {date}" --quiet')

if __name__ == "__main__":
    populate()
