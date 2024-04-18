# Dokumentation zur Website

## Struktur

Die Website ist intern über zwei repositories auf github organisiert:

1. `compphil2maae_source`: privat, enthält den Quellcode der Website, darunter auch mit `hugo` erzeugten statischen Teil im `public` directory, der über eine github-action in das öffentliche Repo `compphil2maae` gepusht wird;

2. `compphil2maae`: öffentlich, hier wird die Website gemounted (see baseurl in `/config/default/hugo.yaml`) und ist von außen abrufbar (automatisches deployment durch gitpages).

Dies ist das Repository `compphil2maae_source`.

## Workflow für Änderungen:

1. Pull from `compphil2maae_source` 
2. Change website locally
3. Run `hugo` (without server!) locally
   - Notabene: Bei größeren Löschungen muss man evtl. zuvor `/public` und `/resources` directories löschen
4. [evtl.] check changes
   - run `hugo server --disableFastRender`
5. Commit locally
6. Push commit to remote repository `compphil2maae_source`
7. execute github action
   - [TBD] see https://www.mytechramblings.com/posts/create-a-website-with-hugo-and-gh/ or https://github.com/marketplace/actions/push-a-directory-to-another-repository
   in `compphil2maae_source` to push `/public` directory to `compphil2maae`.
