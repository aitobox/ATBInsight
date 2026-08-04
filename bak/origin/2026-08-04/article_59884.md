# Package Management as Org Chart

> **Summary:** Conway’s Law dictates that organizations produce systems that mirror their communication structures. Dependency management tooling is no exception. A resolution strategy is merely an opinion on how interpersonal disagreements are settled, while a manifest format records who holds the power to depend on whom. Ultimately, most dependency strategies are simply attempts to avoid human negotiation; the tooling doesn't remove the disagreement—it just hardcodes who loses by default.

---

## The Spectrum of Organizational Dependency Strategies

### Monorepo, Single Version Policy
Every package in the tree must agree on one version of each dependency; upgrading anything means upgrading everyone at once. 
* **The Org Dynamic:** The org chart has been forbidden from appearing in the code. It only works when there is a standing migration workforce whose sole job is dragging every consumer along.

### Monorepo with Workspaces
One repository, but each package keeps its own manifest and can pin its own versions. 
* **The Org Dynamic:** Managed by one strong platform team, backed by leadership that genuinely believes coordination was entirely solved at the 2019 offsite.

### Git Submodules
A dependency is referenced by an exact commit SHA in a separate repository, and updating it is a manual, two-step process that never gets automated. 
* **The Org Dynamic:** Two teams agreed to collaborate and recorded, down to the exact commit hash, precisely how little they meant it.

### Bazel
Every dependency edge between targets is explicitly declared in a `BUILD` file; nothing is ambient or inferred. 
* **The Org Dynamic:** Adopted when the organization grew past the point where anyone knew who depended on whom by simply asking. The build system was invoked to brutally enforce what humans had lost track of. Typically legible to exactly one person, who used to work at Google.

### Nix / Guix
Builds are pure functions of their declared inputs; anything not listed in the derivation simply doesn’t exist at build time. 
* **The Org Dynamic:** "Works on my machine" has been made a structurally impossible sentence—achieved at the direct cost of most of the hiring pipeline.

### Maven Nearest-Wins Mediation
When two paths through the tree want different versions of the same artifact, Maven picks whichever path is fewer hops from the root, regardless of which is newer or satisfies more constraints. 
* **The Org Dynamic:** Conflict resolution by proximity to the top—which happens to be how the organization settles most disagreements anyway.

### Artifactory with Private Forks
Every install goes through a proxy controlled by the org, and packages that needed patching were forked in rather than contributed back upstream. 
* **The Org Dynamic:** Trust is granted by a centralized system rather than a person. The forks date back to an argument Legal won years ago and hasn't been reopened since.

### `deb`/`rpm` Packages for In-House Apps
The application is built into an OS package, installed by the system package manager, and releasing goes through the exact same strict gate as a kernel update. 
* **The Org Dynamic:** Operations won, and has governed ever since. Releases are formal events accompanied by a runbook and at least one person whose job title contains the word “release.”

### Docker
The application ships with its own isolated copy of the operating system, meaning the deployment environment is whatever the developer decided at build time. 
* **The Org Dynamic:** Development seceded from Operations and took the OS with them. Ops can no longer reject an artifact that conveniently contains everything Ops used to control. The company only finds out how many separate copies of Debian it is running when the next `xz`-style vulnerability drops.

### Terraform Modules from a Private Registry
Infrastructure is packaged as versioned modules that application teams consume just like any other software dependency. 
* **The Org Dynamic:** The infrastructure team built an interface so application teams would finally stop paging them, and now they just get constantly paged about the interface instead.

### [Module Federation](https://module-federation.io/)
Separately built and deployed JavaScript bundles negotiate shared dependency versions with each other at runtime, right there in the browser. 
* **The Org Dynamic:** The teams report to different VPs who refuse to share a single meeting, so version resolution was deferred to the absolute last possible moment—on the user’s machine—because agreement couldn't be reached anywhere earlier in the pipeline.

### `peerDependencies`
The package declares a version constraint on a dependency its host must provide, without shipping anything to satisfy it. 
* **The Org Dynamic:** A framework team issuing sweeping policy down to application teams: *"You will be on React 18, we will check, and satisfying the constraint is entirely your problem."*

### Vendored Dependencies
The source code of each dependency is copied directly into the repository and committed; upstream can change or vanish without effect. 
* **The Org Dynamic:** An organization that was deeply burned by an upstream provider once and now takes structural hostages. The cost is a manual merge conflict that lives permanently in the next sprint.

### No Lockfile, `latest` Everywhere
Each install resolves fresh against the registry, and the dependency set is whatever happens to be newest at that exact moment. 
* **The Org Dynamic:** The founder still commits directly to `main`, had a single bad experience with `npm-shrinkwrap.json` years ago, and categorically refuses to touch a lockfile.

### `semantic-release` on Every Merge
The version number is automatically computed from [Conventional Commits](https://www.conventionalcommits.org/) prefixes, and a release is cut instantly whenever `main` changes. 
* **The Org Dynamic:** Publishing became a mindless side effect of the commit prefix, because being the human responsible for cutting a release had become an intolerable liability.

### Go MVS (Minimal Version Selection)
Resolves each dependency to the lowest version anything in the graph explicitly requires, and no higher; nothing upgrades just because a newer version exists. 
* **The Org Dynamic:** Designed by someone who looked at complex SAT-solver resolution and concluded the problem was entirely self-inflicted. It encodes an organization where change only happens when someone officially puts the requirement in writing.

### Brewfile
The entire development environment is declared as a list of Homebrew packages that `brew bundle` installs sequentially. 
* **The Org Dynamic:** Onboarding functions as an initiation ritual: the file invariably fails on line 14, and the actual mechanism for getting a working machine is a Slack thread appropriately named `#dev-setup-help`.

---

> *Most dependency strategies are attempts to avoid interpersonal negotiation. The tooling doesn’t remove the disagreement—it just picks who loses by default.*