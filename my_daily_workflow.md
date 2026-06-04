# Обновить main из оригинала:

Bash
git checkout main
git fetch upstream       # теперь скачает только main (благодаря фильтрации)
git merge upstream/main --ff-only   # только "fast-forward", чтобы не сломать чистоту
git push origin main     # обновить твой форк

# Работать в learn:

```
Bash
git checkout learn
# Внести изменения, commit, push...
git push origin learn
```

# Синхронизировать learn с новым main:

```
Bash
git checkout learn
git rebase main         # или git merge main, если предпочитаешь merge
git push --force-with-lease origin learn
```
