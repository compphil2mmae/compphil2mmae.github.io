# Dokumentation zur Website

## Struktur

Das Repo `compphil2maae.github.io` ist öffentlich und enthält im branch `main` lediglich den Quellcode der Website. 

Über einen github-internen workflow (in `.github/workflows/publish.yml` wird bei jedem push ins remote über hugo ein statische gitpages-html-Seite erzeugt. Der html-Output der  `/public` und `/resources` directories wird ignoriert. Die Website ist unter https://compphil2mmae.github.io/ erreichbar.


## Workflow für Änderungen:

1. Pull from `compphil2maae.github.io` 
2. Change website locally
3. check changes by running `hugo server --disableFastRender`
5. Commit locally
6. Push commit to remote repository `compphil2maae.github.io`
7. wait a couple of minutes & check auto deployment by visiting https://compphil2mmae.github.io

