import {defineConfig,devices} from '@playwright/test'

export default defineConfig({
  testDir:'./e2e',
  use:{baseURL:'http://127.0.0.1:5174',trace:'retain-on-failure'},
  projects:[
    {name:'desktop',use:{...devices['Desktop Chrome']}},
    {name:'mobile',use:{...devices['iPhone 13'],defaultBrowserType:'chromium'}},
  ],
  webServer:{command:'node node_modules/vite/bin/vite.js --host 127.0.0.1 --port 5174 --strictPort',url:'http://127.0.0.1:5174',reuseExistingServer:!process.env.CI},
})
