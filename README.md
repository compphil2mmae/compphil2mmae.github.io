# Dokumentation zur Website

Die Website ist intern über zwei repositories auf github organisiert:

1. `compphil2maae_source`: privat, enthält den Quellcode der Website, darunter auch mit `hugo` erzeugten statischen Teilim `public`-folder, der in das öffentliche Repo `compphil2maae` gepusht wird;

2. `compphil2maae`: öffentlich, hier wird die Website gemounted (see baseurl in `/config/default/hugo.yaml`) und ist von außen abrufbar (deployment durch gitpages).

Dies ist das Repository `compphil2maae_source`.
