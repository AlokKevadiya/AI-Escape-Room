# Demonstration and final submission

## What still requires the student

- Ensure the instructor can access the private GitHub repository.
- Configure a free-tier Gemini key and valid model in local `.env`.
- Run both versions live; record at least five comparison cases from TESTING.md.
- Capture actual screenshots or a short screen recording. Current package has no
  app screenshots: the browser in the build environment could not access the server.
- Update the report with measured V1 behavior and review all AI-assisted material.

## Screenshot / video plan (about 3 minutes)

1. Show V1 with Gemini enabled and examine the bookshelf.
2. Attempt uncollected-key use and administrator impersonation; preserve the real
   responses even if V1 correctly refuses. Do not stage a fabricated failure.
3. Switch to V2 (fresh session); show identical challenges and unchanged progress.
4. Show an interpreted action, cancel once, then confirm a legal action.
5. Complete the walkthrough; show inventory, three puzzles and the open exit.
6. Download evidence for both versions, show tests passing and architecture diagrams.

Never show `.env`, API keys or private account details in a recording. Add only
reviewed game screenshots under `docs/screenshots/` and link them from the README.

## Optional archive recovery (not needed for the uploaded repository)

The downloadable package includes a Git bundle outside the source folder. On a
computer with Git installed, from the extracted package directory:

```bash
git clone AI-Escape-Room-history.bundle AI-Escape-Room-with-history
cd AI-Escape-Room-with-history
git remote remove origin
git remote add origin https://github.com/AlokKevadiya/AI-Escape-Room.git
git push -u origin main
git push origin --tags
```

Create an EMPTY repository for this route (no README/license/gitignore generated
by GitHub). Authenticate to GitHub normally; do not share a token in chat. If the
repository already has commits, do not force-push: ask for help integrating it.
The repository now exists and already contains the project. Do not run these push
commands against it; this section documents archive recovery for a new empty destination.

On the tablet, a GitHub Codespace can provide a terminal and Python environment;
choose only a free allowance and stop it when finished. A Windows PC is another
option. Uploading files through the website alone loses the staged commit history.
