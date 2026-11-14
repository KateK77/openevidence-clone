import {defineConfig} from 'vitest/config'
import react from '@vitejs/plugin-react'
import tailwind from '@tailwindcss/vite'
const proxy = {'/api': process.env.BACKEND_URL || 'http://127.0.0.1:8021'}
export default defineConfig({plugins:[react(),tailwind()],server:{proxy},preview:{proxy},test:{environment:'jsdom',include:['src/**/*.test.tsx']}})
