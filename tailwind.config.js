/** @type {import('tailwindcss').Config} */
module.exports = {
    darkMode: 'class',
  content: [
    './templates/**/*.{html,js}',
    './templates/**/*.{html,js}',
    './node_modules/flowbite/**/*.js',
  ],
  theme: {
    variants: {
      extend: {
        backgroundColor: ['responsive', 'hover', 'focus', 'active'],
      },
    },
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
          primary: {"50":"#eff6ff","100":"#dbeafe","200":"#bfdbfe","300":"#93c5fd","400":"#60a5fa","500":"#3b82f6","600":"#2563eb","700":"#1d4ed8","800":"#1e40af","900":"#1e3a8a","950":"#172554"},
          "light-gray": "#303640",
							seconds: "rgba(6, 252, 63, 1)",
							minutes: "rgba(252, 230, 0, 1)",
							hours: "rgba(253, 41, 112, 1)",
        },
        aspectRatios: {
          '21/9': '21 / 9',
          '16/9': '16 / 9',
          '9/16': '9 / 16',
          '6/4': '6 / 4',
          '4/6': '4 / 6',
          '4/3': '4 / 3',
          '3/4': '3 / 4',
          '2/1': '2 / 1',
          '1/1': '1 / 1',
          '1/2': '1 / 2',
        }
    },
  },
  plugins: [require('flowbite/plugin')
    ({
      charts: true,
  }),
],
}

