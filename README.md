# GitHub Pages

このブランチは公開サイト専用です。制作環境は `main` にあります。

- `index.html`: 紹介ページとプロンプト例
- `site.css`, `site.js`: サイトの表示と操作
- `demo.js`: 抽出した1枚のループ再生（元のスライドには影響しない）
- `build.py`: mainのHTMLから背景ページを抽出し、HTML/PDFをコピー
- `background.html`, `nco-intro.html`, `nco-intro.pdf`, `source-revision.txt`: 生成物

更新はmain側でビルド・コミット後、このブランチのworktreeで実行します。

```sh
uv run --with beautifulsoup4 python build.py /path/to/quarto-html
git add .
git commit -m "Update published slides"
git push origin gh-pages
```

公開設定: Settings → Pages → Deploy from a branch → gh-pages / (root)

`main` のpushだけではサイトは更新されません。プロンプト例を変える場合はindex.htmlとprompt.txtを一緒に編集してください。
