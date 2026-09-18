# PLAN: Add Dockerfile for stats generation
- Goal: Create a Dockerfile to containerize the `generate_streak.py` script.
- Files: Add `Dockerfile` in the root.
- Test Command: `docker build -t yunaremaia-stats . && docker run --rm yunaremaia-stats python generate_streak.py --help`
- Acceptance Criteria: Docker image builds successfully and can run the script.
