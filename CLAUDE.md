# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

WellnessFlow is a mobile-optimized Vue 3 website for "健康班" (Health Class), deployed to GitHub Pages. Content is in Traditional Chinese (zh-TW).

## Commands

- **Dev server:** `bun dev`
- **Build:** `bun run build`
- **Preview production build:** `bun preview`
- **Install dependencies:** `bun install`

No test or lint commands are configured.

## Tech Stack

- **Framework:** Vue 3 with Composition API (`<script setup>`)
- **Build:** Vite 7, base path set to `/WellnessFlow/` for GitHub Pages
- **Styling:** Tailwind CSS 4 + Element Plus component library
- **Package manager:** Bun (lock file: `bun.lock`)
- **Deployment:** GitHub Actions auto-deploys to GitHub Pages on push to `main`

## Architecture

Single-page app with a flat structure. All UI lives in `src/App.vue` — there are no routed views or extracted components yet. Static images (1.jpg–8.jpg) are served from `public/`. The app entry point (`src/main.js`) registers Element Plus globally and mounts the Vue app.

Image paths are resolved using `import.meta.env.BASE_URL` to work correctly under the GitHub Pages subdirectory.
