# Changelog

The releases this repository pins, newest first, in the form of [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
A pin move is recorded here, not in decisions/.

## [Unreleased]

### Changed

- Pinned reader-ergonomics v1.24.3 (`722cfa4`), from v1.24.2 (`65e4247`): a SICI DOI is read whole and a server error is a warning, not an error. The links of the text move with the pin.
- Pinned reader-ergonomics v1.24.2 (`65e4247`), from v1.21.0 (`2e5b6f0`): fixes that remove false findings in the sentence, term and figure checks, and `[defined_terms] cues`.

### Fixed

- The OFT1489 link in the bibliography, whose address at the National Archives answers HTTP 405 behind a human-verification wall (an AWS WAF challenge page), now points to the Internet Archive's copy of the same PDF, captured on 26 Nov. 2013 at the OFT's own address.

## [0.1.0] - 2026-11-04

### Added

- The first reviewed release. It holds the first review of the topic (`evidence/willingness-to-pay/`: frame, protocol, sources, review, case against, state of the art, position and baseline). It also holds the shared bibliography and the front pages with the findings and baseline.
- Tag v0.1.0 and a GitHub release of the same name.

## 2026-11-04

### Added

- Pinned reader-ergonomics v1.21.0 (`2e5b6f0`), at the repository's start: the standard's pin, link, changelog and
  decision-record checks, which this skeleton is written to pass.
