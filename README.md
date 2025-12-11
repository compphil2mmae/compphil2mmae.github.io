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
### Front matter
Ist das definieren vom Aufbau der Seite in Yaml & parametern. Wichtigste Optionen sind in der Doku von [Hug Blox](https://docs.hugoblox.com/reference/front-matter/) festgehalten
- `image` Objekte können entweder:
  1. in zweisprachigen Versionen im selben Ordner als `featured.en.png/jpg` & `featured.de.png/jpg` abgelegt werden
  2. universalsprachig im selben Ordner als `featured.png/jpg` abgelegt werden
  3. zur Vermeidung von Redundanzen relativ aus den `/assets/media/` Dateien referenziert werden, z.B. `filename: Logos/isus/utilitarian-flag.png`
     - Soll das Bild aus dem Markdown selber (außerhalb des Front-Matter/---) referenziert werden kann es sein, dass der Pfad inclusive `/media/` angegeben werden muss
     - > aus irgendeinem Grund kann es zu Fehlern führen, wenn die Ordnerstruktur nicht lower-case a-z (ohne Sonderzeichen) ist! Datei selber kann anders benannt werden.

### Shortcodes
Sind kleine html snippets die zur Wiederverwendung unter `/layouts/shortcodes/` definiert werden und einfach mit `{{< shortcode-id >}}` und ggf. parametern in den Markdown-Texten aufgerufen werden können.
Einige hilfreiche vordefinierte utilities sind in den [Hugo Docs](https://gohugo.io/content-management/shortcodes/) ausführlich beschrieben.
