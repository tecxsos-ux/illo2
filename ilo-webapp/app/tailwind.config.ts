import type { Config } from 'tailwindcss';

const config: Config = {
  content: ['../../app/**/*.html'],
  theme: {
    extend: {
      colors: {
        cream: '#FAF7F2',
        sand: '#F1EBE2',
        ink: '#211D19',
        body: '#5C554D',
        muted: '#8A8178',
        coral: '#E2583E',
        coralDark: '#C7452E',
        teal: '#2E8C8C',
        mustard: '#D9A521',
        leaf: '#7A9E5C',
        hairline: '#E5DDD2',
      },
      fontFamily: {
        display: ['var(--font-fraunces)', 'Georgia', 'serif'],
        sans: ['var(--font-inter)', 'system-ui', 'sans-serif'],
      },
      borderRadius: {
        card: '20px',
        hero: '28px',
        xl2: '24px',
      },
      boxShadow: {
        lift: '0 20px 40px -20px rgba(33,29,25,.25)',
        soft: '0 8px 24px -12px rgba(33,29,25,.18)',
      },
      maxWidth: {
        site: '1200px',
      },
      keyframes: {
        marquee: {
          '0%': { transform: 'translateX(0)' },
          '100%': { transform: 'translateX(-50%)' },
        },
      },
      animation: {
        marquee: 'marquee 30s linear infinite',
      },
    },
  },
  plugins: [],
};

export default config;
