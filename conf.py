"""Sphinx-Konfiguration: Satzung der Bürgerenergie Bösingen-Herrenzimmern eG"""

import os
from datetime import datetime

# -- Project information -----------------------------------------------------

project = "BEG-BHZ-Satzung"
# Anzeigename — wandert in den LaTeX-Header, ins Titelblatt und in den HTML-Titel.
# Bis zur v1.0-Anpassung steht hier die Quelle (BWGV-Mustersatzung).
# Bei v1.0 auf "Bürgerenergie Bösingen-Herrenzimmern eG — Satzung" umstellen.
projectname = "BWGV-Mustersatzung Energiegenossenschaften (Arbeitsversion 2025)"
author = "Baden-Württembergischer Genossenschaftsverband (Vorlage); BEG-BHZ (Anpassungen)"
copyright = f"{datetime.now().year}, BWGV-Vorlage / Anpassungen Bürgerenergie Bösingen-Herrenzimmern eG"
release = os.getenv("DOC_RELEASE", "v0.1 Mustersatzung-Import")

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.githubpages",
]

source_suffix = {".rst": "restructuredtext"}
master_doc = "index"
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "README.md"]
language = "de"
smartquotes = True
today_fmt = "%d.%m.%Y"
todo_include_todos = True

# Numbered figures/tables
numfig = True

# Kein Auto-Section-Numbering — die §-Nummerierung kommt aus den Satzungs-Titeln selbst


# -- HTML output -------------------------------------------------------------

html_theme = "furo"
html_title = projectname
html_static_path = ["_static"]
html_css_files = ["css/beg.css"]

html_theme_options = {
    "sidebar_hide_name": False,
    "navigation_with_keys": True,
    "source_repository": "https://github.com/beg-bhz/BEG-BHZ-Satzung/",
    "source_branch": "main",
    "source_directory": "/",
}

# -- LaTeX / PDF output ------------------------------------------------------
# Ziel: PDF, das im Aufbau und in der Anmutung der BWGV-Mustersatzung-PDF
# nahekommt (DIN A4, sans-serif Schrift wie Arial, einfache Gliederung,
# Inhaltsverzeichnis, Seitennummern unten rechts).

latex_engine = "xelatex"

latex_documents = [
    ("index", f"{project}.tex", projectname, author, "manual"),
]

latex_elements = {
    "papersize": "a4paper",
    "pointsize": "11pt",
    "extraclassoptions": "openany,oneside",
    "fontpkg": r"""
        \usepackage{fontspec}
        \setmainfont{DejaVu Sans}[Scale=0.95]
        \setsansfont{DejaVu Sans}[Scale=0.95]
        \setmonofont{DejaVu Sans Mono}[Scale=0.90]
    """,
    "preamble": r"""
        \usepackage{polyglossia}
        \setmainlanguage[spelling=new]{german}
        \usepackage{microtype}

        % Aktive Silbentrennung — sonst werden Zusammensetzungen wie
        % „Auseinandersetzungsguthaben" oder „Generalversammlung" nicht umbrochen.
        \tolerance=1500
        \emergencystretch=3em
        \hyphenpenalty=50
        \exhyphenpenalty=50
        \hbadness=2000

        % Manuelle Trennhinweise für Genossenschafts-Vokabular
        % (XeLaTeX + Polyglossia/german matched gegen UTF-8 — die Patterns
        % müssen mit echten Umlauten geschrieben sein, sonst greifen sie nicht.)
        \hyphenation{
          Ge-nos-sen-schaft Ge-nos-sen-schafts-ge-setz
          Ge-schäfts-an-teil Ge-schäfts-gut-ha-ben Ge-schäfts-füh-rer
          Ge-ne-ral-ver-samm-lung Auf-sichts-rat Auf-sichts-rats-mit-glied
          Vor-stand Vor-stands-mit-glied Vor-stands-mit-glie-der
          Mit-glied-schaft Mit-glie-der-lis-te
          Aus-ein-an-der-set-zung Aus-ein-an-der-set-zungs-gut-ha-ben
          Be-schluss-fas-sung Be-kannt-ma-chung
          Jah-res-ab-schluss Jah-res-über-schuss Jah-res-fehl-be-trag
          Ka-pi-tal-rück-la-ge Er-geb-nis-rück-la-ge
          Prä-senz-ver-samm-lung In-sol-venz-ver-fah-ren
        }

        % Keine Auto-Section-Numbering im LaTeX/PDF — §-Nummern stehen in den Titeln
        \setcounter{secnumdepth}{-2}
        \setcounter{tocdepth}{3}

        % Sans-serif Headings (passt zur Body-Font)
        \usepackage{titlesec}
        \titleformat{\chapter}[block]{\Large\bfseries}{\thechapter}{0.6em}{}
        \titleformat{\section}{\large\bfseries}{}{0pt}{}
        \titleformat{\subsection}{\normalsize\bfseries}{}{0pt}{}

        % Listen-Abstände kompakt halten
        \usepackage{enumitem}
        \setlist{nosep,topsep=4pt,parsep=2pt,partopsep=0pt}

        % Seitennummern unten rechts, kein Header
        \usepackage{fancyhdr}
        \fancypagestyle{normal}{%
          \fancyhf{}%
          \fancyfoot[R]{\thepage}%
          \renewcommand{\headrulewidth}{0pt}%
          \renewcommand{\footrulewidth}{0pt}%
        }
        \fancypagestyle{plain}{%
          \fancyhf{}%
          \fancyfoot[R]{\thepage}%
          \renewcommand{\headrulewidth}{0pt}%
          \renewcommand{\footrulewidth}{0pt}%
        }

        % TOC-Heading auf "Inhaltsverzeichnis" (Sphinx übernimmt sonst den ersten
        % toctree-Caption als \contentsname)
        \addto\captionsgerman{\renewcommand{\contentsname}{Inhaltsverzeichnis}}
    """,
    "sphinxsetup": (
        "hmargin={1in,1in}, vmargin={1in,1in}, "
        "verbatimwithframe=true, "
        "TitleColor={rgb}{0,0,0}, "
        "InnerLinkColor={rgb}{0,0,0}, "
        "OuterLinkColor={rgb}{0,0,0.5}"
    ),
    "maketitle": r"""
        \begin{titlepage}
        \centering
        \vspace*{6cm}
        {\Large\bfseries BWGV-MUSTERSATZUNG\par}
        \vspace{1cm}
        {\large für\par}
        \vspace{0.5cm}
        {\Large\bfseries Energiegenossenschaften\par}
        \vspace{2cm}
        {\large Arbeitsversion\par}
        \vspace{0.5cm}
        {\normalsize (Stand: 2025)\par}
        \vspace{2cm}
        {\small Import-Stand für das BEG-BHZ-Satzungs-Repo: \today \par}
        \end{titlepage}
    """,
}
