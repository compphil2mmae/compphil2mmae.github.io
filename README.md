# Dokumentation zur Website

## Struktur

Die Website ist intern über zwei repositories auf github organisiert:

1. `compphil2maae_source`: privat, enthält den Quellcode der Website, darunter auch mit `hugo` erzeugten statischen Teil im `public` directory, der in das öffentliche Repo `compphil2maae` gepusht wird;

2. `compphil2maae`: öffentlich, hier wird die Website gemounted (see baseurl in `/config/default/hugo.yaml`) und ist von außen abrufbar (deployment durch gitpages).

Dies ist das Repository `compphil2maae_source`.

## Workflow für Änderungen:

1. Pull from `compphil2maae_source` 
2. Change website locally
3. Run `hugo server --disableFastRender` locally
   Note: evtl. zuvor `/public` und `/resources` directories löschen
4. Check changes 
5. Commit locally
6. Push commit to remote repository `compphil2maae_source`
7. *Either*
   1. copy `/public` directory (locally) into `compphil2maae` 
   2. push local `compphil2maae` to remote 
   *or*
   1. [to be done] define github action as in https://www.mytechramblings.com/posts/create-a-website-with-hugo-and-gh/
