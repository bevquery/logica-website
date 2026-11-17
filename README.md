# LOGICA website — start here

Seven-page, responsive, buildless HTML/CSS/JavaScript website. No package installation, framework, API key, paid font, or database required. All visible copy is editable directly in HTML. This package is a draft for review, not a published site.

## Preview on your computer

Unzip the folder and open index.html in a browser. Relative links, assets, and navigation work without a server. Optional: from this folder run `python3 -m http.server 8000`, then visit http://localhost:8000. Open index.html to begin; 404.html uses the final custom-domain home URL intentionally.

## Before publication

Read REVIEW-BEFORE-LAUNCH.md. Search HTML for `DETAIL TO CONFIRM` and resolve every amber placeholder box. Contact is by telephone until the real public email is added. There is no contact form and no message submission backend.

## GitHub Pages setup

1. Sign in to the GitHub account that should own this site. Create a repository such as `logica-website`. A public repository can use GitHub Free; private-repository Pages availability depends on plan. Never put secrets or customer information in it.
2. Upload the CONTENTS of this folder to the repository root, not the enclosing folder. index.html must be at the root. Preserve assets/ and compatibility subdirectories. Add `.nojekyll` using GitHub’s Add file > Create new file if your upload method skips hidden files.
3. Commit to `main`.
4. Open repository Settings > Pages. Under Build and deployment choose Deploy from a branch, select main and /(root), and Save.
5. Wait for the Pages deployment. Open the URL shown in Settings > Pages, normally https://YOUR-ACCOUNT.github.io/logica-website/.
6. Check all seven pages, the mobile menu, telephone links, and the old compatibility URLs. Paths are relative, so this works at a repository subpath as well as on a custom domain.

Official setup: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

### Hosting policy caveat

GitHub’s Pages limits say it is not intended/allowed as free hosting to run an online business or sites primarily facilitating commercial transactions or commercial SaaS. This package is an informational brochure without commerce, accounts, or SaaS, but do not assume this is permission for your use. Review the current terms before choosing production hosting. If the restriction rules it out, keep this exact code in GitHub and deploy the same folder to a static host such as Cloudflare Pages; no rewrite is necessary. No hosting or DNS change has been made.

https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits

## Move www.logicallc.com only when ready

1. Keep Google Sites live while reviewing the temporary URL.
2. Verify domain ownership in GitHub first; follow the current custom-domain documentation.
3. In repository Settings > Pages, set custom domain to www.logicallc.com. For branch publishing, GitHub creates a CNAME file. This draft intentionally omits CNAME so it cannot claim your live domain accidentally.
4. At your DNS provider, update only the required website record: www CNAME normally points to YOUR-ACCOUNT.github.io (no repository path). Remove the conflicting old www website record as required. Do not change nameservers wholesale or edit Google Workspace MX/email, SPF, DKIM, DMARC, or unrelated verification records.
5. Follow GitHub’s current instructions for the apex domain logicallc.com if you want both apex and www supported. Do not guess IP addresses; use the official current values.
6. When DNS and certificate provisioning finish, enable Enforce HTTPS. Test both domain variants, contact, mobile navigation and compatibility paths. Keep a copy of prior DNS values for rollback.

https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site
https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages
https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https

## Editing guide

- index.html: homepage
- notes-domino.html: Notes/Domino
- processit.html: ProcessIt support
- app-development.html: new application service
- selected-work.html: adapted existing case studies
- about.html: company and biography
- contact.html: telephone and email placeholder
- assets/styles.css: shared design, responsive layouts
- assets/site.js: mobile menu and current year
- assets/workflow.svg: original homepage illustration
- assets/favicon.svg: original favicon
- IMAGE-LICENSE.txt: image reuse details

Header/footer markup is deliberately in every HTML page, so navigation changes must be repeated across the seven pages. Page content is available without JavaScript. No CDN dependencies.

Compatibility folders retain /home, /capabilities, /industries, /about, /contact, /capabilities/lotus-notesdomino and its /case-studies page. These contain immediate HTML meta-refresh redirects and visible fallback links, NOT HTTP 301 redirects. GitHub Pages cannot configure server-side redirects. Moving to a host with redirect rules allows true permanent redirects later.

## Search and future improvements

Descriptive titles and descriptions are included. No canonical URLs, sitemap or social share image are hardcoded until the final production domain is confirmed. After cutover, add canonical URLs and sitemap entries using https://www.logicallc.com/ and submit the sitemap to Search Console. For more accurate page previews when sharing, add approved social metadata and an image. Add analytics only if useful and after deciding appropriate disclosures.

## Verification

Run `python3 validate.py` for local HTML link, asset, duplicate-ID, fragment, title, description, and SVG parsing checks. It does not replace browser, accessibility or email-delivery testing. See QA-NOTES.md for delivered checks.
