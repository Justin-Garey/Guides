# Notes on Next.js

- The `npm run dev` command also hosts the app on the network which is convenient when compared to Vite where you must specify to have the webpage opened up to your local network.
- For a SPA, create the components folder as a private folder within *app*. This will look like *app/_components* then the components can be sourced from there and they won't appear as paths to the app router.