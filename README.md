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

### Publications
To help import (multiple) new publications, the [academic tool](https://github.com/BuildLore/academic-file-converter) can be used.
1. Install the tool: `pip install -U academic` (python3 is a prerequisite)
2. collect all publications to be imported (e.g. as export from zotero) in a BibTeX file.  
   - **Tipp:** the more information included here, the less manual work later.
3. run the tool: `academic import <path-to-bibtex-file> content/publication/ --compact`
4. transfer relevant parameter (e.g. volume, number, pages for articles) from the created `cite.bib` file to the `index.md` file.  
   <details><summary>Only the parameter listed [here](https://github.com/BuildLore/academic-file-converter/blob/main/academic/templates/publication.md) are automatically transferred to the `index.md` file from the BibTeX file - and also only if present:</summary>  
   `title`, `authors`, `author_notes`, `date`, `publishDate`, `publication_types`, `publication`, `publication_short`, `doi`, `abstract`, `summary`, `tags`, `featured`, `url_pdf	url_code`, `url_dataset`, `url_poster`, `url_project`, `url_slides`, `url_source`, `url_video`, `image`, `projects`)
   </details>
   
   - optional parameters are:
     - volume, number, pages (for articles)
     - publisher, if different than 'publication'
     - address
     - series
     - editor
     - note
5. *Optionally:*
   - add project affiliation
   - add content tag/kewords (also to `cite.bib`)
   - add PDF (add to publication sites folder, rename pdf to folder name or reference pdf in [front matter](#front-matter))
   - add other links, image/thumbnail, summary  
     ```yaml
     # for links modify following, for images and summary edit existing parameters
     links:
     - name: URL
       icon: springer
       icon_pack: ai
       url: https://link.springer.com/article/10.1007/s11229-023-04415-9
     ```
   - edit the sites content (e.g. add abstract, keypoints/insights, outcomes)
6. duplicate `index.md` file and adjust to german/english version so you get `index.en.md` and `index.de.md`


### Shortcodes
Sind kleine html snippets die zur Wiederverwendung unter `/layouts/shortcodes/` definiert werden und einfach mit `{{< shortcode-id >}}` und ggf. parametern in den Markdown-Texten aufgerufen werden können.
Einige hilfreiche vordefinierte utilities sind in den [Hugo Docs](https://gohugo.io/content-management/shortcodes/) ausführlich beschrieben.  
Zusätzlich wurde ein shortcode `link` definiert, der auf die Links in `/data/links.yml` zugreift, um regelmäßig wechselnde Links (e.g. Ilias Kurse des aktuellen Semesters) zu verwalten & auf eimnal an allen vorkommenden Stellen ändern zu können.
