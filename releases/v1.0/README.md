# Architecture Before the Formula v1.0

Release artifacts for the first maintained public release.

- [Main paper](Architecture_Before_the_Formula_v1.0.pdf)
- [Technical supplement](Architecture_Before_the_Formula_v1.0_Technical_Supplement.pdf)
- [Clean source package](Architecture_Before_the_Formula_v1.0_Source.zip)
- [SHA-256 checksums](SHA256SUMS.txt)

## Checksums

`ac00c54111d65879e3f414ded92491bde8f3973c6ad43bd16eb1d4e68f5a36b0` - main paper  
`471c74d266ad80d0c8eaee3bc96d4cea3eb806e6add023ee4cf3dc61f49ef685` - technical supplement  
`328ea750c2cbb3163d0ed172c50f29ca4e425d5d7d600ea19eefded77eb38244` - clean source package

The source ZIP excludes compiled PDFs, generated LaTeX products, release artifacts, repository history, and CI-only files. It is built deterministically from the maintained source tree and audited in CI.

These files are the frozen v1.0 release artifacts. Current-source rebuilds are validated independently for structure and semantics; byte-identical PDF output across moving TeX environments is not part of the release claim.
