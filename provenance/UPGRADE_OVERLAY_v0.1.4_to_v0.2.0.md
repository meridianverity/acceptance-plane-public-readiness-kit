# Upgrade Overlay — v0.1.4 to v0.2.0

Boundary: public readiness material only. Not implementation, standard, certification kit, compliance approval, patent license, or production allow/deny system.

This note is included so a v0.1.4 checkout can receive the v0.2.0 overlay and still pass manifest verification after listed stale release-face files are removed.

After applying the overlay, remove the paths listed in `provenance/DELETED_FILES_v0.1.4_to_v0.2.0.txt`, then run:

```bash
make qa-full
```
