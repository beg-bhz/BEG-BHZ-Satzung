# BEG-BHZ-Satzung

Satzung der **Bürgerenergie Bösingen-Herrenzimmern eG** als Sphinx-Projekt — Quelle in **reStructuredText**, gebaut zu HTML (GitHub Pages) und PDF (Release-Asset).

**Aufbau:** Die Satzung liegt als RST-Files pro Abschnitt in `satzung/01-firma-zweck.rst` bis `satzung/08-gerichtsstand.rst`. Das LaTeX-PDF-Layout: DIN A4, sans-serif (DejaVu Sans), einfache §-Gliederung, Seitennummern unten rechts.

**Stand:** v1.0 (beschlossen von der Gründungsversammlung 19.05.2026; aktuell zur Prüfung beim BWGV).

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
