# Google Analytics

## Adding Google Analytics to a Vite + React App

The Google Analytics tag in a Vite + React application is added to the *index.html* file.

```html
<!doctype html>
<html lang="en">
<head>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXX"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag() { dataLayer.push(arguments); }
    gtag('js', new Date());

    gtag('config', 'G-XXXXXXXXX');
  </script>
  ...
</head>
...
</html>
```

## Adding Google Analytics to a Next.js + React App

The Google Analytics tag in a Next.js + React application is added to the *layout.tsx* file.

```tsx
export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
        {gtmId && (
          <>
            <noscript>
              <iframe
                src={`https://www.googletagmanager.com/ns.html?id=${gtmId}`}
                height="0"
                width="0"
                style={{ display: "none", visibility: "hidden" }}
              />
            </noscript>
            <GoogleTagManager gtmId={gtmId} />
          </>
        )}
      <body>
        {children}
      </body>
    </html>
  );
```
- In this case, the google tag is left as an environment variable. It should either be added in *.env.local* or if Github Actions are being used, add it as a repository variable under *Actions* in *Secretes and Variables* in the settings.

Building with Github Actions would then have a step such as:
```yaml
      - name: Build
        run: npm run build
        env:
          NEXT_PUBLIC_GTM_ID: ${{ vars.NEXT_PUBLIC_GTM_ID }}
```