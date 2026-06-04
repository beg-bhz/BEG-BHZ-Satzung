# BEG-BHZ-Satzung

Satzung und Geschäftsordnungen der **Bürgerenergie Bösingen-Herrenzimmern eG** als Sphinx-Projekt — Quelle in **reStructuredText**, gebaut zu HTML (GitHub Pages) und PDF (Release-Asset).

**Aufbau:** Die Satzung liegt als RST-Files pro Abschnitt in `satzung/01-…rst` bis `satzung/08-…rst`, plus `satzung/99-unterschriften.rst`. Das LaTeX-PDF-Layout orientiert sich an der BWGV-Mustersatzung-PDF (DIN A4, sans-serif, einfache §-Gliederung, Seitennummern unten rechts).

**Stand:** v0 (Mustersatzung-Import 2026-06-04, unverändert aus `BWGV-Mustersatzung für Energiegenossenschaften, Arbeitsversion 2025`). v1.0 = beschlossene Fassung der Gründungsversammlung wird in Folgecommits eingearbeitet.

## Lokal bauen

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

make html        # _build/html/index.html
make pdf         # _build/latex/BEG-BHZ-Satzung.pdf (benötigt TeX Live mit xelatex + lang-german)
make clean
```

## CI

`.github/workflows/publish.yaml` baut bei jedem Push auf `main`:

* HTML → Branch `gh-pages`, live unter <https://beg-bhz.github.io/BEG-BHZ-Satzung/>
* PDF → Workflow-Artifact `BEG-BHZ-Satzung-pdf`

Bei Tag-Push `v*`: PDF zusätzlich als Release-Asset.

## Versionierung

Konvention: Tag `v<MAJOR>.<MINOR>` pro Satzungs-Beschluss.

* `v1.0` — Gründungsversammlung 19.05.2026
* `v1.1` — nächste GV mit Satzungsänderung
* `v2.0` — Reform

## Lizenz

[**CC0 1.0 Universal**](https://creativecommons.org/publicdomain/zero/1.0/) — keine Rechte vorbehalten. Die Satzung darf frei als Vorlage für andere Genossenschaften verwendet, angepasst und weiterverbreitet werden, ohne Attributionspflicht. Volltext in [`LICENSE`](LICENSE).
