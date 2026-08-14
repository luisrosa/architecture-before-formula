# Current paper source — v1.6

This directory contains the current public source for *Architecture Before the Formula: Individuating Neural Architecture Beyond the Composite Map*.

The maintained manuscript body is byte-identical to the frozen v1.6 scientific source. The public archival manuscript is arXiv:2601.11618v3; its upload packet uses the same scientific body with upload-facing file naming and bibliography packaging. The exact frozen JMLR-submission PDF is identified by SHA-256 in `../releases/v1.6/README.md`; private submission-administration materials are not duplicated here.

## Build

```bash
bash ./build.sh
```

The build retrieves the official `jmlr2e.sty` file from a pinned upstream JMLR style-file commit, then uses the standard TeX packages named by the manuscript source. The style file is a third-party build dependency rather than part of the manuscript source.
