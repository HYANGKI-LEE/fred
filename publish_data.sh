#!/usr/bin/env bash
# output/db/*.db.gz 를 data 브랜치에 '이력 없는 커밋 하나'로 덮어써 올린다 (force push).
# DB가 매일 바뀌어도 리포 용량이 쌓이지 않게 하려는 것. 코드는 main, 데이터는 data 브랜치.
# 원본 .db 는 GitHub 파일 크기 제한(100MB, 권장 50MB) 때문에 올리지 않고 압축본만 둔다.
# 다시 쓸 때는 압축본을 풀어 .db 로 만든다 (update-data.yml 의 Restore 단계).
# 대시보드(macro-dashboard)는 https://raw.githubusercontent.com/HYANGKI-LEE/fred/data/output/db/<이름>.db.gz 를 읽는다.
#
#   bash publish_data.sh          # GitHub Actions (update-data.yml) 와 로컬 모두 사용
#
# GitHub Actions 에서는 GITHUB_TOKEN 으로, 로컬에서는 origin 주소(저장된 자격 증명)로 push 한다.
set -euo pipefail

cd "$(dirname "$0")"
shopt -s nullglob
files=(output/db/*.db.gz)
if [ ${#files[@]} -eq 0 ]; then
  echo "output/db 에 DB 파일이 없어요" >&2
  exit 1
fi

if [ -n "${GITHUB_TOKEN:-}" ] && [ -n "${GITHUB_REPOSITORY:-}" ]; then
  remote="https://x-access-token:${GITHUB_TOKEN}@github.com/${GITHUB_REPOSITORY}.git"
else
  remote="$(git remote get-url origin)"
fi

tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
mkdir -p "$tmp/output/db"
cp "${files[@]}" "$tmp/output/db/"
cat > "$tmp/README.md" <<'EOF'
# data 브랜치

`output/db/` 의 SQLite DB 압축본(.db.gz)만 두는 브랜치예요. 매번 이력 없이 덮어씁니다 (main 의 publish_data.sh).
풀면(gunzip) 바로 SQLite DB예요. 코드와 설명은 main 브랜치를 보세요.
EOF

git -C "$tmp" init -q
git -C "$tmp" checkout -q -b data
git -C "$tmp" add -A
git -C "$tmp" -c user.name="${GIT_AUTHOR_NAME:-fred-data-bot}" -c user.email="${GIT_AUTHOR_EMAIL:-fred-data-bot@users.noreply.github.com}" \
  commit -q -m "data $(date -u +%Y-%m-%dT%H:%MZ)"

# 올라가 있는 data 브랜치와 내용이 같으면 push 하지 않음
if git -C "$tmp" fetch -q "$remote" data 2>/dev/null && git -C "$tmp" diff --quiet FETCH_HEAD HEAD; then
  echo ">>> data 브랜치와 같아서 건너뜀"
  exit 0
fi
git -C "$tmp" push -q -f "$remote" HEAD:data
echo ">>> data 브랜치에 올림: ${files[*]##*/}"
