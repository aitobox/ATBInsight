# Wheels, Bottles, and Images: The Architecture of Binary Distribution

### Summary
This article explores the convergence of three major self-service binary distribution systems: Python **Wheels**, Homebrew **Bottles**, and OCI **Container Images**. While these systems evolved independently to serve different ecosystems, they share a fundamental architecture: the distribution of immutable, checksummed artifacts selected by client-side platform tags. The piece analyzes their shared technical foundations, their divergent approaches to dependency management, and the ongoing trend toward using OCI registries as a universal storage backend for diverse binary formats.

---

### Similarities
Despite their different origins, these three systems share a common operational model:
*   **Content-Addressed Distribution:** All three rely on downloading immutable, checksummed files (zip, tar.gz, or layers) over HTTP. The integrity is verified via hashes (SHA256 or digests) rather than server-side inspection.
*   **Decoupled Storage:** The index (the "catalog") is separate from the artifact storage. This allows registries to migrate storage backends (e.g., Homebrew moving from Bintray to GitHub Packages) without breaking client functionality.
*   **Client-Side Selection:** Clients (pip, brew, or container runtimes) are responsible for inspecting the host environment and selecting the appropriate artifact based on platform tags or manifests.
*   **Metadata and Provenance:** Each format includes a metadata document (e.g., `.dist-info`, `INSTALL_RECEIPT.json`, or OCI config) and is increasingly adopting **Sigstore** for digital attestations to ensure supply chain security.

### Differences
The systems diverge primarily in how they handle the host environment and dependency resolution:
*   **Dependency Models:** Wheels and bottles are part of a dependency graph; pip and brew resolve these trees before installation. OCI images, conversely, are monolithic; they contain a filesystem and have no native dependency resolution at pull time.
*   **Fallback Mechanisms:** When a pre-compiled artifact is missing, pip and brew can build from source (sdist or formula). OCI images do not have a standard "build-from-source" mechanism at the registry level; if the image isn't there, the pull fails.
*   **Host Requirements:** Wheels and bottles assume a degree of host-side compatibility (libc, OS version, install prefix), whereas images are designed to be self-contained, requiring only a compatible kernel.

### Convergence and the Future
The industry is trending toward a unified infrastructure for binary distribution:
*   **OCI as a Universal Backend:** Homebrew and Helm have already moved to storing artifacts in OCI registries. Because OCI registries treat blobs as opaque media types, they can host bottles, charts, and potentially other formats without requiring registry-side changes.
*   **The "Tag" Challenge:** A significant hurdle remains in how these systems define platform compatibility. Current tag grammars are ecosystem-specific and often fail to account for modern hardware requirements like GPU architectures, SIMD levels, or specific BLAS libraries.
*   **Standardization:** Efforts like **PEP 817** (variant wheels) and the **PURL** (Package URL) specification for cross-ecosystem platform qualifiers represent the next phase of evolution. The goal is to move toward a standardized way of describing hardware capabilities so that installers can make smarter, more granular decisions at the time of deployment.

Ultimately, the core design work for future binary distribution systems is narrowing. The "blob" storage problem is largely solved by OCI registries; the remaining challenge lies in standardizing the metadata and tag grammars that allow these systems to communicate across ecosystem boundaries.