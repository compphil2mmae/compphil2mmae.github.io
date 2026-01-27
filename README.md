# Dokumentation zur Website

## Struktur

Das Repo `compphil2maae.github.io` ist öffentlich und enthält im branch `main` lediglich den Quellcode der Website. 

Über einen github-internen workflow in `.github/workflows/publish.yml` wird bei jedem push ins remote über hugo ein statische gitpages-html-Seite erzeugt. Der html-Output der  `/public` und `/resources` directories wird ignoriert. Die Website ist unter https://compphil2mmae.github.io/ erreichbar.

Unter `/data/links.yml` liegt eine Sammlung an Links, die mit `{{< link "link-id" >}}Optionaler Text{{< /link >}}` referenziert werden können. Gedacht ist das insbesondere für Verweise auf Ilias Kurse o. Ä. die sich regelmäßig ändern, um diese nur an einer einzigen Stelle anpassen zu müssen und nichts zu übersehen.

## Vorgehen bei Änderungsvorschlägen

- Typos, kleine Bugs etc. können gern gleich direkt korrigiert werden.
- Bei größerer Eingriffstiefe sollten Änderungen zunächst in einem eigenen branch vorgenommen werden, den man vor Freigabe dann lokal testen und ggf. direkt in `main` mergen kann. 
- Größere Änderungen an Design oder Struktur, die vorheriger Diskussion und Abstimmung bedürfen, oder Probleme, die man nicht *ad hoc* umzusetzen weiß, können gern als issue gepostet werden.  
- Die Issue-List kann gern (mit entsprechenden Tags) auch als eine Art whishlist oder SOMEDAY/MAYBE-Liste dienen.

## Workflow für Implementierung von Änderungen:

1. Pull from `compphil2maae.github.io` 
2. Change website locally
3. check changes by running `hugo server --disableFastRender` or `hugo server --ignoreCache --disableFastRender` (falls Probleme auftauchen)
5. Commit locally
6. Push commit to remote repository `compphil2maae.github.io`
7. wait a couple of minutes & check auto deployment by visiting https://compphil2mmae.github.io/actions

## Editing
To create new content, the clean way ist to run `hugo new content/publication/<my-publication>` (e.g. for a publication, but also for event, post, etc.).  
Alternatively simply copy paste a similar existing file and adjust the front matter.

### Front matter
Ist das definieren vom Aufbau der Seite in Yaml parametern. Wichtigste Optionen sind in der Doku von [Hug Blox](https://docs.hugoblox.com/reference/front-matter/) festgehalten
- `image` Objekte können entweder:
  1. in zweisprachigen Versionen im selben Ordner als `featured.en.png/jpg` & `featured.de.png/jpg` abgelegt werden
  2. universalsprachig im selben Ordner als `featured.png/jpg` abgelegt werden
  3. zur Vermeidung von Redundanzen relativ aus den `/assets/media/` Dateien referenziert werden, z.B. `filename: Logos/isus/utilitarian-flag.png`
     - Soll das Bild aus dem Markdown selber (außerhalb des Front-Matter/---) referenziert werden kann es sein, dass der Pfad inclusive `/media/` angegeben werden muss
     - > aus irgendeinem Grund kann es zu Fehlern führen, wenn die Ordnerstruktur nicht lower-case a-z (ohne Sonderzeichen) ist! Datei selber kann anders benannt werden.
- `.pdf` Objekte können entweder:
  - universalsprachig im selben Ordner als `<ordnername>.pdf` abgelegt werden (priorisiert, wenn nur für einzelne Seite relevant)
  - im static bereich abgelegt werden und mit `url_pdf: <pdfpfad>.pdf` referenziert werden (e.g. `url_pdf: /uploads/hinweise-essays.pdf`)

### Publications
To help import (multiple) new publications, the [academic tool](https://github.com/BuildLore/academic-file-converter) can be used.
1. Install the tool: `pip install -U academic` (python3 is a prerequisite)
2. collect all publications to be imported (e.g. as export from zotero) in a BibTeX file (e.g. use the `content/pubs_to_import.bib` file).  
   - **Tipp:** the more information included here, the less manual work later.
   - Cheatsheet about BibTeX and comprehensive list of available fields can be found [here](https://tug.ctan.org/info/biblatex-cheatsheet/biblatex-cheatsheet.pdf) and explanation of single fields [here](https://www.bibtex.com/format/)
   - <details>
     <summary>recommended ordering</summary>
     
     1. Required Fields
        - `author` is a list of author names ("Surname, Firstname" connected by and)
        - `title` is the title of the publication
        - `subtitle` is the subtitle of the publication
        - `year` is the year of publication
        - `journal`/`booktitle` is the name of the journal or book
        - `editor` is a list of editors
        - `translator` list of translators if applicable
     2. Publication Details
        - `series` is the series of the publication
        - `volume` is the volume number
        - `number` is the issue number
        - `pages` is the page range
        - `chapter` is the chapter number
        - `edition` is the edition of the publication
        - `month`/`date` is the month/date (yyyy-mm-dd) of publication
     3. Publisher Information
        - `publisher` is the publisher of the publication
        - `address`/`location` is the address of the publisher
        - `institution`/ `organization`/ `school` to store the institution of the publication
        - `howpublished` to store a notice for unusual publications
     4. Identifiers & Links
        - `doi` is the DOI of the publication
        - `isbn` is the ISBN of the publication
        - `issn` is the ISSN of the publication
        - `url` is the URL of the publication
     5. Metadata
        - `abstract` of available
        - `keywords` is a list of keywords for the publication
        - `language` the language of the publication
        - `type` specifies the type of the publication more detailed/descriptive that the BibTeX entry type
     6. Miscellaneous
        - `note`(/`annote`) is a note/annotation for the publication

      </details>
3. run the tool: `academic import <path-to-bibtex-file> content/publication/`
4. transfer relevant parameter (e.g. volume, number, pages for articles) from the created `cite.bib` file to the `index.md` file, that are not autmatically transferred by the import (Only the parameter specified [here](https://github.com/BuildLore/academic-file-converter/blob/main/academic/templates/publication.md) are automatically adopted - and also only if present)
   <details>
   <summary>auto transferred</summary>
   
   `title`, `authors`, `author_notes`, `date`, `publishDate`, `publication_types`, `publication`, `publication_short`, `doi`, `abstract`, `summary`, `tags`, `featured`, `url_pdf	url_code`, `url_dataset`, `url_poster`, `url_project`, `url_slides`, `url_source`, `url_video`, `image`, `projects`
   </details>
   
   **author needs to be corrected if has an own page**
   
   optional additional parameters (need for manual transfer):
     - volume, number, pages (for articles)
     - publisher, if different than 'publication'
     - address
     - series
     - editor
     - note
5. *Optionally:*
   - add project affiliation
   - add content tag/kewords (also to `cite.bib`)
   - add abstract (also in `cite.bib`)
   - add PDF (add to publication sites folder, rename pdf to folder name or reference pdf with links, like in [front matter](#front-matter))
   - add other links
     - DOI link is auto generated if correctly specified in original `cite.bib` or set as parameter `doi` in `index.md`
     - PDF & Cite links are auto generated if files correctly placed and named in publication sites folder (`<foldername>.pdf` and `cite.bib` - latter is he case when imported)
     - Convention so far - use [academicon](https://jpswalsh.github.io/academicons/) if available (e.g. `springer`, `philpaper`) and name for the Link as follows (with `ai` as icon_pack), for open access publications use `openaccess` as icon name + `URL` when referenced
     ```yaml
     links:
     # e.g. for Springer links
     - name: URL
       icon: springer
       icon_pack: ai
       url: https://link.springer.com/article/10.1007/s11229-023-04415-9
     ```
   - add image/thumbnail (see [front matter](#front-matter) `image`)
   - add summary (preview in list views and links)
   - edit the sites content (e.g. add abstract, keypoints/insights, outcomes)
6. duplicate `index.md` file and adjust to german/english version so you get `index.en.md` and `index.de.md`


### Shortcodes
Sind kleine html snippets die zur Wiederverwendung unter `/layouts/shortcodes/` definiert werden und einfach mit `{{< shortcode-id >}}` und ggf. parametern in den Markdown-Texten aufgerufen werden können.
Einige hilfreiche vordefinierte utilities sind in den [Hugo Docs](https://gohugo.io/content-management/shortcodes/) ausführlich beschrieben.  
Zusätzlich wurde ein shortcode `link` definiert, der auf die Links in `/data/links.yml` zugreift, um regelmäßig wechselnde Links (e.g. Ilias Kurse des aktuellen Semesters) zu verwalten & auf eimnal an allen vorkommenden Stellen ändern zu können.
