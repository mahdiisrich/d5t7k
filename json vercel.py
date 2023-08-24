{
  "version": 2,
  "builds": [
    {
      "src": "bot.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "/bot.py"
    }
  ],
  "env": {
    "URL": "YOUR_VERCEL_URL"
  }
}
