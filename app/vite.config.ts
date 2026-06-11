import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { fileURLToPath } from 'node:url'

// Base path: Vercel serves at the domain root (it sets VERCEL=1 at build
// time); GitHub Pages serves under /Karman-Ghia-Project/. Override with
// BASE_PATH if deploying anywhere else.
const base = process.env.BASE_PATH ?? (process.env.VERCEL ? '/' : '/Karman-Ghia-Project/')

export default defineConfig({
  base,
  plugins: [react()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
      // Single source of truth: import the repo's canonical record directly.
      '@data/master-record.json': fileURLToPath(
        new URL('../data/master-record.json', import.meta.url)
      ),
    },
  },
  build: {
    outDir: 'dist',
    assetsInlineLimit: 0,
    chunkSizeWarningLimit: 600,
    rollupOptions: {
      output: {
        manualChunks: {
          react: ['react', 'react-dom'],
          recharts: ['recharts'],
          motion: ['framer-motion'],
        },
      },
    },
  },
})
