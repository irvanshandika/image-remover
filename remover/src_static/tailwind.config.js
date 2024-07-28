/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: "media",
  content: [
    '../templates/**/*.html'
  ],
  theme: {
    extend: {
      fontFamily: {
        "sora": ["Sora", "sans-serif"],
      },
    },
  },
  plugins: [],
}

