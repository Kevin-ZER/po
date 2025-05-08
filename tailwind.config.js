/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        // Kali Linux inspired colors
        border: "hsl(var(--border))",
        input: "hsl(var(--input))",
        ring: "hsl(var(--ring))",
        background: "#1a1a1a", // Dark background
        foreground: "#00ff00", // Bright green text
        primary: {
          DEFAULT: "#00ff00", // Bright green
          foreground: "#1a1a1a",
        },
        secondary: {
          DEFAULT: "#ff00ff", // Magenta
          foreground: "#1a1a1a",
        },
        muted: {
          DEFAULT: "#00ffff", // Cyan
          foreground: "#1a1a1a",
        },
        accent: {
          DEFAULT: "#ffff00", // Yellow
          foreground: "#1a1a1a",
        },
        card: {
          DEFAULT: "#2a2a2a", // Slightly lighter background
          foreground: "#00ff00",
        },
        // Additional Kali Linux colors
        success: "#00ff00", // Green
        warning: "#ffff00", // Yellow
        error: "#ff0000", // Red
        info: "#00ffff", // Cyan
        purple: "#ff00ff", // Magenta
        blue: "#0000ff", // Blue
      },
      borderRadius: {
        lg: "var(--radius)",
        md: "calc(var(--radius) - 2px)",
        sm: "calc(var(--radius) - 4px)",
      },
    },
  },
  plugins: [],
} 