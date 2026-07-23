import type { Config } from 'tailwindcss';

const config: Config = {
  content: ['../../app/**/*.html'],
  theme: {
    extend: {
      colors: {
        cream: '#FFFFFF',
        sand: '#F3E8FF',
        ink: '#2E1065',
        body: '#4C1D95',
        muted: '#8B5CF6',
        coral: '#9333EA',
        coralDark: '#7E22CE',
        teal: '#A855F7',
        mustard: '#C084FC',
        leaf: '#D8B4FE',
        hairline: '#E9D5FF',
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
