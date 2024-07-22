# Dokumentation zur Website

## Struktur

Das Repo `compphil2maae.github.io` ist öffentlich und enthält im branch `main` lediglich den Quellcode der Website. 

Über einen github-internen workflow in `.github/workflows/publish.yml` wird bei jedem push ins remote über hugo ein statische gitpages-html-Seite erzeugt. Der html-Output der  `/public` und `/resources` directories wird ignoriert. Die Website ist unter https://compphil2mmae.github.io/ erreichbar.

## Vorgehen bei Änderungsvorschlägen

- Typos, kleine Bugs etc. können gern gleich direkt korrigiert werden.
- Bei größerer Eingriffstiefe sollten Änderungen zunächst in einem eigenen branch vorgenommen werden, den man vor Freigabe dann lokal testen und ggf. direkt in `main` mergen kann. 
- Größere Änderungen an Design oder Struktur, die vorheriger Diskussion und Abstimmung bedürfen, oder Probleme, die man nicht *ad hoc* umzusetzen weiß, können gern als issue gepostet werden.  
- Die Issue-List kann gern (mit entsprechenden Tags) auch als eine Art whishlist oder SOMEDAY/MAYBE-Liste dienen.

## Workflow für Implementierung von Änderungen:

1. Pull from `compphil2maae.github.io` 
2. Change website locally
3. check changes by running `hugo server --disableFastRender`
5. Commit locally
6. Push commit to remote repository `compphil2maae.github.io`
7. wait a couple of minutes & check auto deployment by visiting https://compphil2mmae.github.io

