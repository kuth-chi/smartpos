/** @type {import('tailwindcss').Config} */
module.exports = {
    darkMode: 'class',
  content: [
    './templates/**/*.{html,js}',
    './templates/**/*.{html,js}',
  ],
  theme: {
    extend: {
            fontFamily: {
            battambang: ['Battambang', 'cursive'],
            borel: ['Borel', 'cursive'],
            'great-vibes': ['Great Vibes', 'cursive'],
            moul: ['Moul', 'cursive'],
            moulpali: ['Moulpali', 'sans-serif'],
            mulish: ['Mulish', 'sans-serif'],
            'odor-mean-chey': ['Odor Mean Chey', 'serif'],
            yellowtail: ['Yellowtail', 'cursive'],
            digital: ['Digital', 'cursive'],
        },
        colors: {
          darkBlue: 'hsl(217, 28%, 15%)',
          darkBlue1: 'hsl(218, 28%, 13%)',
          darkBlue2: 'hsl(216, 53%, 9%)',
          darkBlue3: 'hsl(219, 30%, 18%)',
          accentCyan: 'hsl(176, 68%, 64%)',
          accentBlue: 'hsl(198, 60%, 50%)',
          lightRed: 'hsl(0, 100%, 63%)',
        },
    },
  },
  plugins: [],
}

