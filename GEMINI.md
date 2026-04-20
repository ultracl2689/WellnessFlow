# WellnessFlow Project Context

## Project Overview
WellnessFlow is a mobile-optimized website for "健康班" (Health Class). It is a single-page application (SPA) built with Vue 3, using a modern tech stack focused on performance and developer experience.

- **Primary Language:** Traditional Chinese (zh-TW).
- **Architecture:** Single-page app with a flat structure. Main UI logic resides in `src/App.vue`.
- **Deployment:** Automatically deployed to GitHub Pages via GitHub Actions on every push to the `main` branch.

## Tech Stack
- **Framework:** Vue 3 (Composition API with `<script setup>`)
- **Build Tool:** Vite 7
- **Package Manager:** Bun (preferred)
- **Styling:**
  - Tailwind CSS 4 (integrated via `@tailwindcss/vite`)
  - Element Plus (component library)
- **Deployment:** GitHub Actions

## Key Commands
- **Install Dependencies:** `bun install`
- **Development Server:** `bun dev` (runs at `http://localhost:5173/WellnessFlow/`)
- **Build for Production:** `bun run build`
- **Preview Production Build:** `bun run preview`

## Project Structure
- `src/App.vue`: The heart of the application, containing image handling, navigation logic, and the main layout.
- `src/main.js`: Entry point that initializes Vue and registers Element Plus.
- `src/components/`: Contains UI components like `ComingSoon.vue` (used for development placeholders).
- `public/`: Stores static assets, specifically numbered images (`1.jpg` to `7.jpg`) used in the main scroll view.
- `vite.config.js`: Configured with `base: '/WellnessFlow/'` to ensure correct pathing on GitHub Pages.
- `.github/workflows/deploy.yml`: Defines the CI/CD pipeline for GitHub Pages.

## Development Conventions
- **Image Resolution:** Always use `import.meta.env.BASE_URL` when referencing assets in `public/` to ensure they resolve correctly across environments (local dev vs. GitHub Pages subdirectory).
- **Development Mode:** `src/App.vue` includes a `DEV` toggle (visible only in dev mode) to switch between the live site and a `ComingSoon` placeholder.
- **Styling:** Use Tailwind CSS for utility-first styling and Element Plus for complex UI components (like buttons).
- **Git Flow:**
  - `develop`: Main development branch.
  - `main`: Deployment branch. Merging to `main` triggers the production deployment.

## Critical Files
- `package.json`: Project metadata and dependencies.
- `SETUP_GUIDE.md`: Detailed instructions for environment setup and project recreation.
- `CLAUDE.md`: Operational guidelines for AI assistants.
- `vite.config.js`: Essential for build configuration and base pathing.
