# v1.6 public release record

This release tracks *Architecture Before the Formula: Individuating Neural Architecture Beyond the Composite Map* at the scientific state published as arXiv:2601.11618v3 and submitted to JMLR on 2026-08-12.

The maintained public source is [`../../paper/`](../../paper/). `SOURCE_SHA256SUMS.txt` fixes the exact maintained scientific source bytes from the frozen v1.6 manuscript. The arXiv v3 upload uses the same scientific body with upload-facing filenames and bibliography packaging. GitHub Actions rebuilds the manuscript from the public source and uploads the fresh PDF as a workflow artifact.

Public archival paper: <https://arxiv.org/abs/2601.11618>

Submission-provenance hashes, recorded for identity without duplicating private submission packages:

- frozen JMLR-submission manuscript PDF: `4fddb69c4ce94d4b45923724fcf0f0b61a01b4c5b76c2e5341c450f13e7e212e`
- validated clean arXiv v3 source ZIP: `76f9eebeda84e4c9e45bce66d4ab6178708ebae27ae2f8a10e35e3590e398b6f`

The public arXiv PDF and local/CI fresh builds need not be byte-identical to the frozen JMLR PDF because their TeX/PDF production environments can differ.
