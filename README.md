# WellnessFlow

健康班手機版網站，使用 Vue + Vite + Element Plus + Tailwind CSS 建立。

## 開發

```bash
bun install
bun dev
```

## 部署到 GitHub Pages

### 1. 設定 base path

`vite.config.js` 中設定 `base` 為 repo 名稱：

```js
export default defineConfig({
  base: '/WellnessFlow/',
  // ...
})
```

### 2. 建立 GitHub Actions

新增 `.github/workflows/deploy.yml`，push 到 main 時自動 build 並部署到 GitHub Pages。

### 3. 開啟 GitHub Pages

repo Settings > Pages > Source 選擇 **GitHub Actions**。

### 4. 推送

```bash
git init
git add .
git commit -m "init"
git remote add origin <your-repo-url>
git push -u origin main
```

推送後 GitHub Actions 會自動 build 並部署。
