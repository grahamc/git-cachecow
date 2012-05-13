Caches git repositories locally. Every time a build happens, it uses local
caches for pulling. Submodules especially, which are harder to intercept
for caching.

Will also inflate submodules recursively.

With 8 submodules, a total of 150MB of data to clone:

Before caching: `13.79s user 6.36s system 18% cpu 1:49.45 total`

After caching: `2.12s user 2.07s system 25% cpu 16.310 total`

How to clone a repository:

`gsclone git://github.com/grahamc/git-multi.git`

## cachehash.sh
`cachehash.sh repo_uri [clone_to [hash]]`

## smartsub.py

Outputs submodule data into parsable format

```
git://github.com/nationalfield/symfony.git  lib/vendor/symfony  aec67b5e7ba148c79b884b86988e42f9f9483bcd
git@github.com:nationalfield/pheanstalk.git lib/vendor/pheanstalk   5b38924730b70ea720f760369899398479e2ea13
git@github.com:nationalfield/tinymce.git    web/js/tiny_mce 0c3da0cc9e33df0f2b82f70bf7e24405de216bee
```

## smartsub-clone.py
 Clones all the submodules recursively attheir defined location and hashes.

