import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { fileURLToPath } from 'node:url'

// GitHub Pages project site: served under /Karman-Ghia-Project/
export default defineConfig({
  base: '/Karman-Ghia-Project/',
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
