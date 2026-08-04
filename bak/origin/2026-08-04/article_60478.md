# Release: shot-scraper 1.11

### Summary
The 1.11 release of `shot-scraper` introduces several usability improvements, focusing on command consistency and more robust server handling. Key updates include a more resilient startup process for local servers and the addition of flexible JavaScript loading options across multiple commands.

---

### Key Improvements

*   **Robust Server Startup:** Processes using the `server:` mechanism (in `shot-scraper multi` and `shot-scraper video`) now feature a more reliable startup sequence. Instead of a fixed one-second delay, the tool now polls for port availability and waits up to 30 seconds for the target URL to accept connections. ([#197](https://github.com/simonw/shot-scraper/issues/197))
*   **Flexible JavaScript Loading:** A new `--js-file` option has been added to the `shot-scraper`, `pdf`, `html`, `accessibility`, and `har` commands. This allows users to load JavaScript from a local file, standard input, or a GitHub Gist (`gh:username/script`) as an alternative to passing raw strings via `--javascript`. ([#192](https://github.com/simonw/shot-scraper/issues/192))
*   **YAML Support:** The `shot-scraper multi` command now supports the `js_file:` key in its configuration.
*   **Command Consistency:** The `shot-scraper javascript` and `shot-scraper html` commands have been updated to include a `--timeout` option, bringing them in line with the rest of the toolset. ([#118](https://github.com/simonw/shot-scraper/issues/118))

---

**Links:** [Official Release Notes](https://github.com/simonw/shot-scraper/releases/tag/1.11) | **Tags:** #shot-scraper