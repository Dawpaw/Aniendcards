# Aniendcards — Frontend (Vibecoded)

SvelteKit + Tailwind CSS v4 frontend for the Aniendcards database.

## Local Setup

**Prerequisites:** Node.js 18+

```bash
# 1. Clone and enter the repo
git clone https://github.com/Dawpaw/Aniendcards.git
cd Aniendcards

# 2. Install dependencies
npm install

# 3. Configure environment
cp .env.example .env
# Edit .env and set VITE_API_URL to your FastAPI backend URL
# Default: http://localhost:8000

# 4. Start dev server
npm run dev
```

The site will be available at http://localhost:5173.

## Building for Production

```bash
npm run build
npm run preview   # preview the production build locally
```

## Project Structure

```
src/
├── app.css                  # Global styles + design tokens (Tailwind v4 @theme)
├── app.html                 # HTML shell (Google Fonts loaded here)
├── lib/
│   ├── api.js               # All API calls — single source of truth
│   └── components/
│       ├── Navbar.svelte
│       ├── Footer.svelte
│       ├── EndcardCard.svelte
│       └── MediaCard.svelte
└── routes/
    ├── +layout.svelte       # Root layout (Navbar + Footer)
    ├── +page.svelte         # Home — latest endcards + media
    ├── +page.server.js
    ├── about/               # About page
    ├── media/               # Media list + detail (/media/[id])
    └── endcards/            # Endcard list + detail (/endcards/[id])
```

## Connecting to the API

All API calls go through `src/lib/api.js`. Change `VITE_API_URL` in `.env` to point to your backend.

Only GET endpoints are used — the site is read-only.
