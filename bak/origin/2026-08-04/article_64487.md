# Release: datasette-apps 0.2a0

### Summary
The `0.2a0` release of `datasette-apps` introduces new tooling designed to enhance the integration between Datasette Apps and [Datasette Agent](https://agent.datasette.io/). These updates empower the agent to programmatically inspect, test, and manage applications through new specialized tools.

---

### Key Changes
*   **`app_debug()` Tool:** Enables the agent to open an app invisibly to perform automated testing and inspection via JavaScript.
*   **`app_list()` Tool:** Provides the agent with the ability to list apps that the user has permission to edit, facilitating easier management.

### Technical Highlights
The new `app_debug()` functionality is a sophisticated addition to the Datasette ecosystem. It operates by rendering the target app within an `opacity: 0` iframe with `pointer-events: none`. This creates a "headless" environment where the agent can:
*   Execute sandboxed JavaScript to perform smoke tests.
*   Measure element dimensions and verify layout integrity.

This feature leverages the `context.browser_task()` mechanism, which was recently introduced in [datasette-agent 0.4a0](https://simonwillison.net/2026/Jul/31/datasette-agent/).

---

### References
*   [Release Notes (GitHub)](https://github.com/datasette/datasette-apps/releases/tag/0.2a0)
*   [Pull Request #33: app_debug()](https://github.com/datasette/datasette-apps/pull/33)
*   [Issue #36: app_list()](https://github.com/datasette/datasette-apps/issues/36)

**Tags:** #iframes #datasette #datasette-apps